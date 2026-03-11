# language=rst
"""
Submodule for :class:`.ClassEnumType`.
"""

from abc import ABCMeta, abstractmethod
from logging import getLogger
from typing import Any, override, Self


# noinspection PyMethodParameters
class ClassEnumType(type, metaclass=ABCMeta):
    """
    Abstract metaclass that defines methods in common to all :term:`ClassEnum`.
    """

    @override
    def __new__(
        classenumtype: type[Self],
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        *,
        register: bool = True,
        **kwargs: Any,
    ) -> Self:
        """
        Initialize a new class based on this metaclass, possibly registering it as :term:`ClassMember`.

        Calls :meth:`._register` if ``register`` is ``True``.

        The following positional arguments are automatically passed on class creation, but are documented here for completeness.

        :param name: The name of the class to create.
        :param bases: The classes from which the class will inherit.
        :param namespace: The namespace (dictionary mapping variable names to values) that the class will have once created.

        The following keyword arguments have to be manually provided after the ``metaclass=...`` expression.

        :param register: Whether the new class should be registered as :term:`ClassMember` or not. Useful to define some :term:`ClassMemberBase`.

        .. admonition:: Example

            This would create a new enumeration:

            .. code-block:: python

                class MyEnum(ClassEnumType):
                    ...

            This would register a variant on the created enumeration:

            .. code-block:: python

                class MyVariant(metaclass=MyEnum):
                    ...

            This would create a class from which enumeration variants can inherit from, but which is not registered on the enumeration itself:

            .. code-block:: python

                class MyBaseVariant(metaclass=MyEnum, register=False):
                    ...

        """

        classenum = super().__new__(classenumtype, name, bases, namespace)

        if register:
            classenumtype.register(classenum, **kwargs)

        return classenum

    @classmethod
    @abstractmethod
    def register(classenumtype: type[Self], classenum: Self, **kwargs) -> None:
        """
        Register a new *ClassMember* with the given identifier.

        Called after a *ClassMember* with ``register=True`` is created.

        :param classenum: The *ClassMember* to register.
        :param kwargs: Keyword arguments specified as metaclass keyword parameters, excluding ones captured by :meth:`__init__`, like ``register``.
        """


__all__ = ("ClassEnumType",)
