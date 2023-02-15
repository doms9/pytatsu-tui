#!/bin/sh

failed() {
    printf '%s\n' "$1" >&2
    exit "${2-1}"
}

[ -d "dist" ] && rm -rf dist/*

[ -x "$(command -v python3)" ] || failed "python3 is not installed"

[ -x "$(command -v poetry)" ] || failed "poetry is not installed"

poetry build || failed "poetry failed to build python package"

python3 -m pip install $(ls dist/*.tar.gz)
