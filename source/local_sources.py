"""Resolve legacy article links and publish redirects to canonical documents."""
from __future__ import annotations

import html
import json
import os
import posixpath
import re
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


def configure(app, config):
    if os.environ.get('READTHEDOCS', '').lower() != 'true':
        for label, directory in (('source', app.srcdir), ('HTML', app.outdir), ('doctrees', app.doctreedir)):
            path = Path(directory).resolve()
            if any((parent / '.git').exists() for parent in (path, *path.parents)):
                raise ConfigError(f'Local {label} directory must be outside the Git checkout. Run ./build-in-tmp.sh.')
    aliases = json.loads((Path(app.confdir) / 'local_doc_aliases.json').read_text())
    redirects = json.loads((Path(app.confdir) / 'local_doc_redirects.json').read_text())
    for old, new in redirects.items():
        for path in (old, new):
            if path.startswith('/') or '..' in path.split('/') or urlsplit(path).scheme:
                raise ConfigError(f'Invalid article redirect path: {path}')
        if old == new or new in redirects:
            raise ConfigError(f'Article redirects must resolve in one step: {old} -> {new}')
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
    source[0] = rewrite_roles(source[0], app._local_doc_aliases, docname)


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
    return {'version': '2.0', 'parallel_read_safe': True, 'parallel_write_safe': True}
