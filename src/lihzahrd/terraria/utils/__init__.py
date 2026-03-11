# language=rst
"""
Module for utilities useful for the processing of Terraria save files.

It has three submodules:

#. :mod:`lihzahrd.terraria.utils.structures`, with some basic data structures that appear often in save files;
#. :mod:`lihzahrd.terraria.utils.file_processor`, for low level Terraria save file operations;
#. :mod:`lihzahrd.terraria.utils.pack`, a set of mixins to implement reading and writing classes to :class:`~lihzahrd.terraria.utils.file_processor.FileProcessor`, plus validation capabilities to optionally ensure the values being written are correct.

"""
