# language=rst
"""
Submodule for the base :class:`.Pack` abstract class.
"""

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Self, Any

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.error import LihzahrdException


class Pack(metaclass=ABCMeta):
    """
    Block of **adjacent** data in a Terraria save file.

    Instances of classes inheriting from this one always have:

    - :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.read` and :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.write` methods to interact with a :class:`~lihzahrd.terraria.utils.file_processor.FileProcessor`;
    - a :meth:`.validate` method to check that the data currently represented makes sense in the context of a Terraria save file.

    To better support future Terraria updates, or just to allow more tinkering with the save files, inheritors of :class:`.Pack` should try to allow as much leeway as it makes sense to in reading and writing values that do not pass validation.
    """

    @classmethod
    @abstractmethod
    def read(cls, fp: FileProcessor, *, strict: bool = True, **kwargs: Any) -> PackRead[Self]:
        """
        Read a value from the given :class:`~lihzahrd.terraria.utils.file_processor.FileProcessor`, validate it, then use it to create an instance of this class.

        :param fp: The :class:`~lihzahrd.terraria.utils.file_processor.FileProcessor` to read from.
        :param strict: Whether any :exc:`.ValidationError` raised should be raised again, or ignored.
        :param kwargs: Additional keyword arguments that may be used by implementations to do conditional processing.
        :return: A :class:`.PackRead` instance with the created instance and validation information.
        :raises ValidationError: If the read value is invalid and validation is ``strict``.
        :raises ReadError: If the value could not be read.
        """

    class ReadError(LihzahrdException):
        """
        A failure of some kind in :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.read`, preventing the object from being read.
        """

    @abstractmethod
    def write(self, fp: FileProcessor, *, strict: bool = True, **kwargs: Any) -> PackWrite[Self]:
        """
        Validate the value represented by this instance, then write it to the given :class:`~lihzahrd.terraria.utils.file_processor.FileProcessor`.

        :param fp: The :class:`~lihzahrd.terraria.utils.file_processor.FileProcessor` to write to.
        :param strict: Whether any :exc:`.ValidationError` raised should be raised again, or ignored.
        :param kwargs: Additional keyword arguments that may be used by implementations to do conditional processing.
        :return: A :class:`.PackWrite` instance with validation information.
        :raises ValidationError: If the value to write is invalid and validation is ``strict``.
        :raises WriteError: If the value could not be written.
        """

    class WriteError(LihzahrdException):
        """
        A failure of some kind in :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.write`, preventing the object from being written.
        """

    @abstractmethod
    def validate(self, *, strict: bool = True, **kwargs: Any) -> bool:
        """
        Validate the value represented by this instance.

        .. note::

            This method is separate from :meth:`.read` and :meth:`.write`, but can be called by them at their own discretion.

        :param strict: Whether any :exc:`.ValidationError` encountered should be re-raised (:obj:`True`) or ignored (:obj:`False`).
        :param kwargs: Additional keyword arguments that may be used by implementations to do conditional processing.
        :return: :obj:`True` if the value is valid, :obj:`False` if the value is invalid and validation isn't ``strict``.
        :raises ValidationError: If the value is invalid and validation is ``strict``.
        """

    class ValidationError(LihzahrdException):
        """
        A failure in validation of some kind; if this occurs, it means that the data represented by this instance would not be valid in a Terraria save file.

        .. tip::

            You can ignore errors of this type in :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.read`, :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.write`, and :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.validate` by specifying ``strict=False`` as a keyword argument!

        """


@dataclass(eq=False, frozen=True, slots=True)
class PackRead[Pck: Pack]:
    """
    The result of a call to :meth:`.Pack.read`.

    The generic type ``Pck`` is the :class:`.Pack` instance returning this.

    Used to bubble up validity information.

    Attributes on this class are frozen.
    """

    instance: Pck
    "The created :class:`Pack` instance representing the read value."

    valid: bool
    "Whether the read value passed validation."

    def __bool__(self) -> bool:
        """
        :return: Whether the read value is :attr:`.valid`.
        """
        return self.valid

    def __str__(self) -> str:
        """
        :return: The :func:`repr` of the :attr:`.instance`, followed by either ``" (ok)"`` or ``" (invalid)"`` depending on :attr:`.valid`.
        """
        if self.valid:
            return f"{self.instance!r} (ok)"
        else:
            return f"{self.instance!r} (invalid)"

    def __repr__(self) -> str:
        instance = self.instance
        valid = self.valid
        return f"{self.__class__.__qualname__}({instance=}, {valid=})"


@dataclass(eq=False, frozen=True, slots=True)
class PackWrite[Pck: Pack]:
    """
    The result of a call to :meth:`.Pack.write`.

    The generic type ``Pck`` is the :class:`.Pack` instance returning this.

    Used to bubble up validity information.

    Attributes on this class are frozen.
    """

    valid: bool
    "Whether the written value passed validation."

    def __bool__(self) -> bool:
        """
        :return: Whether the written value is :attr:`.valid`.
        """
        return self.valid

    def __str__(self) -> str:
        """
        :return: Either ``"ok"`` or ``"invalid"`` depending on the value of :attr:`.valid`.
        """
        if self.valid:
            return f"ok"
        else:
            return f"invalid"

    def __repr__(self) -> str:
        valid = self.valid
        return f"{self.__class__.__qualname__}({valid=})"


__all__ = (
    "Pack",
    "PackRead",
    "PackWrite",
)
