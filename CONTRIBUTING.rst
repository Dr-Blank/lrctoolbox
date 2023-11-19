==================
Contributing Guide
==================

Getting Started
===============

To get started with contributing to this project, you'll need to set up your development environment. 

poetry is used for dependency management. Install it with `pip install poetry` and then run `poetry install` to install all dependencies.


Building Documentation
======================

We use Sphinx for documentation. You can set it up and build the docs as follows:

1. Install Sphinx: 

.. code-block:: bash

  pip install sphinx

2. Run the quickstart:

.. code-block:: bash

  sphinx-quickstart

Follow the prompts to set up your docs.


Autodoc
=======

We use autodoc for automatically generating documentation from the Python source code. Here's how to use it:

1. Install the Sphinx autodoc extension:

.. code-block:: bash

  pip install sphinx.ext.autodoc

2. In your `conf.py` file (created by `sphinx-quickstart`), add `'sphinx.ext.autodoc'` to the `extensions` list.

3. Use the `.. automodule::` directive in your `.rst` files to document Python modules. For example:

.. code-block:: rst

  .. automodule:: mymodule
    :members:

This will automatically document the `mymodule` module.

Please ensure that your Python code is well-documented with docstrings, as autodoc uses these to generate the documentation.


Using sphinx-apidoc
===================
If you have a large project with many modules, you can use the `sphinx-apidoc` command to automatically generate `.rst` files for each module. This will save you from having to manually create a `.rst` file for each module.

1. Install the Sphinx apidoc extension:

.. code-block:: bash

  pip install sphinx-apidoc

2. Run the `sphinx-apidoc` command:

.. code-block:: bash

  sphinx-apidoc -o docs/ mymodule

This will generate `.rst` files for each module in the `mymodule` package, and place them in the `docs/` directory. You can then edit these files to add more documentation.