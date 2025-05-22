# Build project
build: clean
    uv build

# Publish project to PyPI
publish: build
    uvx uv-publish

# Clean project
clean:
    rm -rf dist

# Run tests
test:
    uv run pytest

# Run tests for all supported Python versions
test-all:
    #!/usr/bin/env bash
    for pyversion in 3.8 3.9 3.10 3.11 3.12 3.13; do
        uv run --python=$pyversion --isolated --locked pytest
    done

# Open project page on PyPI
pypi:
    open https://pypi.org/project/wrpy/
