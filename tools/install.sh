#!/usr/bin/env bash
set -euo pipefail
python3 -m pip install --user pyyaml >/dev/null
chmod +x tools/*.py
printf '[ok] ProjectForge tools prepared.\n'
