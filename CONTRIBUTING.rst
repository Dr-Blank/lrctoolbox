==================
Contributing Guide
==================

Development setup
=================

`uv <https://docs.astral.sh/uv/>`_ manages the environment and dependencies.
Install it, then clone the repository and run:

.. code-block:: bash

   uv sync
   uv run pre-commit install

``uv sync`` creates ``.venv`` with the package and the ``dev`` dependency
group. ``pre-commit install`` sets up the git hook, so ruff (lint and
format), mypy and the ``uv.lock`` check run automatically on every commit.
To run all hooks over the whole repository by hand:

.. code-block:: bash

   uv run pre-commit run --all-files

Tests and checks
================

.. code-block:: bash

   uv run pytest                # tests
   uv run pytest --cov=lrctoolbox
   uv run ruff check .          # lint
   uv run ruff format .         # format
   uv run mypy                  # type check

CI runs the tests on Linux and Windows for every supported Python version,
plus ruff and mypy.

Documentation
=============

The docs use Sphinx with the Furo theme. API pages come from docstrings via
autodoc, and notebooks in ``docs/examples`` are rendered with myst-nb using
their saved outputs. Build them locally with warnings treated as errors, the
same way Read the Docs does:

.. code-block:: bash

   uv run --group docs sphinx-build -W -b html docs docs/_build/html

Read the Docs builds every push to ``main`` as ``latest`` and every release
tag as its own version.

Releasing
=========

Use `Conventional Commits <https://www.conventionalcommits.org/>`_ subjects
(``feat:``, ``fix:``, ``docs:``, ``build:``, ``feat!:`` for breaking
changes). The release notes are built from them.

In VS Code, run the ``release: bump version`` task (it asks for patch, minor
or major), then ``release: push``. By hand:

1. Bump the version, commit it and tag it:

   .. code-block:: bash

      uv version --bump patch   # or minor / major
      version=$(uv version --short)
      git commit -m "chore(release): $version" pyproject.toml uv.lock
      git tag -a "v$version" -m "v$version"

2. Push the branch together with the tag:

   .. code-block:: bash

      git push --follow-tags

3. The tag runs the ``Release`` workflow. It checks the tag matches the
   version in ``pyproject.toml``, runs the tests, builds with ``uv build``,
   uploads to PyPI through trusted publishing (no API token), then creates
   the GitHub release with notes grouped from the commits since the previous
   tag. To retry a failed run for an existing tag, start the workflow by hand
   with that tag.

Python version support
======================

Supported versions follow the CPython release cycle: a new version is added
to the CI matrix and classifiers once it is released, and a version is
dropped around its end of life. Dropping a version means raising
``requires-python`` in ``pyproject.toml``, removing it from the CI matrix and
classifiers, and releasing a new minor version. pip on the old interpreter
then keeps installing the last release that supported it.

Dependency updates
==================

Renovate opens weekly pull requests for Python dependencies, ``uv.lock``,
GitHub Actions and pre-commit hooks.
