# language=rst
"""
Submodule for distinguishing between Terraria save file kinds.

.. seealso::

    :attr:`lihzahrd.terraria.common.file_metadata.FileMetadata.flags`

"""

from enum import IntFlag
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackFlags
from lihzahrd.terraria.utils.pack.primitive.int import PackULong


class FileFlags(IntFlag):
    """
    :class:`~enum.IntFlag` representing all possible file flags a Terraria world might have.
    """

    FAVORITE = 1
    "If set, the file is marked as favorite."


class PackFileFlags(PackFlags[FileFlags, int], PackULong):
    """

    :class:`~lihzahrd.terraria.utils.pack.pack.Pack` for :class:`.FileFlags` as represented in the save file metadata header.
    """

    _LOG = getLogger(__name__)

    FLAGS = FileFlags


__all__ = (
    "FileFlags",
    "PackFileFlags",
)
