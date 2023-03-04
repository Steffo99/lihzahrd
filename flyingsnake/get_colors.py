import typing
from xml.etree import ElementTree
from PIL import ImageColor
import json


def get_block_colors_from_tedit_settings(tree: ElementTree) -> typing.Dict[int, typing.Tuple[int, int, int, int]]:
    root = tree.findall(".//Tile")

    colors = {}

    for block in root:
        id_ = block.attrib["Id"]
        color = block.attrib["Color"] if "Color" in block.attrib else "#00000000"
        alpha, red, green, blue = ImageColor.getrgb(color)
        colors[id_] = red, green, blue, alpha

    return colors


def get_wall_colors_from_tedit_settings(tree: ElementTree) -> typing.Dict[int, typing.Tuple[int, int, int, int]]:
    root = tree.findall(".//Wall")

    colors = {}

    for wall in root:
        id_ = wall.attrib["Id"]
        color = wall.attrib["Color"] if "Color" in wall.attrib else "#00000000"
        alpha, red, green, blue = ImageColor.getrgb(color)
        colors[id_] = red, green, blue, alpha

    return colors


def get_global_colors_from_tedit_settings(tree: ElementTree) -> typing.Dict[str, typing.Tuple[int, int, int, int]]:
    root = tree.findall(".//GlobalColor")

    colors = {}

    for g in root:
        name = g.attrib["Name"]
        color = g.attrib["Color"] if "Color" in g.attrib else "#00000000"
        alpha, red, green, blue = ImageColor.getrgb(color)
        colors[name] = red, green, blue, alpha

    return colors


def get_paint_colors_from_tedit_settings(tree: ElementTree) -> typing.Dict[int, typing.Tuple[int, int, int, int]]:
    root = tree.findall(".//Paint")

    colors = {}

    for color in root:
        id_ = color.attrib["Id"]
        color = color.attrib["Color"] if "Color" in color.attrib else "#00000000"
        alpha, red, green, blue = ImageColor.getrgb(color)
        colors[id_] = red, green, blue, alpha

    return colors


def get_colors_from_tedit_settings(filename: str) -> typing.Dict:
    tree = ElementTree.parse(filename)
    return {
        "Blocks": get_block_colors_from_tedit_settings(tree),
        "Walls": get_wall_colors_from_tedit_settings(tree),
        "Globals": get_global_colors_from_tedit_settings(tree),
        "Paints": get_paint_colors_from_tedit_settings(tree)
    }


if __name__ == "__main__":
    with open("example_colors.json", "w") as file:
        json.dump(get_colors_from_tedit_settings("settings.xml"), file)
