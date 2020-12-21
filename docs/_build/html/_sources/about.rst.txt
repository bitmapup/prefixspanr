Description
===========

copper is a package which implements following sequential mining algorithms:

- PrefixSpan [Pei2002]_
- COPPER [Guevara2015]_
- PrefixSpan with Time constraints capabilities  [Alatrista2020]_
- COPPER with Time constraints capabilities [Alatrista2020]_

.. Extension of COPPER  with time constraints capabilities, improving the selection of interesting patterns for expert

Install
========

Install by Source Code
----------------------

if you clone repository or download the source you can install in your environment you will use:
::

   python setup.py install

or if you would install in your development environment you will use:
::

   python setup.py develop

Install by Pip
--------------

you can install last release using:
::

   pip install git+https://github.com/bitmapup/prefixspanr.git

or a specific version using:
::

   pip install git+https://github.com/bitmapup/prefixspanr.git@v1.0


Make sure to read the ``README.md`` in the public repository for notes on dependencies and installation.

``wincopper`` depends on the following packages which will be installed by pip during the installation process

- ``psutil``
- ``pandas``
- ``numpy``
- ``resources`` (Only in Linux-like OS)