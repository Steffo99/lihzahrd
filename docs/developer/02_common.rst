#################
Common operations
#################

This page lists some common operations you'll find yourself doing while using :mod:`lihzahrd`.

.. tip::

    What else would you like to see here? Don't be afraid to ask, it helps us build a better package!


********************
Loading a world file
********************

To load an existing Terraria world save file, first you'll need to :func:`open` a binary file object:

.. code-block:: python
    :linenos:
    :emphasize-lines: 1

    with open("World.wld", "rb") as file:
        pass

Then, you'll need to load the file object in a :class:`~lihzahrd.terraria.utils.file_processor.FileProcessor`:

.. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4

    from lihzahrd.terraria.utils.file_processor import FileProcessor

    with open("World.wld", "rb") as file:
        fp = FileProcessor(file)

Then, with the file object still open, call the :func:`~lihzahrd.terraria.utils.pack.pack.Pack.read` class method of :class:`~lihzahrd.terraria.world.world.PackWorld` to get a :class:`~lihzahrd.terraria.utils.pack.pack.PackRead` containing the results of the read:

.. code-block:: python
    :linenos:
    :emphasize-lines: 2, 6

    from lihzahrd.terraria.utils.file_processor import FileProcessor
    from lihzahrd.terraria.world.world import PackWorld

    with open("World.wld", "rb") as file:
        fp = FileProcessor(file)
        result = PackWorld.read(fp, strict=False)  # Note: can be very slow!

You can now close the file; if the read completed without any issues, your results will be :attr:`~lihzahrd.terraria.utils.pack.pack.PackRead.valid`, but even if an issue occurred, you'll still be able to access the read data at :attr:`~lihzahrd.terraria.utils.pack.pack.PackRead.instance`:

.. code-block:: python
    :linenos:
    :emphasize-lines: 8, 9, 11

    from lihzahrd.terraria.utils.file_processor import FileProcessor
    from lihzahrd.terraria.world.world import PackWorld

    with open("World.wld", "rb") as file:
        fp = FileProcessor(file)
        result = PackWorld.read(fp, strict=False)

    if not result.valid:
        exit(1)

    world = result.instance


******************************
Accessing a world's properties
******************************

Properties are contained inside :class:`~lihzahrd.terraria.world.world.PackWorld` objects, and are grouped by the section of the save file they appear in.

Most data about a world appears in the :attr:`~lihzahrd.terraria.world.world.PackWorld.header`, and all of the properties appearing there can have their values accessed directly as a Python object via their :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value` attribute:

.. code-block:: python
    :linenos:
    :emphasize-lines: 13, 14

    from lihzahrd.terraria.utils.file_processor import FileProcessor
    from lihzahrd.terraria.world.world import PackWorld

    with open("World.wld", "rb") as file:
        fp = FileProcessor(file)
        result = PackWorld.read(fp, strict=False)

    if not result.valid:
        exit(1)

    world = result.instance

    world_name: str = world.header.name.value
    print(f"Welcome to {world_name}!")

Values can also be set to change them:

.. code-block:: python
    :linenos:
    :emphasize-lines: 16, 17

    from lihzahrd.terraria.utils.file_processor import FileProcessor
    from lihzahrd.terraria.world.world import PackWorld

    with open("World.wld", "rb") as file:
        fp = FileProcessor(file)
        result = PackWorld.read(fp, strict=False)

    if not result.valid:
        exit(1)

    world = result.instance

    world_name: str = world.header.name.value
    print(f"Welcome to {world_name}!")

    world.header.name.value = f"{world_name} but for the Worthy"
    world.header.special_fortheworthy.value = True

Some properties may offer utility methods which might be clearer or safer to use than directly accessing :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value`; those are usually called ``is_*``, ``set_to_*``, ``get_*``, or ``set_from_*``:

.. code-block:: python
    :linenos:
    :emphasize-lines: 3, 4, 16, 19, 21, 25, 27, 28

    from lihzahrd.terraria.utils.file_processor import FileProcessor
    from lihzahrd.terraria.world.world import PackWorld
    from lihzahrd.terraria.data.classmembers.block_base import BlockBase
    from lihzahrd.terraria.data.classmembers.blocks import PalladiumOre

    with open("World.wld", "rb") as file:
        fp = FileProcessor(file)
        result = PackWorld.read(fp, strict=False)

    if not result.valid:
        exit(1)

    world = result.instance

    world_name: str = world.header.name.value
    world_ore_1: type[BlockBase] = world.header.ore_copper_tier.get_block()

    print(f"Welcome to {world_name}, land of {world_ore_1.NAME}!")
    if world.header.difficulty.is_master():
        print("You are already a legendary hero!")
    if world.header.mode.is_hardmode():
        print("Your foes are already worthy of the challenge!")

    world.header.name.value = f"{world_name} but for Legendary Heroes"
    world.header.difficulty.set_master()
    world.header.special_fortheworthy.value = True
    world.header.mode.set_to_hardmode()
    world.header.ore_cobalt_tier.set_from_block(PalladiumOre)


