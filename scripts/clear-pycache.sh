#!/usr/bin/env bash

# List or delete __pycache__ dirs, excluding .venv

set -euo pipefail

if [[ "${1:-}" == "-y" ]]; then
  echo "Deleting all __pycache__ directories (excluding .venv)..."
  set -x
  find . -path './.venv' -prune -o -type d -name '__pycache__' -exec rm -r {} +
  set +x
else
  echo "Dry-run: listing __pycache__ directories (excluding .venv)..."
  find . -path './.venv' -prune -o -type d -name '__pycache__' -print
  echo
  echo "Run with '-y' to delete them."
fi



