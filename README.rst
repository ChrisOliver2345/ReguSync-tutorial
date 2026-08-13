ReguSync Tutorial
=================

This repository contains the Sphinx source for the ReguSync user guide.

Read the published documentation at:

https://regusync-tutorial.readthedocs.io/en/latest/

Build locally
-------------

From the repository root, install the documentation dependencies and build the
HTML site:

.. code-block:: console

   python -m pip install -r docs/requirements.txt
   python -m sphinx -W --keep-going -b html docs/source docs/build/html

Open ``docs/build/html/index.html`` after the build completes.
