# language=rst
"""
Module for everything in common between all kinds of Terraria save files.

Assuming a save file is not encrypted, as is the case for character files, you can use the items made available by this module to determine the kind of save file you're dealing with.

.. admonition:: Example

    .. code-block:: python

        from lihzahrd.terraria.utils.packer import Packer
        from lihzahrd.terraria.common.file_metadata import FileMetadata

        with open("tests/lihzahrd/terraria/world/Honey_of_Privacy.wld") as stream:
            fp = Packer(stream)
            metadata = FileMetadata.read(fp).instance
            print(metadata.kind)
            metadata.revision.value += 1
            print(metadata.revision)


``file_metadata``
=================

.. automodule:: lihzahrd.terraria.common.file_metadata


``file_version``
================

.. automodule:: lihzahrd.terraria.common.file_version


``file_signature``
==================

.. automodule:: lihzahrd.terraria.common.file_signature


``file_kind``
=============

.. automodule:: lihzahrd.terraria.common.file_kind


``file_revision``
=================

.. automodule:: lihzahrd.terraria.common.file_revision


``file_flags``
==============

.. automodule:: lihzahrd.terraria.common.file_flags

"""
