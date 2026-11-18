#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

CONF="book/conf.py"
EXTENSION_PATH="sys.path.insert(0, os.path.join(os.path.dirname(__file__), '_ext'))"
AUTHORS_SETTING="git_show_all_authors = False"


jupyter-book config sphinx book/

# Not `sed -i`: it creates a temporary file inside book/ (watched by sphinx-autobuild),
# which retriggers the build and therefore this script, endlessly.
TMP_CONF="$(mktemp)"
trap 'rm -f "$TMP_CONF"' EXIT

sed "/# re-generate this one/a\\
import os\\
import sys\\
\\
$EXTENSION_PATH" "$CONF" > "$TMP_CONF"
cat "$TMP_CONF" > "$CONF"

sed 's/git_show_all_authors = True/git_show_all_authors = False/' "$CONF" > "$TMP_CONF"
cat "$TMP_CONF" > "$CONF"

grep -Fq "$EXTENSION_PATH" "$CONF"
grep -Fq "$AUTHORS_SETTING" "$CONF"
