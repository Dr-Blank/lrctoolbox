.. meta::
   :description: Python library for working with LRC files. It can be used to
                 read, write, modify and create synchronized lyrics files.

LRCToolbox
==========

Toolkit to work with `LRC files
<https://en.wikipedia.org/wiki/LRC_(file_format)>`_ in Python. Read, modify
and write synchronized lyrics, including their metadata tags.

Installation
------------

LRCToolbox requires Python 3.11 or newer and has no runtime dependencies.

.. code-block:: bash

   pip install lrctoolbox

or, in a uv project:

.. code-block:: bash

   uv add lrctoolbox

Quick start
-----------

.. code-block:: python

   from lrctoolbox import SyncedLyrics

   # load an LRC file
   lyrics = SyncedLyrics.load_from_file("example.lrc")

   # check that every line has a timestamp, in ascending order
   assert lyrics.is_synced

   # shift all lyrics by 1 second
   for line in lyrics:
       line.timestamp += 1000

   # change metadata and save
   lyrics.artist = "New Artist"
   lyrics.save_to_file("example_new.lrc", overwrite=True)

Continue with the :doc:`examples/index` or browse the
:doc:`API reference <modules>`.

.. toctree::
   :maxdepth: 2
   :hidden:

   examples/index
   modules
   contributing

Indices
-------

* :ref:`genindex`
* :ref:`modindex`
