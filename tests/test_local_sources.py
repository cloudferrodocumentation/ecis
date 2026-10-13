"""Safety and URL checks for the local article importer."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from sphinx.errors import ConfigError

spec = importlib.util.spec_from_file_location('local_sources', Path(__file__).resolve().parents[1] / 'source/local_sources.py')
local_sources = importlib.util.module_from_spec(spec)
spec.loader.exec_module(local_sources)


class LocalSourceImportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'repository/source'
        self.source.mkdir(parents=True)
        (self.source.parent / '.git').mkdir()
        self.article = self.source / 'section/Article/Article.rst'
        self.article.parent.mkdir(parents=True)
        self.article.write_text('Article\n=======\n\nOriginal content.\n')
        (self.article.parent / 'image.png').write_bytes(b'image')
        self.output = self.root / 'build/imported-source'

    def test_external_flat_copy_preserves_originals_and_assets(self):
        originals = {p.relative_to(self.source): p.read_bytes() for p in self.source.rglob('*') if p.is_file()}
        docnames = local_sources.import_local_sources(self.source, self.output)
        self.assertEqual(docnames['section/Article/Article'], 'section/Article')
        self.assertEqual((self.output / 'section/Article.rst').read_bytes(), self.article.read_bytes())
        self.assertEqual((self.output / 'section/Article/image.png').read_bytes(), b'image')
        self.assertFalse((self.output / 'section/Article/Article.rst').exists())
        self.assertEqual(originals, {p.relative_to(self.source): p.read_bytes() for p in self.source.rglob('*') if p.is_file()})

    def test_incremental_copy_updates_and_removes_only_owned_files(self):
        local_sources.import_local_sources(self.source, self.output)
        self.article.write_text('Updated content.\n')
        (self.output / 'unowned.txt').write_text('Keep me')
        local_sources.import_local_sources(self.source, self.output)
        self.assertEqual((self.output / 'section/Article.rst').read_text(), 'Updated content.\n')
        self.article.unlink()
        local_sources.import_local_sources(self.source, self.output)
        self.assertFalse((self.output / 'section/Article.rst').exists())
        self.assertTrue((self.output / 'unowned.txt').exists())

    def test_rejects_repository_overlap_and_unmanaged_destinations(self):
        for destination in [self.source, self.source / 'build', self.source.parent / 'build', self.source.parent]:
            with self.subTest(destination=destination), self.assertRaises(ConfigError):
                local_sources.import_local_sources(self.source, destination)
        self.output.mkdir(parents=True)
        (self.output / 'existing.txt').write_text('Keep me')
        with self.assertRaises(ConfigError):
            local_sources.import_local_sources(self.source, self.output)

    def test_rejects_flat_and_nested_duplicate(self):
        (self.source / 'section/Article.rst').write_text('Duplicate')
        with self.assertRaises(ConfigError):
            local_sources.import_local_sources(self.source, self.output)
        self.assertFalse(self.output.exists())

    def test_source_links_and_toctrees_keep_short_urls(self):
        aliases = {'/section/Article/Article': '/section/Article'}
        text = '.. toctree::\n   :maxdepth: 1\n\n   A label <Article/Article>\n\n:doc:`Read it </section/Article/Article>`\n'
        actual = local_sources.rewrite_toctrees(local_sources.rewrite_roles(text, aliases, 'section/section'), aliases, 'section/section')
        self.assertIn('A label </section/Article>', actual)
        self.assertIn(':doc:`Read it </section/Article>`', actual)
        self.assertIn(':maxdepth: 1', actual)

    def test_rtd_checkout_uses_external_import_directory(self):
        for filename in ['local_doc_aliases.json', 'local_doc_redirects.json']:
            (self.source / filename).write_text('{}')
        app = SimpleNamespace(srcdir=str(self.source), confdir=str(self.source),
                              outdir=str(self.source.parent / '_build/html'),
                              doctreedir=str(self.source.parent / '_build/doctrees'))
        config = SimpleNamespace(jinja_contexts={}, rst_prolog='', rst_epilog='')
        external = self.root / 'rtd-temporary-source'
        with patch.dict('os.environ', {'READTHEDOCS': 'true'}), patch.object(local_sources.tempfile, 'mkdtemp', return_value=str(external)):
            local_sources.configure(app, config)
        self.assertEqual(Path(app.srcdir), external)
        self.assertTrue(self.article.is_file())
        self.assertFalse((self.source / 'section/Article.rst').exists())
        self.assertTrue((external / 'section/Article.rst').is_file())
        self.assertEqual(app._local_doc_aliases['/section/Article/Article'], '/section/Article')


if __name__ == '__main__':
    unittest.main()
