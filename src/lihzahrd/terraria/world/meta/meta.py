from typing import Self

from .favorite import Favorite
from .frameimportantarray import FrameImportantArray
from .pointers import Pointers
from .revision import Revision
from .savefiletype import SaveFileType
from .signature import Signature
from ..version import Version
from ...utils import Packable, FilePacker


class Meta(Packable):
    """
    Metadata about a save file, written even before the world information.
    """

    __slots__ = ("version", "signature", "type", "revision", "favorite", "pointers", "frameimportantarray", "unknown")

    def __init__(
            self,
            version_: Version,
            signature_: Signature,
            type_: SaveFileType,
            revision_: Revision,
            favorite_: Favorite,
            pointers_: Pointers,
            frameimportantarray_: FrameImportantArray,
            unknown_: bytearray = bytearray(),
    ):
        self.version: Version = version_
        """The game version when this savefile was last saved."""

        self.signature: Signature = signature_
        """The signature with which the world was saved."""

        self.type: SaveFileType = type_
        """The type of the save file."""

        self.revision: Revision = revision_
        """The number of times this world was saved."""

        self.favorite: Favorite = favorite_
        """
        If the world is marked as favorite or not. 
        
        In-game, Favorite worlds cannot be deleted.
        """

        self.pointers: Pointers = pointers_
        """Pointers to the positions of the other sections of the save file."""

        self.frameimportantarray: FrameImportantArray = frameimportantarray_
        """Something related to the FrameImportant-ness of tiles. Not sure what."""

        self.unknown: bytearray = unknown_
        """Extra, unknown bytes in the meta section of the savefile."""

    def serialize(self, f: FilePacker) -> None:
        self.version.serialize(f)
        self.signature.serialize(f, v=self.version)
        self.type.serialize(f, v=self.version)
        self.revision.serialize(f, v=self.version)
        self.favorite.serialize(f, v=self.version)
        self.pointers.serialize(f, v=self.version)
        self.frameimportantarray.serialize(f, v=self.version)
        f.write_bytearray(self.unknown)

    @classmethod
    def deserialize(cls, f: FilePacker) -> Self:
        version_ = Version.deserialize(f)
        signature_ = Signature.deserialize(f, v=version_)
        type_ = SaveFileType.deserialize(f, v=version_)
        revision_ = Revision.deserialize(f, v=version_)
        favorite_ = Favorite.deserialize(f, v=version_)
        pointers_ = Pointers.deserialize(f, v=version_)
        frameimportantarray_ = FrameImportantArray.deserialize(f, v=version_)
        unknown_ = f.read_bytearray(pointers_.header)

        return cls(
            version_=version_,
            signature_=signature_,
            type_=type_,
            revision_=revision_,
            favorite_=favorite_,
            pointers_=pointers_,
            frameimportantarray_=frameimportantarray_,
            unknown_=unknown_,
        )


__all__ = (
    "Meta",
)