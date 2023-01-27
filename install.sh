#!/bin/sh

[ -d "dist" ] && rm -rf dist/*

[ -x "$(command -v python3)" ] || echo "python3 is not installed" && exit 1

[ -x "$(command -v poetry)" ] && poetry build || echo "poetry is not installed" && exit 1

python3 -m pip install $(ls dist/*.tar.gz)
