# language=rst
"""
Submodule containing :class:`.BestiaryDictData`.
"""

from dataclasses import dataclass


@dataclass
class BestiaryDictData:
    """
    Data about a stat tracked in the Bestiary.
    """

    name: str
    "The name of the tracked character."

    count: int
    "The number of times the event has happened."


__all__ = ("BestiaryDictData",)
