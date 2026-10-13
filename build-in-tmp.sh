#!/usr/bin/env bash
# Build a source copy outside the checkout and the quota-limited /tmp filesystem.
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
build_parent="/var/tmp/dusko-sphinx-builds"
mkdir -p "$build_parent"
chmod 700 "$build_parent"
build_root="$(mktemp -d "$build_parent/ecis-build.XXXXXX")"
cp -a "$repo_root/source" "$build_root/source"
mkdir -p "$build_root/tmp"
export CF_RUN_REMOTE_IMPORTS=0
export CF_PROTECTED_REPO_ROOT="$repo_root"
export CF_REMOTE_IMPORT_ROOT="$build_root/source"
export TMPDIR="$build_root/tmp"
export PYTHONPYCACHEPREFIX="$build_root/pycache"
printf 'Build directory: %s\n' "$build_root"
cd "$build_root/source"
sphinx-build -q -j auto -b html -d "$build_root/doctrees" \
    -w "$build_root/warnings.log" "$build_root/source" "$build_root/html"
printf 'HTML output: %s\nWarnings: %s\n' "$build_root/html" "$build_root/warnings.log"
