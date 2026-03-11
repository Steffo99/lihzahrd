# language=rst
"""
Submodule collecting all parts of the Terraria save file header in a single class.
"""

from logging import getLogger
from typing import Self, override

from lihzahrd.terraria.common.file_flags import PackFileFlags
from lihzahrd.terraria.common.file_kind import PackFileKind
from lihzahrd.terraria.common.file_revision import PackFileRevision
from lihzahrd.terraria.common.file_signature import PackFileSignature
from lihzahrd.terraria.common.file_version import PackFileVersion
from lihzahrd.terraria.utils.pack.composite.composite import PackComposite as PaCo
from lihzahrd.terraria.utils.pack.pack import Pack


class FileMetadata(PaCo):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.composite.PackComposite` for all parts of the Terraria save file header.
    """

    _LOG = getLogger(__name__)

    version: PaCo.Field[Self, PackFileVersion] = PaCo.Field(PackFileVersion)
    """
    The version with which the save file was written with.
    
    :type: :class:`~lihzahrd.terraria.common.file_version.PackFileVersion`
    """

    signature: PaCo.Field[Self, PackFileSignature] = PaCo.Field(PackFileSignature)
    """
    The signature of the save file.
    
    :type: :class:`~lihzahrd.terraria.common.file_signature.PackFileSignature`
    """

    kind: PaCo.Field[Self, PackFileKind] = PaCo.Field(PackFileKind)
    """
    The kind of the save file.
    
    :type: :class:`~lihzahrd.terraria.common.file_kind.PackFileKind`
    """

    revision: PaCo.Field[Self, PackFileRevision] = PaCo.Field(PackFileRevision)
    """
    The revision of the save file.
    
    The save file revision should increase by ``1`` each time a save file is saved.
    
    :type: :class:`~lihzahrd.terraria.common.file_revision.PackFileRevision`
    """

    flags: PaCo.Field[Self, PackFileFlags] = PaCo.Field(PackFileFlags)
    """
    The flags of the save file.
    
    :type: :class:`~lihzahrd.terraria.common.file_flags.PackFileFlags`
    """

    # noinspection PyTypeChecker
    @override
    def __init__(self, *args: Pack, **kwargs):
        """"""
        self.version: PackFileVersion = ...
        self.signature: PackFileSignature = ...
        self.kind: PackFileKind = ...
        self.revision: PackFileRevision = ...
        self.flags: PackFileFlags = ...

        super().__init__(*args, **kwargs)

    @classmethod
    @override
    def _fields(cls, **kwargs) -> list[PaCo.Field[Self, Pack]]:
        return [
            cls.version,
            cls.signature,
            cls.kind,
            cls.revision,
            cls.flags,
        ]


__all__ = ("FileMetadata",)
