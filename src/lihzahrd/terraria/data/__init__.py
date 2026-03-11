# language=rst
"""
Module containing Terraria game data not included in save files, but useful to represent their contents.

It contains some enumerations in the :mod:`~lihzahrd.terraria.data.enums` submodule, but most data is represented in the form of :ref:`h-class_enums`.

.. _h-class_enums:

******************
Class enumerations
******************

This module makes heavy use of *class enumerations*.

Class enumerations are similar to :class:`enum.Enum`, but while in those the enumeration is a class and its variants are its instances, in class enumerations the enumeration is a metaclass, while its variants are themselves classes instances of that metaclass.

This allows variants to have multiple properties of their own, and be themselves *instantiated*.


Class hierarchy
===============

The names and hierarchy of the classes involved in this abstraction are as follows:

.. glossary::

    :class:`~lihzahrd.terraria.data.classenumtype.class_enum_type.ClassEnumType`

        Abstract metaclass from which new *ClassEnum* should inherit normally.

        It represents the **type of collections of kinds of things**.

        Stored in the :mod:`~lihzahrd.terraria.data.classenumtype` submodule.

    ClassEnum

        The individual metaclasses which keep track of the classes that are created using them.

        They represent **collections of kinds of things**:

        - :class:`~lihzahrd.terraria.data.classenums.block_enum.BlockEnum` is the metaclass tracking (placed) block types;
        - :class:`~lihzahrd.terraria.data.classenums.wall_enum.WallEnum` is the metaclass tracking (placed) wall types;
        - :class:`~lihzahrd.terraria.data.classenums.item_enum.ItemEnum` is the metaclass tracking (in-inventory) item types;
        - :class:`~lihzahrd.terraria.data.classenums.npc_enum.NPCEnum` is the metaclass tracking non-player character types;
        - :class:`~lihzahrd.terraria.data.classenums.prefix_enum.PrefixEnum` is the metaclass tracking item prefix types;
        - :class:`~lihzahrd.terraria.data.classenums.liquid_enum.LiquidEnum` is the metaclass tracking (placed) liquid types.

        Stored in the :mod:`~lihzahrd.terraria.data.classenums` submodule.

    ClassMember

        The individual classes created using :term:`ClassEnum` as metaclass, tracked by them as members.

        They represent **kinds of things**:

        - *Blocks* are kinds of (placed) blocks;
        - *Walls* are kinds of (placed) walls;
        - *Items* are kinds of (in-inventory) items;
        - *Npcs* are kinds of non-player characters;
        - *Prefixes* are kinds of item prefixes;
        - *Liquids* are kinds of (placed) liquids.

        Stored in the :mod:`~lihzahrd.terraria.data.classmembers` submodule.

    ClassInstance

        The objects instantiated normally from :term:`ClassMember`.

        They represent **things** themselves:

        - A *block instance* corresponds to an actual block placed in a world;
        - A *wall instance* corresponds to an actual wall placed in a world;
        - An *item instance* corresponds to an actual item stack in an inventory in a world;
        - A *npc instance* corresponds to an actual NPC physically present in a world;
        - *Prefix instances* cannot be instantiated, as that would not make sense;
        - A *liquid instance* corresponds to an actual tile of liquid in a world.


Base classes
============

Some base classes are also defined, to provide various defaults to the classes in the above hierarchy:

.. glossary::

    ClassEnumTypeBase

        Class which implement ways to index the registered *ClassMembers*:

        - :class:`~lihzahrd.terraria.data.classenumtype.class_enum_type_dict.ClassEnumTypeDict` uses :class:`dict` to index the variants with multiple indexes.

        Stored in the :mod:`~lihzahrd.terraria.data.classenumtype` submodule.

    ClassMemberBase

        Class which defines *ClassMember* methods and properties and annotates them:

        - :class:`~lihzahrd.terraria.data.classmembers.block_base.BlockBase` does so for *blocks*;
        - :class:`~lihzahrd.terraria.data.classmembers.wall_base.WallBase` does so for *walls*;
        - :class:`~lihzahrd.terraria.data.classmembers.item_base.ItemBase` does so for *items*;
        - :class:`~lihzahrd.terraria.data.classmembers.npc_base.NPCBase` does so for *npcs*;
        - :class:`~lihzahrd.terraria.data.classmembers.prefix_base.PrefixBase` does so for *prefixes*.
        - :class:`~lihzahrd.terraria.data.classmembers.liquid_base.LiquidBase` does so for *liquids*.

        Stored in the :mod:`~lihzahrd.terraria.data.classmembers` submodule.

"""

from . import classenums
from . import classenumtype
from . import classmembers
from . import enums
from . import frameimportant_variant
