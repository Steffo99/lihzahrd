# language=rst
"""
Submodule containing processors for classes in :mod:`enum`.
"""

from abc import ABCMeta
from enum import Enum, Flag
from typing import Any, override, Self

from lihzahrd.terraria.utils.pack.primitive.op.boolean import OpBoolean
from lihzahrd.terraria.utils.pack.primitive.op.equality import OpEquality
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class PackEnum[ValidValue: Enum, InternalValue](OpEquality[InternalValue], PackPrimitive, metaclass=ABCMeta):
    """
    A :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` where all the valid values are known at class definition time, and are represented by the :class:`~enum.Enum` ``ValidValue``, whose value is of the generic type ``InternalValue``.

    On validation, it checks that the represented value is a valid value of :attr:`~.PackEnum.ENUM`, and raises :exc:`.UnknownVariantError` otherwise.
    """

    ENUM: type[ValidValue] = NotImplemented
    "The :class:`type` containing all the known values."

    @classmethod
    def from_variant(cls, variant: ValidValue) -> Self:
        """
        Create an instance of this class from an :class:`~enum.Enum` variant.

        :param variant: The variant to use to create the instance.
        :return: The created instance.
        """
        return cls(variant.value)

    @classmethod
    def from_name(cls, key) -> Self:
        """
        Create an instance of this class from an :class:`~enum.Enum` variant's :attr:`~enum.Enum.name`.

        :param key: The :attr:`~enum.Enum.name` to use to create the instance.
        :return: The created instance.
        """
        # noinspection PyTypeChecker
        variant: ValidValue = cls.ENUM.__getitem__(key)
        return cls.from_variant(variant=variant)

    def variant(self) -> ValidValue:
        """
        Convert this instance to the corresponding :class:`~enum.Enum` variant.

        :return: The created variant.
        :raises ValueError: If the value does not correspond to any enum variant.
        """
        return self.ENUM(self.value)

    def name(self) -> str:
        """
        Convert this instance to the corresponding :class:`~enum.Enum` variant :attr:`~enum.Enum.name`.

        :return: The enum :attr:`~enum.Enum.name`.
        """
        return self.ENUM(self.value).name

    def set_from_variant(self, variant: ValidValue) -> None:
        """
        Set the value of this class instance to the value of the given variant.

        :param variant: The variant to use to set the value.
        """
        self.value = variant.value

    def set_from_name(self, name: str) -> None:
        """
        Set the value of this class instance to the value of the variant with the specified :attr:`~enum.Enum.name`.

        :param name: The :attr:`~enum.Enum.name` to use to set the value.
        """
        self.value = self.ENUM(name).value

    class UnknownVariantError(PackPrimitive[InternalValue].ValidationError):
        """
        The specified value is not among the known values :attr:`~.PackEnum.ENUM` can take.
        """

    @classmethod
    @override
    def _validate(cls, value: InternalValue, **kwargs: Any) -> None:
        super()._validate(value, **kwargs)

        # noinspection PyTypeChecker
        assert cls.ENUM is not NotImplemented

        # noinspection PyTypeChecker
        if value not in cls.ENUM:
            raise cls.UnknownVariantError(value)

    @override
    def __repr__(self):
        try:
            return f"<{self.__class__.__qualname__}: {self.name()}>"
        except ValueError:
            return super().__repr__()


class PackFlags[ValidValue: Flag, InternalValue](OpBoolean[InternalValue], PackPrimitive, metaclass=ABCMeta):
    """
    A :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` where all the valid values are known at class definition time, and are represented by the :class:`~enum.Flag` ``ValidValue``, whose value is of the generic type ``InternalValue``.

    On validation, it checks that the represented value is a valid value of :attr:`~.PackFlags.FLAGS`, and raises :exc:`.UnknownVariantError` otherwise.
    """

    FLAGS: type[ValidValue] = NotImplemented
    "The :class:`type` containing all the known values."

    class UnknownFlagsError(PackPrimitive[InternalValue].ValidationError):
        """
        The specified value is not among the known values :attr:`~.PackFlags.FLAGS` can take.
        """

    @classmethod
    def from_variant(cls, variant: ValidValue) -> Self:
        """
        Create an instance of this class from a :class:`~enum.Flag` variant.

        :param variant: The variant to use to create the instance.
        :return: The created instance.
        """
        return cls(variant.value)

    def variant(self) -> ValidValue:
        """
        Convert this instance to the corresponding :class:`~enum.Flag` variant.

        :return: The created variant.
        :raises ValueError: If the value does not correspond to any enum variant.
        """
        return self.FLAGS(self.value)

    def set_from_variant(self, variant: ValidValue) -> None:
        """
        Set the value of this class instance to the value of the given variant.

        :param variant: The variant to use to set the value.
        """
        self.value = variant.value

    @classmethod
    @override
    def _validate(cls, value: InternalValue, **kwargs: Any) -> None:
        super()._validate(value, **kwargs)

        # noinspection PyTypeChecker
        assert cls.FLAGS is not NotImplemented

        # noinspection PyTypeChecker
        if value not in cls.FLAGS:
            raise cls.UnknownFlagsError(value)

    @override
    def __repr__(self):
        try:
            variant = self.variant()
            return f"<{self.__class__.__name__}: {variant.name}>"
        except ValueError:
            return super().__repr__()


__all__ = (
    "PackEnum",
    "PackFlags",
)
