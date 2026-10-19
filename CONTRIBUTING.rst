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

1. Bump the version in ``pyproject.toml``:

   .. code-block:: bash

      uv version --bump patch   # or minor / major

2. Commit, push, and create a GitHub release with a ``vX.Y.Z`` tag.
3. Publishing the release runs the ``PyPi Publish`` workflow, which builds
   with ``uv build`` and uploads to PyPI through trusted publishing. No API
   token is involved.

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
