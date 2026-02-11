<div align="center">

![](.media/icon-128x128_round.png)

# Lihzahrd

Terraria game world parser for Python

</div>

## Links

[![Available on PyPI](https://img.shields.io/pypi/v/lihzahrd)](https://pypi.org/project/lihzahrd/)

[![Full documentation](https://img.shields.io/website?url=https%3A%2F%2Fgh.steffo.eu%2Flihzahrd%2Fhtml%2F&up_message=passing&down_message=failing&label=docs)](https://gh.steffo.eu/lihzahrd/html/)

## Installation

Lihzahrd can be installed from PyPI like any other public Python package.

Using [uv](https://docs.astral.sh/uv/), that means:

```shell
uv add lihzahrd
```

## Usage

You can open a world file and get a `World` object by calling:

```python
import lihzahrd
world = lihzahrd.World.create_from_file("filename.wld")
```

It _will_ take a while to process: a small Terraria world contains more than 5 million tiles!

Once you have a `World` object, you can use all data present in the save file by accessing [its attributes](http://gh.steffo.eu/lihzahrd/html/world.html).

### Fast loading with caching

Since parsing large world files can take significant time, lihzahrd supports caching parsed worlds for much faster subsequent loads:

```python
import lihzahrd
from pathlib import Path

world_path = Path("MyWorld.wld")
cache_path = world_path.with_suffix(".lzd")  # .lzd = lihzahrd cache

# Check if cache exists
if cache_path.exists():
    world = lihzahrd.World.load_from_cache(str(cache_path))  # Fast!
else:
    world = lihzahrd.World.create_from_file(str(world_path))  # Slow
    world.save_to_cache(str(cache_path))  # Save for next time
```

**Performance:** Loading from cache is typically **5-20x faster** than parsing the original .wld file!

The cache uses pickle serialization (no external dependencies) with optional gzip compression. You can trade file size for even faster loading:

```python
# Compressed (default): smaller files, moderate speed
world.save_to_cache("MyWorld.lzd")

# Uncompressed: larger files, maximum speed
world.save_to_cache("MyWorld.lzd", compress=False)
```

> [!Note]
>
> Cache files are tied to the lihzahrd version that created them. If you upgrade lihzahrd, regenerate your cache files.

> [!Warning]
> 
> Maliciously designed Terraria worlds can drain system resources, crash the interpreter, or possibly do other evil things!
> 
> **Make sure you trust worlds before parsing them!**

## Documentation

The documentation is available [here](https://gh.steffo.eu/lihzahrd/html/).

If you know something that is missing in the documentation, please let me know [with an issue](https://github.com/Steffo99/lihzahrd/issues/new)!

## PyPy

`lihzahrd` is compatible with [PyPy](https://www.pypy.org), an alternative implementation on Python!

If you think that parsing a world takes too much time, you can use PyPy to reduce the required time by a factor of ~3!

### Benchmarks

Time to parse the same large world:

- CPython took 11.45 s.
- Pypy took 3.57 s!

### Building docs

You can build the docs by entering the `docs_source` folder and running `make html`, then committing the whole `docs` folder.

## References used

- The [TEdit World Parser](https://github.com/TEdit/Terraria-Map-Editor/blob/master/TEditXna/Terraria/World.FileV2.cs), the most accurate source currently available.
- The [tModLoader wiki](https://github.com/tModLoader/tModLoader/wiki), containing lists of all possible IDs.
- The [Terrafirma world documentation](http://seancode.com/terrafirma/world.html), accurate for old worlds (version <69)
- The [1.3.x.x world documentation](http://ludwig.schafer.free.fr/), a bit incomplete, but an useful source nevertheless.
- A [JS World Parser](https://github.com/cokolele/terraria-world-parser/) on GitHub.
- A [Background Guide](https://steamcommunity.com/sharedfiles/filedetails/?id=841032800) on Steam that displays all possible world backgrounds.

## See also

- [flyingsnake](https://github.com/Steffo99/flyingsnake), a map renderer using this package
