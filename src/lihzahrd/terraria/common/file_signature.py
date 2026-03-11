# language=rst
"""
Submodule for distinguishing between the possible file signature that a Terraria save file may have.

.. seealso::

    :attr:`lihzahrd.terraria.common.file_metadata.FileMetadata.signature`

"""

from enum import StrEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.str import PackStrFixed


class FileSignature(StrEnum):
    """
    :class:`~enum.StrEnum` containing all known Terraria save file signatures.
    """

    RELOGIC = "relogic"
    "Signature of international Terraria save files."

    XINDONG = "xindong"
    "Signature of some Chinese Terraria save files."


class PackFileSignature(PackEnum[FileSignature, str], PackStrFixed):
    """
    :class:`~lihzahrd.terraria.utils.pack.pack.Pack` for :class:`.FileSignature` as represented in the save file metadata header.

    Validates that the contained signature is exactly 7-characters long.
    """

    _LOG = getLogger(__name__)

    ENUM = FileSignature
    DATA_LEN = 7


__all__ = (
    "FileSignature",
    "PackFileSignature",
)
