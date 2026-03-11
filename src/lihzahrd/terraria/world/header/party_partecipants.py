from logging import getLogger
from typing import override, Any, Iterable

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.data.classenums.npc_enum import NPCEnum
from lihzahrd.terraria.data.classmembers.npc_base import NPCBase
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class PartyPartecipants(PackPrimitive[list[int]]):
    """
    NPC IDs of NPCs partecipating in the ongoing party.
    """

    _LOG = getLogger(__name__)

    def __repr__(self):
        length = len(self.value)
        return f"<{self.__class__.__qualname__}: {length} NPCs partying>"

    def get_npcs(self) -> list[type[NPCBase]]:
        """
        :return: The :class:`list` of NPC :term:`ClassMember` corresponding to :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value`.
        :raises KeyError: If a NPC is not found.
        """
        return list(map(NPCEnum.INDEXES["ID"].__getitem__, self.value))

    def set_from_npcs(self, value: Iterable[type[NPCBase]]) -> None:
        """
        :param value: The :class:`list` of NPC :term:`ClassMember` to set :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value` to.
        """
        self.value = list(map(lambda npc: npc.ID, value))

    class ListOverflowError(PackPrimitive[list[int]].ValidationError):
        """
        The list contains more items than how many can possibly be represented.
        """

    class UnknownNPCError(PackPrimitive[list[int]].ValidationError):
        """
        At least one value in the list does not correspond to a known NPC ID.
        """

    @classmethod
    @override
    def _validate(cls, value: list[int], **kwargs: Any) -> None:
        length = len(value)
        if not FileProcessor.INT_MIN <= length <= FileProcessor.INT_MAX:
            raise cls.ListOverflowError(value)

        for item in value:
            try:
                _npc = NPCEnum.get_by_id(item)
            except KeyError:
                raise cls.UnknownNPCError(value)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> list[int]:
        length = fp.read_int()
        counts: list[int] = []
        for _ in range(length):
            count = fp.read_int()
            counts.append(count)
        return counts

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: list[int], **kwargs: Any) -> None:
        length = len(value)
        fp.write_int(length)
        for item in value:
            fp.write_int(item)


__all__ = ("PartyPartecipants",)
