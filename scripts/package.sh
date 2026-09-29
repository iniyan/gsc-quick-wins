#!/usr/bin/env bash
# Builds dist/gsc-quick-wins.zip — the file people upload in Claude.ai → Settings → Capabilities → Skills.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
(cd skills && zip -rq ../dist/gsc-quick-wins.zip gsc-quick-wins -x '*.DS_Store' '*__pycache__*')
echo "Built dist/gsc-quick-wins.zip"
unzip -l dist/gsc-quick-wins.zip
