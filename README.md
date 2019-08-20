# ![](https://gamepedia.cursecdn.com/terraria_gamepedia/e/ee/Lihzahrd.png?version=b8e7ea78b2f9f27a46e2e70d5684b344) `lihzahrd` [![](https://img.shields.io/pypi/v/lihzahrd)](https://pypi.org/project/lihzahrd/)

A Terraria 1.3.5.3 world parser in Python.

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

## Documentation

The documentation is available [here](https://gh.steffo.eu/lihzahrd/html/).

It's a bit messy and incomplete, as I still have not figured out the meaning of some data, and the code is in need of some refactoring.

If you know something that isn't present in the documentation, please let me know [with an issue](https://github.com/Steffo99/lihzahrd/issues/new)!

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
