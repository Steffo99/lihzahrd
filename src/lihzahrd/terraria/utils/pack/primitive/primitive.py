# language=rst
"""
Submodule containing the abstract base class of :class:`~lihzahrd.terraria.utils.pack.pack.Pack` primitives.
"""

from abc import ABCMeta, abstractmethod
from logging import getLogger, Logger
from typing import Self, override, Any

from lihzahrd.terraria.utils.pack.pack import Pack, PackRead, PackWrite
from lihzahrd.terraria.utils.file_processor import FileProcessor


class PackPrimitive[Value](Pack, metaclass=ABCMeta):
    """
    A :class:`~lihzahrd.terraria.utils.pack.pack.Pack` representing a single unit of data of generic type ``InternalValue``.

    Automatically implements logging, validation, and structured results in :meth:`~object.__init__`, :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.read`, :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.write`, and :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.validate`, but still requires the inheritor to specify *what* should be performed in each of those methods by implementing :meth:`._read`, :meth:`._write`, and :meth:`_validate`.

    .. tip::

        To alter the value of PackPrimitives, you can either use the methods specific to the inheriting class, like :meth:`~lihzahrd.terraria.utils.pack.primitive.enumeration.PackEnum.set_from_variant`, or directly operate on the :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value` attribute, like this::

            p.value = 67

        Via this approach, you can set the value of the PackPrimitive to anything you want, including invalid values!

    """

    __slots__ = ("value",)

    @override
    def __init__(self, value: Value):
        super().__init__()

        self.value: Value = value
        """
        The raw ``InternalValue`` represented by this instance.
        """

    @override
    def __repr__(self) -> str:
        return f"<{self.__class__.__qualname__}: {self.value}>"

    _LOG: Logger
    """
    The :class:`logging.Logger` to use to emit messages about the packing process.
    
    .. note::
    
        :class:`logging.Logger` is not created as a global variable because in this way, logging can be filtered by section being processed instead of by class doing the processing, which arguably is more useful in debugging.
    
    :meta public:
    """

    @classmethod
    def _validate(cls, value: Value, **kwargs: Any) -> None:
        """
        Validate the given ``InternalValue``, raising :exc:`.ValidationError` if it's invalid.

        :param value: The ``InternalValue`` to validate.
        :param kwargs: Additional keyword arguments that may be used by implementations to do conditional processing.
        :raises ValidationError: If ``value`` is not valid.
        :meta public:
        """

    @classmethod
    @abstractmethod
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> Value:
        """
        Read a ``InternalValue`` from the given :class:`.Packer`.

        .. admonition:: Example

            The usual implementation of this method will have a body like:

            .. code-block:: python

                def _read(cls, fp: FileProcessor, **kwargs: Any) -> int:
                    return fp.read_int()

        :param fp: The :class:`.FilePacker` to read from.
        :param kwargs: Additional keyword arguments that may be used by implementations to do conditional processing.
        :returns: The read ``InternalValue``.
        :raises ReadError: If the value could not be read.
        :meta public:
        """

    @classmethod
    @abstractmethod
    def _write(cls, fp: FileProcessor, value: Value, **kwargs: Any) -> None:
        """
        Write the given ``InternalValue`` to the given :class:`.Packer`.

        .. admonition:: Example

            The usual implementation of this method will have a body like:

            .. code-block:: python

                def _write(cls, fp: FileProcessor, value: int, **kwargs: Any) -> None:
                    fp.write_int(value)

        :param fp: The :class:`.FilePacker` to write to.
        :param value: The ``InternalValue`` to write.
        :param kwargs: Additional keyword arguments that may be used by implementations to do conditional processing.
        :raises WriteError: If the value could not be written.
        :meta public:
        """

    class ValidationError(Pack.ValidationError):
        """
        A :exc:`~lihzahrd.terraria.utils.pack.pack.Pack.ValidationError` in which ``InternalValue`` can be stored.

        :meth:`._validate` is expected to raise this kind of error if the value represented by this class is invalid.
        """

        __slots__ = ("value",)

        def __init__(self, value: Value):
            self.value: Value = value
            "The value which failed validation."

    @classmethod
    @override
    def read(cls, fp: FileProcessor, *, strict: bool = True, **kwargs: Any) -> PackRead[Self]:
        cls._LOG.debug("Reading with %r...", kwargs)
        value = cls._read(fp, **kwargs)
        instance = cls(value)
        cls._LOG.debug("Read: %r", instance)

        valid = instance.validate(strict=strict, **kwargs)

        return PackRead(instance=instance, valid=valid)

    @override
    def write(self, fp: FileProcessor, *, strict: bool = True, **kwargs: Any) -> PackWrite[Self]:
        valid = self.validate(strict=strict, **kwargs)

        self._LOG.debug("Writing with %r: %r", kwargs, self.value)
        self._write(fp, self.value, **kwargs)
        self._LOG.debug("Written: %r", self.value)

        return PackWrite(valid=valid)

    @override
    def validate(self, *, strict: bool = True, **kwargs: Any) -> bool:
        self._LOG.debug("Validating with %r: %r", kwargs, self.value)
        try:
            self._validate(self.value, **kwargs)
        except self.ValidationError:
            if strict:
                self._LOG.error("Invalid: %r", self.value)
                raise
            else:
                self._LOG.warning("Invalid: %r", self.value)
            valid = False
        else:
            self._LOG.debug("Valid: %r", self.value)
            valid = True

        return valid


__all__ = ("PackPrimitive",)
