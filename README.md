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

Toolkit to work with [LRC files](https://en.wikipedia.org/wiki/LRC_(file_format)) in Python. Read, modify and write synchronized lyrics, including their metadata tags.

## Installation

Requires Python 3.11 or newer. No runtime dependencies.

```bash
pip install lrctoolbox
# or
uv add lrctoolbox
```

## Usage

```python
from lrctoolbox import SyncedLyrics

# load an LRC file
lyrics = SyncedLyrics.load_from_file("example.lrc")

# check that every line has a timestamp, in ascending order
assert lyrics.is_synced

# get lyrics as a list of lines
print(lyrics.lyrics)

# shift all lyrics by 1 second
for line in lyrics:
    line.timestamp += 1000

# change metadata and save
lyrics.artist = "New Artist"
lyrics.save_to_file("example_new.lrc", overwrite=True)
```

More examples and the API reference are in the [documentation](https://lrctoolbox.readthedocs.io/).

## Development

```bash
uv sync
uv run pre-commit install
```

See [CONTRIBUTING.rst](CONTRIBUTING.rst) for tests, docs builds and the release process.
