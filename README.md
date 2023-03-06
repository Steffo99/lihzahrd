# ![](https://gamepedia.cursecdn.com/terraria_gamepedia/e/ee/Lihzahrd.png?version=b8e7ea78b2f9f27a46e2e70d5684b344) `lihzahrd` [![](https://img.shields.io/pypi/v/lihzahrd)](https://pypi.org/project/lihzahrd/)

A Terraria 1.4.4.9 world parser in Python.

You can use this package to get programmer-friendly data from a Terraria world!

Install with:
```
pip install lihzahrd
```

## Usage

You can open a world file and get a `World` object by calling:

```
import lihzahrd
world = lihzahrd.World.create_from_file("filename.wld")
```

It _will_ take a while to process: a small Terraria world contains more than 5 million tiles!

Once you have a `World` object, you can use all data present in the save file by accessing [its attributes](http://gh.steffo.eu/lihzahrd/html/world.html).

> **Warning**
> 
> Maliciously designed Terraria worlds can drain system resources, crash the interpreter, or possibly do more evil things!
> 
> **Make sure you trust the worlds you are parsing!**

## Documentation

The documentation is available [here](https://gh.steffo.eu/lihzahrd/html/).

It's a bit messy and incomplete, as I still have not figured out the meaning of some data, and the code is in need of some refactoring.

If you know something that isn't present in the documentation, please let me know [with an issue](https://github.com/Steffo99/lihzahrd/issues/new)!

## PyPy

`lihzahrd` is compatible with [PyPy](https://www.pypy.org), a faster implementation of Python!

If you think that parsing a world takes too much time, you can use PyPy to reduce the required time by a factor of ~3!

### Benchmarks

Time to parse the same large world:

- CPython took 11.45 s.
- Pypy took 3.57 s!

## Development

To contribute to `lihzahrd`, you need to have [Poetry](https://poetry.eustace.io/) installed on your PC.

After you've installed Poetry, clone the git repo with the command:

```
git clone https://github.com/Steffo99/lihzahrd
```

Then enter the new directory:

```
cd lihzahrd
```

And finally install all dependencies and the package:

```
poetry install
```

This will create a new virtualenv for the development of the library; you can activate it by typing:

```
poetry shell
```

Please note that for compatibility with PyPy, the project needs to target Python 3.6.

### Building docs

You can build the docs by entering the `docs_source` folder and running `make html`, then committing the whole `docs` folder.

## References used

- The [TEdit World Parser](https://github.com/TEdit/Terraria-Map-Editor/blob/master/TEditXna/Terraria/World.FileV2.cs), the most accurate source currently available.
- The [tModLoader wiki](https://github.com/tModLoader/tModLoader/wiki), containing lists of all possible IDs.
- The [Terrafirma world documentation](http://seancode.com/terrafirma/world.html), accurate for old worlds (version <69)
- The [1.3.x.x world documentation](http://ludwig.schafer.free.fr/), a bit incomplete, but an useful source nevertheless.
- A [JS World Parser](https://github.com/cokolele/terraria-world-parser/) on GitHub.
- A [Background Guide](https://steamcommunity.com/sharedfiles/filedetails/?id=841032800) on Steam that displays all possible world backgrounds.

## License

`lihzahrd` is licensed under the [AGPL 3.0](/LICENSE.txt).
That means you have to publish under the same license the source code of any program you create that uses `lihzahrd`.

## See also

- [flyingsnake](https://github.com/Steffo99/flyingsnake), a map renderer using this package
