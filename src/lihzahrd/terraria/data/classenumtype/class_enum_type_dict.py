# language=rst
"""
Submodule for :class:`.ClassEnumTypeDict`.
"""

from abc import ABCMeta
from collections import defaultdict
from logging import getLogger
from typing import Self, override, Any

from lihzahrd.terraria.data.classenumtype.class_enum_type import ClassEnumType


# noinspection PyMethodParameters
class ClassEnumTypeDict(ClassEnumType, metaclass=ABCMeta):
    """
    A kind of :class:`~lihzahrd.terraria.data.classenumtype.class_enum_type.ClassEnumType` which uses metaclass kwargs to index the created class instances in :class:`dict`, and sets them as attributes on the created class instance.

    Inheritors **MUST** set :attr:`.INDEXES` to a new :class:`collections.defaultdict`, so that they have their own unique indexes.

    .. admonition:: Example

        .. code-block:: python

            >>> class MyEnum(ClassEnumTypeDict):
            ...     INDEXES = defaultdict(dict)
            ...
            >>> class MyClass(ClassEnumTypeDict, ID=123, NAME="My Class"):
            ...     ID: int
            ...     NAME: str
            ...     UNINDEXED_PROPERTY: str = "Hello world!"
            ...
            >>> assert MyClass.ID == 123
            >>> assert MyClass.NAME == "My Class"
            >>> assert MyClass.UNINDEXED_PROPERTY == "Hello world!"
            >>> assert MyEnum.INDEXES["ID"][123] == MyClass
            >>> assert MyEnum.INDEXES["NAME"]["My Class"] == MyClass
            >>> assert "Hello world!" not in MyEnum.INDEXES["UNINDEXED_PROPERTY"]

    """

    INDEXES: defaultdict[str, dict[Any, Self]]
    ":class:`defaultdict` mapping index names to their respective indexes."

    @classmethod
    @override
    def register(classenumtype: type[Self], classenum: Self, **kwargs) -> None:
        for key, value in kwargs.items():
            classenum.INDEXES[key][value] = classenum
            setattr(classenum, key, value)

        super().register(classenum)


__all__ = ("ClassEnumTypeDict",)