*******************
Saving a world file
*******************

Once you've completed your edits, you can save back the world to a file.

Again, you'll need to :func:`open` a binary file object, but this time in write mode, and make a :class:`~lihzahrd.terraria.utils.file_processor.FileProcessor` like before:

.. code-block:: python
    :linenos:
    :emphasize-lines: 30, 31

    from lihzahrd.terraria.utils.file_processor import FileProcessor
    from lihzahrd.terraria.world.world import PackWorld
    from lihzahrd.terraria.data.classmembers.block_base import BlockBase
    from lihzahrd.terraria.data.classmembers.blocks import PalladiumOre

    with open("World.wld", "rb") as file:
        fp = FileProcessor(file)
        result = PackWorld.read(fp, strict=False)

    if not result.valid:
        exit(1)

    world = result.instance

    world_name: str = world.header.name.value
    world_ore_1: type[BlockBase] = world.header.ore_copper_tier.get_block()

    print(f"Welcome to {world_name}, land of {world_ore_1.NAME}!")
    if world.header.difficulty.is_master():
        print("You are already a legendary hero!")
    if world.header.mode.is_hardmode():
        print("Your foes are already worthy of the challenge!")

    world.header.name.value = f"{world_name} but for Legendary Heroes"
    world.header.difficulty.set_master()
    world.header.special_fortheworthy.value = True
    world.header.mode.set_to_hardmode()
    world.header.ore_cobalt_tier.set_from_block(PalladiumOre)

    with open("WorldLegendary.wld", "wb") as file:
        fp = FileProcessor(file)

Then, you can :func:`~lihzahrd.terraria.utils.pack.pack.Pack.write` the :class:`~lihzahrd.terraria.world.world.PackWorld` instance to it, getting a :class:`~lihzahrd.terraria.utils.pack.pack.PackWrite` result object, through which you can check if the written world is :attr:`~lihzahrd.terraria.utils.pack.pack.PackWrite.valid`:

.. code-block:: python
    :linenos:
    :emphasize-lines: 32, 34, 35

    from lihzahrd.terraria.utils.file_processor import FileProcessor
    from lihzahrd.terraria.world.world import PackWorld
    from lihzahrd.terraria.data.classmembers.block_base import BlockBase
    from lihzahrd.terraria.data.classmembers.blocks import PalladiumOre

    with open("World.wld", "rb") as file:
        fp = FileProcessor(file)
        result = PackWorld.read(fp, strict=False)

    if not result.valid:
        exit(1)

    world = result.instance

    world_name: str = world.header.name.value
    world_ore_1: type[BlockBase] = world.header.ore_copper_tier.get_block()

    print(f"Welcome to {world_name}, land of {world_ore_1.NAME}!")
    if world.header.difficulty.is_master():
        print("You are already a legendary hero!")
    if world.header.mode.is_hardmode():
        print("Your foes are already worthy of the challenge!")

    world.header.name.value = f"{world_name} but for Legendary Heroes"
    world.header.difficulty.set_master()
    world.header.special_fortheworthy.value = True
    world.header.mode.set_to_hardmode()
    world.header.ore_cobalt_tier.set_from_block(PalladiumOre)

    with open("WorldLegendary.wld", "wb") as file:
        fp = FileProcessor(file)
        result = world.write(fp, strict=False)

    if not result.valid:
        exit(2)


*************
Editing tiles
*************

Tiles are represented internally as a :mod:`numpy` matrix, which you can edit `in the same ways you'd edit such an object <https://numpy.org/doc/stable/user/basics.html>`_, except that you can assign :class:`~lihzahrd.terraria.world.tiles.tile.Tile` objects to their values:

.. code-block::
    :linenos:
    :emphasize-lines: 1, 2, 7, 10, 13

    from lihzahrd.terraria.data.classmembers.blocks import Grass, Dirt
    from lihzahrd.terraria.data.classmembers.walls import DirtWall

    ...

    # Turn all tiles in the world into air
    world.tiles[:, :] = Tile()

    # Create a line of grass blocks at world height 300
    world.tiles[:, 300:301] = Tile(block=Grass())

    # Fill everything below height 300 with dirt blocks and dirt walls
    world.tiles[:, 301:] = Tile(block=Dirt(), wall=DirtWall())

Alternatively, you can manually access the properties as you would for a `structured array <https://numpy.org/doc/stable/user/basics.rec.html>`_, but you'll need to manually set their values as described by :obj:`~lihzahrd.terraria.world.tiles.array_dtype.TILE_DTYPE`:

.. code-block::
    :linenos:
    :emphasize-lines: 4, 7, 10

    ...

    # In the left half of the world, draw a red wire column every 10 tiles
    world.tiles["wire_red"][0:2100:10, :] = True

    # In the right half of the world, draw a blue wire column every 10 tiles
    world.tiles["wire_blue"][2101:4200:10, :] = True

    # Remove one block every 3x3 square
    world.tiles["block_id"][::3, ::3] = 0
