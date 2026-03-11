# language=rst
"""
Submodule for :class:`.PackFlagArray`.
"""

from abc import ABCMeta
from collections.abc import Iterator
from logging import getLogger
from typing import override, Any, Self

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.pack import Pack, PackRead, PackWrite


class PackFlagArray[Item: Pack](Pack, metaclass=ABCMeta):
    """
    A :class:`~lihzahrd.terraria.utils.pack.pack.Pack` representing an **ordered** and **variable-length** set of **homogeneous** :class:`~lihzahrd.terraria.utils.pack.pack.Pack` items.

    The serialization it expects is:

    #. Boolean :obj:`True` ("there is an item afterward")
    #. Item #1
    #. Boolean :obj:`True` ("there is an item afterward")
    #. Item #2
    #. Boolean :obj:`False` ("items have ended")

    Automatically implements :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.read`, :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.write`, and :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.validate` with logging, validation, and structured results.
    """

    _LOG = getLogger(__name__)
    "The :class:`logging.Logger` to use to emit messages about the packing process."

    @override
    def __init__(self, items: list[Item]) -> None:
        super().__init__()
        self.items: list[Item] = items

    @override
    def __repr__(self):
        count = len(self.items)
        return f"<{self.__class__.__qualname__}: {count} items>"

    def __iter__(self) -> Iterator[Item]:
        """
        :return: An iterator of the items in the collection.
        """
        return iter(self.items)

    def __len__(self) -> int:
        """
        :return: The number of items in the collection.
        """
        return len(self.items)

    ITEM: type[Pack]
    """
    The :class:`type` of items to read or write.
    """

    @override
    def validate(self, *, strict: bool = True, **kwargs: Any) -> bool:
        self._LOG.debug("Validating with %r: %r", kwargs, self.items)
        self._LOG.debug("Nothing to validate.")
        return True

    @classmethod
    @override
    def read(cls, fp: FileProcessor, *, strict: bool = True, **kwargs: Any) -> PackRead[Self]:
        cls._LOG.debug("Reading with %r...", kwargs)

        valid = True

        index = 1
        instances = []
        while fp.read_bool():
            cls._LOG.debug(f"Reading instance %r...", index)

            result = cls.ITEM.read(fp, strict=strict, **kwargs)
            valid &= result.valid
            cls._LOG.info(f"Read instance %r: %s", index, result)

            instances.append(result.instance)

        cls._LOG.debug("Creating collection with all read items...")
        instance = cls(items=instances)

        instance.validate(strict=strict, **kwargs)

        return PackRead(
            instance=instance,
            valid=valid,
        )

    @override
    def write(self, fp: FileProcessor, *, strict: bool = True, **kwargs: Any) -> PackWrite[Self]:
        valid = self.validate(strict=strict, **kwargs)

        self._LOG.debug("Writing with %r: %r", kwargs, self.items)

        instance_count = len(self.items)

        for index, container in enumerate(self.items, start=1):
            self._LOG.debug(f"Writing instance %r / %r...", index, instance_count)

            fp.write_bool(True)
            result = container.write(fp, strict=strict, **kwargs)
            valid &= result.valid
            self._LOG.info(f"Written instance %r / %r: %s", index, instance_count, result)

        self._LOG.debug("Writing final False...")
        fp.write_bool(False)

        return PackWrite(
            valid=valid,
        )


__all__ = ("PackFlagArray",)
