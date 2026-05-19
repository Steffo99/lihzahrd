################
Install Lihzahrd
################

Lihzahrd is distributed as a Python package `on PyPI`_, and, as a backup, `on Steffo's code forge`_.

.. note::

	Make sure you have `Python 3.14 or later`_ installed on your system before proceeding!

.. _on PyPI: https://pypi.org/project/lihzahrd/
.. _on Steffo's code forge: https://g.starshard.space/steffo/-/packages/pypi/lihzahrd/
.. _Python 3.14 or later: https://www.python.org/downloads/

*******************************
Command-line tools installation
*******************************

If you intend to only use the command-line tools Lihzahrd provides, you can use the following installation methods.

Recommended: pipx
=================

`pipx`_ is the software recommended by the `Python Packaging Authority`_ for installing standalone Python applications, like the Lihzahrd command-line tools are.

If you have `pipx`_ installed, you can install Lihzahrd by running:

.. code-block:: shell-session
	:caption: Terminal

	$ pipx install "lihzahrd[cli]"

You can then run the Lihzahrd command-line tools with:

.. code-block:: shell-session
	:caption: Terminal

	$ lihzahrd

To later upgrade Lihzahrd, you can run:

.. code-block:: shell-session
	:caption: Terminal

	$ pipx upgrade lihzahrd

.. _pipx: https://pipx.pypa.io/latest/
.. _Python Packaging Authority: https://www.pypa.io/en/latest/

Alternative: pip in a venv
==========================

`pip`_ is the software included with Python for adding packages to your Python installation.

Since many operating systems rely on the local Python installation for their internal tools, using it directly there is strongly discourages, as that might break your operating system.

However, it is possible to create a virtual Python installation with the built-in :mod:`venv` module, and install Lihzahrd in isolation there.

To do so, first create a venv somewhere on your system by running:

.. code-block:: shell-session
	:caption: Terminal

	$ python -m venv "lihzahrd_venv"

.. _s-venv_activation:

Then, activate the venv following the instructions for the shell you are currently using:

.. code-block:: shell-session
	:caption: Terminal (Bash)

	$ source lihzahrd_venv/bin/activate

.. code-block:: shell-session
	:caption: Terminal (Fish)

	$ source lihzahrd_venv/bin/activate.fish

.. code-block:: pwsh-session
	:caption: Terminal (Powershell)

	> lihzahrd_venv\Scripts\activate.ps1

And finally, install the Lihzahrd command-line tools by running:

.. code-block:: shell-session
	:caption: Terminal

	(lihzahrd_venv)$ pip install "lihzahrd[cli]"

You can then run the Lihzahrd command-line tools with:

.. code-block:: shell-session
	:caption: Terminal

	(lihzahrd_venv)$ lihzahrd

.. note::

	The command-line tools will only be available while the venv is activated; you'll need to repeat :ref:`the activation process <s-venv_activation>` each time you want to use them.

To later upgrade Lihzahrd, you can run:

.. code-block:: shell-session
	:caption: Terminal

	(lihzahrd_venv)$ pip install --upgrade "lihzahrd[cli]"

.. _pip: https://pypi.org/project/pip/

********************
Library installation
********************

If you intend to develop a Python application based on Lihzahrd, you can add it as a dependency to your project's `pyproject.toml`_ file.

.. code-block:: toml
	:caption: ``pyproject.toml``

	dependencies = [
	    "lihzahrd>=4",
	]

It is not tipically required by a standalone Python application, but if necessary, you can include the command-line tools by adding the ``cli`` extra as a dependency:

.. code-block:: toml
	:caption: ``pyproject.toml``

	dependencies = [
	    "lihzahrd[cli]>=4",
	]

.. _pyproject.toml: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
