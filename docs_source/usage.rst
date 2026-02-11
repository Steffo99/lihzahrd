.. currentmodule:: lihzahrd

Usage guide
====================================

Prerequisites
------------------------------------

To use ``lihzahrd``, you need Python 3.6 or higher.

That's it! No other packages are required!

Installing
------------------------------------

You can download (or update) the package with ``pip`` by entering in your terminal: ::

    python3.8 -m pip install --upgrade lihzahrd

Opening a world
------------------------------------

To open a Terraria world file named ``terra.wld`` located in the current working directory, you should import the
:py:mod:`lihzahrd` package and then call the :py:meth:`World.create_from_file` function: ::

    import lihzahrd
    world = lihzahrd.World.create_from_file("terra.wld")

It should take **a few minutes**, depending on the size of the world, and then return a
:py:class:`World` object.

Fast loading with caching
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since parsing world files can be slow (especially for large worlds), lihzahrd supports caching parsed worlds for much faster subsequent loads.

**Basic usage:** ::

    import lihzahrd
    from pathlib import Path
    
    world_path = Path("terra.wld")
    cache_path = world_path.with_suffix(".lzd")  # .lzd = lihzahrd cache
    
    # Load from cache if available, otherwise parse and cache
    if cache_path.exists():
        world = lihzahrd.World.load_from_cache(str(cache_path))
    else:
        world = lihzahrd.World.create_from_file(str(world_path))
        world.save_to_cache(str(cache_path))

**Performance:** Loading from cache is typically **5-20x faster** than parsing the .wld file!

**Compression options:**

You can choose between compressed (smaller files) or uncompressed (faster loading) caches: ::

    # Compressed (default): smaller files, moderate speed
    world.save_to_cache("terra.lzd")
    
    # Uncompressed: larger files, maximum speed  
    world.save_to_cache("terra.lzd", compress=False)

**How it works:**

- Uses pickle serialization with optional gzip compression (no external dependencies)
- Automatically detects compressed vs uncompressed format when loading
- Includes lihzahrd version metadata for compatibility checking

**Advanced usage with automatic invalidation:** ::

    def load_world_smart(wld_path):
        """Load world with cache, regenerating if .wld is newer."""
        cache_path = Path(wld_path).with_suffix('.lzd')
        
        if cache_path.exists():
            wld_time = Path(wld_path).stat().st_mtime
            cache_time = cache_path.stat().st_mtime
            
            if wld_time <= cache_time:
                return lihzahrd.World.load_from_cache(str(cache_path))
        
        # Cache doesn't exist or is outdated
        world = lihzahrd.World.create_from_file(wld_path)
        world.save_to_cache(str(cache_path))
        return world

.. note::

    Cache files are tied to the lihzahrd version that created them.
    If you upgrade lihzahrd, you should regenerate your cache files.

.. warning::

    Never load cache files from untrusted sources!
    Pickle files can execute arbitrary code when loaded.

Accessing the world properties
------------------------------------

Most of the world properties are accessible directly as attributes of the :py:class:`World` object: ::

    print(world.name)
    # "Terra"

    print(world.is_hardmode)
    # False

    print(world.spawn_point)
    # Coordinates(2101, 246)

Some world properties may be grouped in other objects: ::

    print(world.bosses_defeated)
    # <BossesDefeated>

    print(world.bosses_defeated.eye_of_cthulhu)
    # False

You can look at the :py:class:`World` class documentation or use an IDE that supports type annotations
(such as `PyCharm <https://www.jetbrains.com/pycharm/>`_) to find all available attributes.

Accessing the tile data
------------------------------------

All :py:class:`tiles.Tile` are stored in the :py:class:`tiles.TileMatrix` accessible at the :py:attr:`World.tiles`
attribute. ::

    print(world.tiles)
    # <TileMatrix 4200x1200>

You can access them by using the ``tiles`` attribute as a two-dimensional array, where (0, 0) is the top-left block: ::

    print(world.tiles[0, 0])
    # <Tile>

You can also use :py:class:`fileutils.Coordinates` instead of a :py:class:`tuple` to fetch a specific tile: ::

    print(world.tiles[lihzahrd.fileutils.Coordinates(2000, 1000)])
    # <Tile B>

    print(world.tiles[world.spawn_point])
    # <Tile B>

Counting tiles from the bottom-right is possible too: ::

    print(world.tiles[-1, -1])
    # <Tile>

A single :py:class:`tiles.Tile` has five attributes that you can access:

* :py:attr:`tiles.Tile.block`, the foreground :py:class:`tiles.Block`;
* :py:attr:`tiles.Tile.wall`, the background :py:class:`tiles.Wall`;
* :py:attr:`tiles.Tile.liquid`, the :py:class:`tiles.Liquid` present in that tile;
* :py:attr:`tiles.Tile.wiring`, the colored wires and actuators (:py:class:`tiles.Wiring`);
* :py:attr:`tiles.Tile.extra`, additional data about the block present at that tile, such as the contents of a chest.

All of these attributes may be :py:const:`None` if the property isn't applicable for the tile:
for example, :py:attr:`tiles.Tile.block` is :py:const:`None` if there is no block ("air") placed there.

Accessing extra data
------------------------------------

Extra data, such as the content of chests or the text of signs, may be accessed in two different ways:

* Through the :py:attr:`tiles.Tile.extra` attribute: ::

    print(world.tiles[2893, 1074].extra)
    # <Chest '' at 2893, 1074>

* Through the various lists available in the :py:class:`World` class, such as :py:attr:`World.chests`: ::

    print(world.chests[0])
    # <Chest '' at 2893, 1074>

Both ways return the same object, but one may be faster than the other, depending on your use case: ::

    print(world.tiles[2893, 1074].extra is world.chests[0])
    # True

Something else
------------------------------------

All information included in a Terraria savefile is parsed in this package and made available in the :py:class:`World`
object.

If you couldn't find what you needed in this short usage guide, check the API Reference or have a look at the
`source code <https://github.com/Steffo99/lihzahrd/tree/master/lihzahrd>`_ !
