.. _h-style_guide:

###########
Style guide
###########

Variable naming
===============

- Use ``UPPERCASE`` names for module-level constants, or class-level attributes.

- Use ``lowercase`` names for module-level variables, or instance-level attributes, or methods in general.

- Use names prefixed by an underscore ``_`` for protected attributes, both class-level and instance-level.

- Suffix :class:`~enum.Enum` subclasses and :term:`ClassEnum` with ``...Enum``.

  .. todo::

      This runs counter to Python's intended naming scheme, where ``...Enum`` implies that something is an *enum metaclass*.

      Maybe it could be changed?

- Suffix :term:`ClassMemberBase` with ``...Base``.

  .. todo::

      This feels a bit odd to write, especially when doing typing.

      A :class:`type`\ [:class:`~lihzahrd.terraria.data.classmembers.item_base.ItemBase`\ ] is the kind of an item, an ``ItemBase`` is a stack?

      Maybe that could be changed, too?

.. todo::

    Decide on when to use ``Pack...`` and ``World...`` prefixes, and when to avoid them.


Module organization
===================

.. todo::

    Fully develop the hierarchy describing which classes go where with no ambiguity.


Documentation
=============

- Follow the `Python Developer's Guide`_ for documenting sections.

- Either use ``:caption:`` to document the context of ``.. code-block``, or, alternatively, wrap it in a ``.. admonition:: Example`` if applicable.

.. _Python Developer's Guide: https://devguide.python.org/documentation/markup/#sections
