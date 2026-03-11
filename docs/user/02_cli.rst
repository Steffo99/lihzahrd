##################
Command-line tools
##################

Lihzahrd includes a suite of command-line tools to perform some common operations on Terraria save files.

To view info about them, run:

.. code-block:: shell-session
	:caption: Terminal

	$ lihzahrd --help

The options displayed there are global, and work with all sub-commands; they should be specified after the ``lihzahrd`` command but before any further subcommands, like so:

.. code-block:: shell-session
	:caption: Terminal

	$ lihzahrd --force-color worlds

***********
World tools
***********

All included command-line tools currently operate on Terraria **world** save files.

To view info about that category of tools, run:

.. code-block:: shell-session
	:caption: Terminal

	$ lihzahrd worlds --help

List worlds
===========

Lihzahrd can list the worlds available in your system.

To do so, run:

.. code-block:: shell-session
	:caption: Terminal

	$ lihzahrd worlds list
	The Blursed Land - Journey - 0% - Medium World
	The Example Land - Expert - 0% - Small World

.. note::

	If you play on Linux, and your data is not appearing, it might be because you are playing via Proton, which uses a different save file location compared to the Linux-native Terraria executable.

	In that case, you can specify the global ``--directory-auto-proton`` option to look for save files in the default Proton Terraria save directory, like so:

	.. code-block:: shell-session
		:caption: Terminal

		$ lihzahrd --directory-auto-proton worlds list
