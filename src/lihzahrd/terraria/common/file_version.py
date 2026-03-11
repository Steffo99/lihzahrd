# language=rst
"""
Submodule for distinguishing between the Terraria game versions with which a save file was written with.

.. seealso::

    :attr:`lihzahrd.terraria.common.file_metadata.FileMetadata.version`

"""

from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackInt
from lihzahrd.terraria.utils.pack.primitive.op.comparison import OpComparison


class FileVersion(IntEnum):
    """
    :class:`~enum.IntEnum` containing all known associations between Terraria version strings and file version numbers.

    .. seealso::

        `Desktop version history <https://terraria.wiki.gg/wiki/Desktop_version_history>`_ on the Terraria wiki.
    """

    def __str__(self) -> str:
        """
        Get the properly-formatted version name.

        .. admonition:: Example

            .. code-block:: python

                >>> str(FileVersion["V.1.4.5.5"])
                "v1.4.5.5"

        :return: The properly-formatted version name, such as ``"v1.4.5.5"``.
        """
        return self.name.replace("V.", "v").replace(".", ".")

    V_1_0_5 = 12
    "`Version 1.0.5 <https://terraria.wiki.gg/wiki/1.0.5>`_."

    V_1_0_6 = 20
    "`Version 1.0.6 <https://terraria.wiki.gg/wiki/1.0.6>`_."

    V_1_0_6_1 = 22
    "`Version 1.0.6.1 <https://terraria.wiki.gg/wiki/1.0.6.1>`_."

    V_1_1_1 = 37
    "`Version 1.1.1 <https://terraria.wiki.gg/wiki/1.1.1>`_."

    V_1_1_2 = 39
    "`Version 1.1.2 <https://terraria.wiki.gg/wiki/1.1.2>`_."

    V_1_2 = 67
    "`Version 1.2 <https://terraria.wiki.gg/wiki/1.2>`_."

    V_1_2_0_3_1 = 71
    "`Version 1.2.0.3.1 <https://terraria.wiki.gg/wiki/1.2.0.3.1>`_."

    V_1_2_1_1 = 72
    "`Version 1.2.1.1 <https://terraria.wiki.gg/wiki/1.2.1.1>`_."

    V_1_2_1_2 = 73
    "`Version 1.2.1.2 <https://terraria.wiki.gg/wiki/1.2.1.2>`_."

    V_1_2_2 = 77
    "`Version 1.2.2 <https://terraria.wiki.gg/wiki/1.2.2>`_."

    V_1_2_3_1 = 94
    "`Version 1.2.3.1 <https://terraria.wiki.gg/wiki/1.2.3.1>`_."

    V_1_2_4 = 101
    "`Version 1.2.4 <https://terraria.wiki.gg/wiki/1.2.4>`_."

    V_1_2_4_1 = 102
    "`Version 1.2.4.1 <https://terraria.wiki.gg/wiki/1.2.4.1>`_."

    # V_1_2_3 = 104
    V_1_3_0_1 = 140
    "`Version 1.3.0.1 <https://terraria.wiki.gg/wiki/1.3.0.1>`_."

    # V_1_3_0_1 = 146
    V_1_3_0_2 = 147
    "`Version 1.3.0.2 <https://terraria.wiki.gg/wiki/1.3.0.2>`_."

    V_1_3_0_3 = 149
    "`Version 1.3.0.3 <https://terraria.wiki.gg/wiki/1.3.0.3>`_."

    V_1_3_0_4 = 151
    "`Version 1.3.0.4 <https://terraria.wiki.gg/wiki/1.3.0.4>`_."

    V_1_3_0_5 = 153
    "`Version 1.3.0.5 <https://terraria.wiki.gg/wiki/1.3.0.5>`_."

    V_1_3_0_6 = 154
    "`Version 1.3.0.6 <https://terraria.wiki.gg/wiki/1.3.0.6>`_."

    V_1_3_0_7 = 155
    "`Version 1.3.0.7 <https://terraria.wiki.gg/wiki/1.3.0.7>`_."

    V_1_3_0_8 = 156
    "`Version 1.3.0.8 <https://terraria.wiki.gg/wiki/1.3.0.8>`_."

    V_1_3_1 = 168
    "`Version 1.3.1 <https://terraria.wiki.gg/wiki/1.3.1>`_."

    V_1_3_1_1 = 169
    "`Version 1.3.1.1 <https://terraria.wiki.gg/wiki/1.3.1.1>`_."

    V_1_3_2 = 170
    "`Version 1.3.2 <https://terraria.wiki.gg/wiki/1.3.2>`_."

    V_1_3_2_1 = 173
    "`Version 1.3.2.1 <https://terraria.wiki.gg/wiki/1.3.2.1>`_."

    V_1_3_3 = 174
    "`Version 1.3.3 <https://terraria.wiki.gg/wiki/1.3.3>`_."

    V_1_3_3_1 = 175
    "`Version 1.3.3.1 <https://terraria.wiki.gg/wiki/1.3.3.1>`_."

    V_1_3_3_2 = 176
    "`Version 1.3.3.2 <https://terraria.wiki.gg/wiki/1.3.3.2>`_."

    V_1_3_3_3 = 177
    "`Version 1.3.3.3 <https://terraria.wiki.gg/wiki/1.3.3.3>`_."

    V_1_3_4 = 178
    "`Version 1.3.4 <https://terraria.wiki.gg/wiki/1.3.4>`_."

    V_1_3_4_1 = 185
    "`Version 1.3.4.1 <https://terraria.wiki.gg/wiki/1.3.4.1>`_."

    V_1_3_4_2 = 186
    "`Version 1.3.4.2 <https://terraria.wiki.gg/wiki/1.3.4.2>`_."

    V_1_3_4_3 = 187
    "`Version 1.3.4.3 <https://terraria.wiki.gg/wiki/1.3.4.3>`_."

    V_1_3_4_4 = 188
    "`Version 1.3.4.4 <https://terraria.wiki.gg/wiki/1.3.4.4>`_."

    V_1_3_5 = 191
    "`Version 1.3.5 <https://terraria.wiki.gg/wiki/1.3.5>`_."

    V_1_3_5_1 = 192
    "`Version 1.3.5.1 <https://terraria.wiki.gg/wiki/1.3.5.1>`_."

    V_1_3_5_2 = 193
    "`Version 1.3.5.2 <https://terraria.wiki.gg/wiki/1.3.5.2>`_."

    V_1_3_5_3 = 194
    "`Version 1.3.5.3 <https://terraria.wiki.gg/wiki/1.3.5.3>`_."

    V_1_4_0_1 = 225
    "`Version 1.4.0.1 <https://terraria.wiki.gg/wiki/1.4.0.1>`_."

    V_1_4_0_2 = 226
    "`Version 1.4.0.2 <https://terraria.wiki.gg/wiki/1.4.0.2>`_."

    V_1_4_0_3 = 227
    "`Version 1.4.0.3 <https://terraria.wiki.gg/wiki/1.4.0.3>`_."

    V_1_4_0_4 = 228
    "`Version 1.4.0.4 <https://terraria.wiki.gg/wiki/1.4.0.4>`_."

    V_1_4_0_5 = 230
    "`Version 1.4.0.5 <https://terraria.wiki.gg/wiki/1.4.0.5>`_."

    V_1_4_2_3 = 238
    "`Version 1.4.2.3 <https://terraria.wiki.gg/wiki/1.4.2.3>`_."

    V_1_4_4_5 = 274
    "`Version 1.4.4.5 <https://terraria.wiki.gg/wiki/1.4.4.5>`_."

    V_1_4_4_8 = 278
    "`Version 1.4.4.8 <https://terraria.wiki.gg/wiki/1.4.4.8>`_."

    V_1_4_4_9 = 279
    "`Version 1.4.4.9 <https://terraria.wiki.gg/wiki/1.4.4.9>`_."

    V_1_4_5_4 = 317
    "`Version 1.4.5.4 <https://terraria.wiki.gg/wiki/1.4.5.4>`_."

    V_1_4_5_5 = 318
    "`Version 1.4.5.5 <https://terraria.wiki.gg/wiki/1.4.5.5>`_."


class PackFileVersion(OpComparison[int], PackEnum[FileVersion, int], PackInt):
    """
    :class:`~lihzahrd.terraria.utils.pack.pack.Pack` for :class:`.FileVersion` as represented in the save file metadata header.
    """

    _LOG = getLogger(__name__)

    ENUM = FileVersion


__all__ = (
    "FileVersion",
    "PackFileVersion",
)
