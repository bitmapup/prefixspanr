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

if you would install in your environment
::

   python setup.py install

if you would install in your development environment
::

   python setup.py develop

coming soon install by pip...


Make sure to read the ``README.md`` in the public repository for notes on dependencies and installation.

``copper`` depends on the following packages which will be installed by pip during the installation process

- ``psutil``
- ``pandas``
- ``numpy``
- ``resources`` (Only in Linux-like OS)