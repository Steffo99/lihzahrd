# language=rst
"""
Submodule for :class:`.PackComposite`.
"""

from abc import abstractmethod, ABCMeta
from logging import getLogger
from typing import Self, override, overload

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.pack import Pack, PackRead, PackWrite


class PackComposite(Pack, metaclass=ABCMeta):
    """
    A :class:`~lihzahrd.terraria.utils.pack.pack.Pack` representing an **ordered** and **fixed-length** set of **heterogenous** :class:`Pack` items.

    Automatically implements :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.read`, :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.write`, and :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.validate` with logging, validation, and structured results, but requires the inheritor to define the fields that instances should contain, and specify the order they should be processed to via :meth:`._fields`.
    """

    @abstractmethod
    @override
    def __init__(self, *args: Pack, **kwargs):
        """
        Create a new instance of the :class:`.PackComposite` by determining the fields it will have with the given kwargs, then by setting the value of each to the arg with the same index.

        For instances to have correct attribute suggestions in IDEs, the :meth:`.__init__` method of each :class:`PackComposite` must be overridden.

        The override should define a new instance-level attribute for each field, annotating it with the type of the field value, and assigning to it the value :obj:`Ellipsis` (which will be ignored by :class:`.Field`).

        .. warning::

            Not setting the value to :obj:`Ellipsis` will result in the type annotation becoming :obj:`~typing.Any` for IDEs!

        .. admonition:: Example

            From :class:`~lihzahrd.terraria.common.file_metadata.FileMetadata`:

            .. code-block:: python

                @override
                def __init__(self, *args: Pack, **kwargs):
                    self.version: PackFileVersion = ...
                    self.signature: PackFileSignature = ...
                    self.kind: PackFileKind = ...
                    self.revision: PackFileRevision = ...
                    self.flags: PackFileFlags = ...

                    super().__init__(*args, **kwargs)

        :param kwargs: The arguments to pass to :meth:`._fields` to determine which fields will exist on the instance.
        :param args: The values to use for each field returned by :meth:`._fields`.
        """

        super().__init__()

        fields = self._fields(**kwargs)

        n_fields = len(fields)
        n_args = len(args)
        if n_fields != n_args:
            raise ValueError(f"Incorrect number of args ({n_args}) for the number of fields ({n_fields}).")

        for field, arg in zip(fields, args):
            field.__set__(self, arg)

    @override
    def __repr__(self):
        return f"<{self.__class__.__qualname__}>"

    class Field[Owner, Value: Pack]:
        """
        A descriptor for one of the :class:`Pack` values making up the composite object.

        Necessary to allow :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.read` to determine the class to call :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.read` on.

        If a field is attempted to be set to :obj:`Ellipsis`, the action is ignored; this is used to make instance-level type hinting prevail over the class-level descriptor access on IDEs.
        """

        def __init__(self, ty: type[Value]) -> None:
            """
            Create a new field.

            You should call this as if defining a class-level variable.

            The name of the field is determined via :meth:`.__set_name__`.

            :param ty: The type of the value to store in it.
            """
            self.name: str | None = None
            self.ty: type[Value] = ty

        def __set_name__(self, owner: type[Owner], name: str) -> None:
            self.name = name

        def container_name(self) -> str:
            """
            :return: The name of the variable to use to store the actual value in.
            """
            assert self.name is not None
            return f"_{self.name}"

        @overload
        def __get__(self, instance: Owner, owner: type[Owner]) -> Value: ...

        @overload
        def __get__(self, instance: None, owner: type[Value]) -> Self: ...

        def __get__(self, instance: Owner | None, owner: type[Owner]) -> Value | Self:
            if instance is None:
                return self
            return getattr(instance, self.container_name())

        def __set__(self, instance: Owner, value: Value) -> None:
            if value is ...:
                return None
            return setattr(instance, self.container_name(), value)

        def __str__(self) -> str:
            return repr(self.name)

        def __repr__(self) -> str:
            field = self.__class__.__qualname__
            name = self.name
            ty = self.ty.__qualname__
            return f"<{field} {name!r} ({ty})>"

    @classmethod
    @abstractmethod
    def _fields(cls, **kwargs) -> list[Field[Self, Pack]]:
        """
        Get a :class:`list` of the fields that should be processed, in the order they should be processed.

        .. warning::

            Getters of the included properties **must** have a correct type annotation!

        :param kwargs: Additional keyword arguments that may be used by implementations to do conditional processing.
        :return: The :func:`property` that should be validated, read, or written, in the order these operations should be done.
        :meta public:
        """

    _LOG = getLogger(__name__)
    """
    The :class:`logging.Logger` to use to emit messages about the packing process.
    
    :meta public:
    """

    @override
    def validate(self, *, strict: bool = True, **kwargs) -> bool:
        valid = True

        for field in self._fields(**kwargs):
            self._LOG.debug("Validating field %s with %r...", field, kwargs)
            # Validate each value obtained by the field's getter, and "and" all of them together
            valid &= field.__get__(self, self.__class__).validate(strict=strict, **kwargs)

        self._LOG.debug("Composite validity: %r", valid)
        return valid

    @classmethod
    @override
    def read(cls, fp: FileProcessor, *, strict: bool = True, **kwargs) -> PackRead[Self]:
        values: list = []
        valid = True

        for field in cls._fields(**kwargs):
            cls._LOG.debug("Reading field %s with %r...", field, kwargs)
            # Read each type
            result = field.ty.read(fp, strict=strict, **kwargs)
            cls._LOG.info("Read field %s: %s", field, result)
            # "and" the validity of all results together
            valid &= result.valid
            # Collect all values in the values array
            values.append(result.instance)

        # Create the instance from the given values
        instance = cls(*values)

        cls._LOG.debug("Composite instance: %r", instance)
        cls._LOG.debug("Composite validity: %r", valid)

        return PackRead(instance=instance, valid=valid)

    @override
    def write(self, fp: FileProcessor, *, strict: bool = True, **kwargs) -> PackWrite[Self]:
        valid = True

        for field in self._fields(**kwargs):
            self._LOG.debug("Writing field %s with %r...", field, kwargs)
            # Use the field's getter to write each value
            result = field.__get__(self, self.__class__).write(fp, strict=strict, **kwargs)
            self._LOG.info("Written field %s: %s", field, result)
            # "and" the validity of all results together
            valid &= result.valid

        self._LOG.debug("Composite validity: %r", valid)

        return PackWrite(valid=valid)


__all__ = ("PackComposite",)
