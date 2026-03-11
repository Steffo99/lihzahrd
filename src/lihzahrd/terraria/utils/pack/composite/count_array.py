# language=rst
"""
Submodule for :class:`.PackCountArray`.
"""

from abc import ABCMeta, abstractmethod
from collections.abc import Iterator
from logging import getLogger
from typing import override, Any, Self

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.pack import Pack, PackRead, PackWrite


class PackCountArray[Item: Pack](Pack, metaclass=ABCMeta):
    """
    A :class:`~lihzahrd.terraria.utils.pack.pack.Pack` representing an **ordered** and **variable-length** set of **homogeneous** :class:`Pack` items.

    The serialization it expects is:

    #. Item count
    #. Item #1
    #. Item #2
    #. ...

    Automatically implements :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.read`, :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.write`, and :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.validate` with logging, validation, and structured results, but it requires the inheritor to define the way to read or write *the item count* by implementing :meth:`_read_count` and :meth:`._write_count`.

    On validation, if :attr:`.MAX_COUNT` is not :obj:`None`, it ensures that the collection represented by this object is not larger than :attr:`.MAX_COUNT`, and raises :exc:`LimitExceededError` otherwise.
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

    @classmethod
    @abstractmethod
    def _read_count(cls, fp: FileProcessor) -> int:
        """
        Read the amount of items to subsequently read to the collection.

        :param fp: The :class:`lihzahrd.terraria.utils.file_processor.FileProcessor` to read from.
        :return: The number of items to read to the collection.
        :meta public:
        """

    @classmethod
    @abstractmethod
    def _write_count(cls, fp: FileProcessor, count: int) -> None:
        """
        Write the amount of items to subsequently write to the collection.

        :param fp: The :class:`lihzahrd.terraria.utils.file_processor.FileProcessor` to write to.à
        :param count: The count of items in the collection to write.
        :meta public:
        """

    MAX_COUNT: int | None = None
    """
    The maximum number of items that this collection can contain.

    Usually specified because of hardcoded limits in the Terraria save file format.
    """

    class LimitExceededError(Pack.ValidationError):
        """
        The collection has more items than how many are allowed by :attr:`.MAX_COUNT`.
        """

    def validate(self, *, strict: bool = True, **kwargs: Any) -> bool:
        self._LOG.debug("Validating with %r: %r", kwargs, self.items)

        if self.MAX_COUNT is not None and len(self.items) > self.MAX_COUNT:
            if strict:
                self._LOG.error("Invalid: %r", self.items)
                raise self.LimitExceededError(self)
            else:
                self._LOG.warning("Invalid: %r", self.items)
                valid = False
        else:
            self._LOG.debug("Valid: %r", self.items)
            valid = True

        return valid

    @classmethod
    def read(cls, fp: FileProcessor, *, strict: bool = True, **kwargs: Any) -> PackRead[Self]:
        cls._LOG.debug("Reading with %r...", kwargs)

        instance_count = cls._read_count(fp)
        cls._LOG.debug("Read instance count: %r", instance_count)

        valid = True

        instances = []
        for index in range(1, instance_count + 1):
            cls._LOG.debug(f"Reading instance %r / %r...", index, instance_count)

            result = cls.ITEM.read(fp, strict=strict, **kwargs)
            valid &= result.valid
            cls._LOG.info(f"Read instance %r / %r: %s", index, instance_count, result)

            instances.append(result.instance)

        cls._LOG.debug("Creating collection with all read items...")
        instance = cls(items=instances)

        instance.validate(strict=strict, **kwargs)

        return PackRead(
            instance=instance,
            valid=valid,
        )

    def write(self, fp: FileProcessor, *, strict: bool = True, **kwargs: Any) -> PackWrite[Self]:
        valid = self.validate(strict=strict, **kwargs)

        self._LOG.debug("Writing with %r: %r", kwargs, self.items)

        instance_count = len(self.items)
        self._LOG.debug("Writing instance count: %r", instance_count)
        self._write_count(fp, instance_count)

        for index, container in enumerate(self.items, start=1):
            self._LOG.debug(f"Writing instance %r / %r...", index, instance_count)

            result = container.write(fp, strict=strict, **kwargs)
            valid &= result.valid
            self._LOG.info(f"Written instance %r / %r: %s", index, instance_count, result)

        return PackWrite(
            valid=valid,
        )


__all__ = ("PackCountArray",)
