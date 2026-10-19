LRC Toolbox
===========

<p>
  <a href="https://pypi.org/project/lrctoolbox/">
    <img src="https://img.shields.io/pypi/v/lrctoolbox?color=purple" alt="Stable Version">
  </a>
  <a href="https://pypistats.org/packages/lrctoolbox">
    <img src="https://img.shields.io/pypi/dm/lrctoolbox?color=blue" alt="Downloads">
  </a>
  <a href="https://github.com/Dr-Blank/lrctoolbox/actions">
    <img src="https://github.com/Dr-Blank/lrctoolbox/actions/workflows/tests.yaml/badge.svg" alt="Test">
  </a>
  <a href="https://codecov.io/gh/Dr-Blank/lrctoolbox" >
    <img src="https://codecov.io/gh/Dr-Blank/lrctoolbox/graph/badge.svg"/>
  </a>
  <a href='https://lrctoolbox.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/lrctoolbox/badge/?version=latest' alt='Documentation Status' />
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
  </a>
  <a href="https://mypy-lang.org/">
    <img src="https://www.mypy-lang.org/static/mypy_badge.svg" alt="Checked with mypy">
  </a>
</p>


Toolkit to work with [LRC Files](https://en.wikipedia.org/wiki/LRC_(file_format)) in Python

## Usage

```python
from lrctoolbox import SyncedLyrics

# Load LRC file
lyrics = SyncedLyrics.load_from_file("example.lrc")

# check if lyrics are synced
assert lyrics.is_synced

# get lyrics as string
print(lyrics.lyrics)

# shift lyrics by 1 second
for line in lyrics.lines:
    line.timestamp += 1000
```

## Development

[uv](https://docs.astral.sh/uv/) is used for dependency management. Install it and then run `uv sync` to install all dependencies.
