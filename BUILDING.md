# Article sources and local builds

Keep each article and its own assets in a matching directory:

```text
source/accountmanagement/Active-services/
    Active-services.rst
    active-service-billing-ecis-portal.png
    track-usage-summary-fra1-3-ecis-portal.png
```

Section indexes stay at section level, for example
`source/accountmanagement/accountmanagement.rst`. Shared images may remain at
section level. Source `:doc:` links and toctrees use the actual article paths.

Run `./build-in-tmp.sh` for a local preview. The launcher puts its workspace,
HTML, doctrees, caches and logs under `/var/tmp/dusko-sphinx-builds/` and prints
the locations. Keep this workspace while its preview server is running.

The local article importer in `source/local_sources.py` runs on both local
builds and Read the Docs. It reads the committed article folders and prepares
a separate temporary Sphinx source tree. Only this build copy is flattened.
For example, `Active-services/Active-services.rst` becomes
`Active-services.rst` in the build copy, preserving the published URL
`/accountmanagement/Active-services.html`.

The importer converts source links and toctrees to the published document
paths, preserves asset paths and never writes generated articles into the
repository. Read the Docs continues to use `source/conf.py`; no extra remote
article downloads or sibling repositories are needed.

`source/local_doc_aliases.json` and `source/local_doc_redirects.json` describe
published document paths. Historical branded and nested URLs redirect to the
short debranded URLs. These maps are not source-file inventories.
