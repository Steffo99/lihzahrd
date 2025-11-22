from typing import Self

from ...utils import Packable, FilePacker
from ..version import Version
from .signature import Signature
from .savefiletype import SaveFileType
from .revision import Revision
from .favorite import Favorite


class Meta(Packable):
    """
    Metadata about a save file, written even before the world information.
    """

    def __init__(
            self,
            version_: Version,
            signature_: Signature,
            type_: SaveFileType,
            revision_: Revision,
            favorite_: Favorite,
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

    def serialize(self, f: FilePacker) -> None:
        self.version.serialize(f)
        self.signature.serialize(f, v=self.version)
        self.type.serialize(f, v=self.version)
        self.revision.serialize(f, v=self.version)
        self.favorite.serialize(f, v=self.version)

    @classmethod
    def deserialize(cls, f: FilePacker) -> Self:
        version_ = Version.deserialize(f)
        signature_ = Signature.deserialize(f, v=version_)
        type_ = SaveFileType.deserialize(f, v=version_)
        revision_ = Revision.deserialize(f, v=version_)
        favorite_ = Favorite.deserialize(f, v=version_)

        return cls(
            version_=version_,
            signature_=signature_,
            type_=type_,
            revision_=revision_,
            favorite_=favorite_,
        )


__all__ = (
    "Meta",
)