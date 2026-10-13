"""Resolve legacy article links and publish redirects to canonical documents."""
from __future__ import annotations

import html
import json
import os
import posixpath
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import urlsplit

from sphinx import addnodes
from sphinx.errors import ConfigError


def resolve_target(target, aliases, docname=''):
    if not isinstance(target, str) or not target or '{{' in target:
        return target
    if target.startswith(('https://', 'http://', 'mailto:')):
        return target
    clean = target
    if not clean.startswith('/'):
        clean = '/' + posixpath.normpath(posixpath.join(posixpath.dirname(docname), clean))
    return aliases.get(clean, target)


def rewrite_roles(text, aliases, docname=''):
    def replace(match):
        value = match.group(1)
        titled = re.fullmatch(r'(.*?)\s*<([^<>]+)>', value)
        old = titled.group(2) if titled else value
        new = resolve_target(old, aliases, docname)
        return ':doc:`' + (titled.group(1) + ' <' + new + '>' if titled else new) + '`'
    return re.sub(r':doc:`([^`]+)`', replace, text)


def import_local_sources(source_root, build_root):
    """Import local article folders into an external, flat Sphinx source tree.

    Assets retain their paths. Only matching Article/Article.rst documents are
    flattened; section indexes and private static bundles keep their layout.
    """
    source_root = Path(source_root).resolve()
    build_root = Path(build_root).resolve()
    if (source_root == build_root or source_root in build_root.parents
            or build_root in source_root.parents):
        raise ConfigError('The local import tree must be separate from its sources.')
    if any((parent / '.git').exists() for parent in (build_root, *build_root.parents)):
        raise ConfigError('The local import tree must be outside every Git checkout.')

    manifest_path = build_root / '.local-source-import.json'
    previous = {}
    if manifest_path.exists():
        previous = json.loads(manifest_path.read_text())
        if previous.get('source_root') != str(source_root):
            raise ConfigError('The local import tree belongs to another source directory.')
    elif build_root.exists() and any(build_root.iterdir()):
        raise ConfigError('Refusing to overwrite an unmanaged local import directory.')

    files = {}
    docnames = {}
    for source in sorted(source_root.rglob('*')):
        relative = source.relative_to(source_root)
        if any(part in {'.git', '__pycache__', '_build'} for part in relative.parts):
            continue
        if not source.is_file():
            continue
        target = relative
        if (source.suffix == '.rst' and len(relative.parts) >= 3
                and not relative.parts[0].startswith('_')
                and source.stem == source.parent.name):
            target = relative.parent.parent / relative.name
        if target in files:
            raise ConfigError(f'Two local files would import to {target}.')
        files[target] = source
        if source.suffix == '.rst':
            docnames[relative.with_suffix('').as_posix()] = target.with_suffix('').as_posix()

    build_root.mkdir(parents=True, exist_ok=True)
    for relative, source in files.items():
        target = build_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.is_symlink() or not target.resolve().is_relative_to(build_root):
            raise ConfigError(f'Unsafe local import destination: {target}')
        if not target.exists() or source.read_bytes() != target.read_bytes():
            shutil.copy2(source, target)
    # Remove only files recorded by this importer that no longer have a source.
    for relative in set(previous.get('files', [])) - {p.as_posix() for p in files}:
        target = build_root / relative
        if not target.resolve().is_relative_to(build_root):
            raise ConfigError(f'Unsafe previous local import path: {relative}')
        if target.is_file():
            target.unlink()
    manifest_path.write_text(json.dumps({
        'source_root': str(source_root), 'files': sorted(p.as_posix() for p in files),
        'docnames': docnames,
    }, indent=2) + '\n')
    return docnames


def rewrite_toctrees(text, aliases, docname=''):
    """Resolve article-folder entries without changing labels or ordering."""
    lines = []
    toctree_indent = None
    for line in text.splitlines(keepends=True):
        match = re.match(r'^(\s*)\.\.\s+toctree::\s*$', line)
        if match:
            toctree_indent = len(match.group(1))
        elif toctree_indent is not None and line.strip():
            indent = len(line) - len(line.lstrip())
            if indent <= toctree_indent:
                toctree_indent = None
            elif not line.lstrip().startswith((':', '..', '{%')):
                value = line.strip()
                titled = re.fullmatch(r'(.*?)\s*<([^<>]+)>', value)
                old = titled.group(2) if titled else value
                new = resolve_target(old, aliases, docname)
                if new != old:
                    entry = titled.group(1) + ' <' + new + '>' if titled else new
                    line = line[:indent] + entry + ('\n' if line.endswith('\n') else '')
        lines.append(line)
    return ''.join(lines)


