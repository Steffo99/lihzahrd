########
Lihzahrd
########

.. image:: https://terraria.wiki.gg/images/Lihzahrd.gif
    :alt: A Lihzahrd walking.

**Lihzahrd** is a suite of utilities for the manipulation of Terraria save files.

Its name, Lihzahrd, comes from `the Terraria enemy of the same name`_, and corresponds to the word "`lizard`_" with an "h" after each vowel.

It features a Python interface to load, edit, and save Terraria worlds, and a small command-line interface to perform some basic tasks, which also acts as an example on how the package can be used.

.. versionchanged:: 4.0.0b1

    The version 4 of Lihzahrd is a **backwards-incompatible** rewrite of the whole library. If coming from version 3 or earlier, expect things to be very different!

.. _the Terraria enemy of the same name: https://terraria.wiki.gg/wiki/Lihzahrd
.. _lizard: https://en.wiktionary.org/wiki/lizard

.. warning::

    The rewrite of the library is pretty recent, and as a result is not yet very mature.

    - Due to a lack of time, not many tests were written, so test coverage is very low! The likelihood of bugs is therefore much higher.
    - Class names are sometimes inconsistent, since a :ref:`h-style_guide` was not fully developed;
    - Let's improve the ergonomicity together: please let us know what you find painful to use, so that we can improve it!
    - Let's also improve the documentation: please let us know if you don't understand something in these docs, so that we can fix that!

.. tip::

    If you found this package useful, please consider `leaving a tip`_ to `Steffo`_, its main developer!

    It will allow him to dedicate more time in the future to both this and other similar projects!

.. todo::

    Terraria 1.4.5.6 data is currently missing.

    Research and add the new :mod:`~lihzahrd.terraria.data` and :class:`~lihzahrd.terraria.common.file_version.FileVersion` when possible.

.. _leaving a tip: https://ko-fi.com/steffo
.. _Steffo: https://www.steffo.eu/


Table of contents
=================

.. toctree::
    :caption: User guide
    :titlesonly:

    user/01_install
    user/02_cli

.. toctree::
    :caption: Developer guide
    :titlesonly:

    developer/01_lihzahrd
    developer/02_common

.. toctree::
    :caption: Contributor guide
    :titlesonly:

    contributor/01_generate
    contributor/02_style


Links
=====

- `Git forge <https://g.starshard.space/steffo/lihzahrd>`_
- `PyPI package <https://pypi.org/project/lihzahrd/>`_
- `Tipping <https://ko-fi.com/steffo>`_
- :ref:`genindex`

.. todo::

    Where to provide support for the library?
