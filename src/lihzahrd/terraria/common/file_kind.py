# language=rst
"""
Submodule for distinguishing between Terraria save file kinds.

.. seealso::

    :attr:`lihzahrd.terraria.common.file_metadata.FileMetadata.kind`

"""

from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackByte


class FileKind(IntEnum):
    """
    :class:`~enum.IntEnum` describing a kind of Terraria save file.
    """

    INVALID = 0
    "A specifically-invalid value."

    MAP = 1
    "A minimap."

    WORLD = 2
    """
    A world save file.
    
    .. seealso::
    
        The :mod:`lihzahrd.terraria.world` module.
    """

    PLAYER = 3
    """
    A player character save file.
    
    .. note::
    
        Player character save files are usually encrypted with a static key, and must be unencrypted before they can be processed with :class:`~lihzahrd.terraria.common.file_metadata.FileMetadata`.
    
    """


class PackFileKind(PackEnum, PackByte):
    """
    :class:`~lihzahrd.terraria.utils.pack.pack.Pack` for :class:`.FileKind` as represented in the save file metadata header.
    """

    _LOG = getLogger(__name__)

    ENUM = FileKind


__all__ = (
    "FileKind",
    "PackFileKind",
)