def configure(app, config):
    source_root = Path(app.srcdir).resolve()
    on_rtd = os.environ.get('READTHEDOCS', '').lower() == 'true'
    if not on_rtd:
        for label, directory in (('HTML', app.outdir), ('doctrees', app.doctreedir)):
            path = Path(directory).resolve()
            if any((parent / '.git').exists() for parent in (path, *path.parents)):
                raise ConfigError(f'Local {label} directory must be outside the Git checkout. Run ./build-in-tmp.sh.')
    import_root = Path(app.doctreedir).resolve().parent / 'imported-source'
    if any((parent / '.git').exists() for parent in (import_root, *import_root.parents)):
        # RTD may keep its output/doctrees in the disposable checkout. Article
        # import output must still be outside that checkout.
        import_root = Path(tempfile.mkdtemp(prefix='ecis-local-import-', dir='/var/tmp'))
    docnames = import_local_sources(source_root, import_root)
    app.srcdir = str(import_root)
    app._local_source_docnames = docnames
    aliases = json.loads((Path(app.confdir) / 'local_doc_aliases.json').read_text())
    redirects = json.loads((Path(app.confdir) / 'local_doc_redirects.json').read_text())
    for old, new in redirects.items():
        for path in (old, new):
            if path.startswith('/') or '..' in path.split('/') or urlsplit(path).scheme:
                raise ConfigError(f'Invalid article redirect path: {path}')
        if old == new or new in redirects:
            raise ConfigError(f'Article redirects must resolve in one step: {old} -> {new}')
    aliases.update({'/' + old: '/' + new for old, new in docnames.items()})
    app._local_doc_aliases = aliases
    app._local_doc_redirects = redirects

    def walk(value):
        if isinstance(value, dict):
            return {key: walk(item) for key, item in value.items()}
        if isinstance(value, list):
            return [walk(item) for item in value]
        if isinstance(value, tuple):
            return tuple(walk(item) for item in value)
        if isinstance(value, str):
            return rewrite_roles(resolve_target(value, aliases), aliases)
        return value

    config.jinja_contexts = walk(config.jinja_contexts)
    config.rst_prolog = rewrite_roles(config.rst_prolog or '', aliases)
    config.rst_epilog = rewrite_roles(config.rst_epilog or '', aliases)


def read_source(app, docname, source):
    source[0] = rewrite_toctrees(
        rewrite_roles(source[0], app._local_doc_aliases, docname),
        app._local_doc_aliases, docname,
    )


def resolve_rendered_links(app, doctree):
    # Jinja document links become concrete only after source-read.
    for node in doctree.findall(addnodes.pending_xref):
        if node.get('reftype') == 'doc':
            node['reftarget'] = resolve_target(node['reftarget'], app._local_doc_aliases,
                                               node.get('refdoc', app.env.docname))


def write_redirects(app, exception):
    if exception is not None or app.builder.name != 'html':
        return
    for old, new in app._local_doc_redirects.items():
        if old in app.env.found_docs:
            raise ConfigError(f'Redirect still has an article source: {old}')
        if new not in app.env.found_docs:
            raise ConfigError(f'Redirect destination is missing: {old} -> {new}')
        relative = posixpath.relpath(new + '.html', posixpath.dirname(old) or '.')
        url = html.escape(relative, quote=True)
        output = Path(app.outdir) / (old + '.html')
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            '<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="robots" content="noindex">'
            f'<link rel="canonical" href="{url}">'
            '<title>Article moved</title>'
            '<script>window.location.replace(' + json.dumps(relative) +
            ' + window.location.search + window.location.hash);</script>'
            f'<meta http-equiv="refresh" content="0; url={url}">'
            f'</head><body><p>This article is now available <a href="{url}">here</a>.</p>'
            '</body></html>\n', encoding='utf-8'
        )


def setup(app):
    app.connect('config-inited', configure, priority=0)
    app.connect('source-read', read_source, priority=900)
    app.connect('doctree-read', resolve_rendered_links)
    app.connect('build-finished', write_redirects)
    return {'version': '3.0', 'parallel_read_safe': True, 'parallel_write_safe': True}
