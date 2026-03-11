# language=rst
"""
Submodule for processing the save file revision number.

.. seealso::

    :attr:`lihzahrd.terraria.common.file_metadata.FileMetadata.revision`

"""

from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.int import PackUInt
from lihzahrd.terraria.utils.pack.primitive.op.integer import OpInteger


class PackFileRevision(OpInteger[int], PackUInt):
    """
    :class:`~lihzahrd.terraria.utils.pack.pack.Pack` for the revision of a Terraria save file.
    """

    _LOG = getLogger(__name__)


__all__ = ("PackFileRevision",)
