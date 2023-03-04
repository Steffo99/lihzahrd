import click as c
import lihzahrd as li
import lihzahrd.enums as le
import json
import typing
from PIL import Image, ImageDraw
from .default_colors import DEFAULT_COLORS


@c.command()
@c.argument("input_file", type=c.Path(exists=True))
@c.argument("output_file", type=c.Path(exists=False))
@c.option("-c", "--colors", "colors_file", help="The json file to get the tile colors from.", type=c.Path(exists=True))
@c.option(
    "--background/--no-background",
    "draw_background",
    help="Draw the sky/underground/cavern wall beneath the tiles.",
    default=None,
)
@c.option("--blocks/--no-blocks", "draw_blocks", help="Draw the blocks present in the world.", default=None)
@c.option("--walls/--no-walls", "draw_walls", help="Draw the walls present in the world.", default=None)
@c.option("--liquids/--no-liquids", "draw_liquids", help="Draw the liquids present in the world.", default=None)
@c.option("--wires/--no-wires", "draw_wires", help="Draw the liquids present in the world.", default=None)
@c.option(
    "--paint/--no-paint",
    "draw_paint",
    help="Draw painted blocks with the paint color overlayed on them.",
    default=True,
)
@c.option("-x", "--x_coord", "min_x", type=int, help="Min x coord for custom world rendering", default=None)
@c.option("-y", "--y_coord", "min_y", type=int, help="Min y coord for custom world rendering", default=None)
@c.option(
    "-w",
    "--region_width",
    "region_width",
    type=int,
    help="Width of region for custom world rendering",
    default=None,
)
@c.option(
    "-h",
    "--region_height",
    "region_height",
    type=int,
    help="Height of region for custom world rendering",
    default=None,
)
class flyingsnake2:
    def __init__(
        self,
        input_file: str,
        output_file: str,
        colors_file: str,
        draw_background: bool,
        draw_blocks: bool,
        draw_walls: bool,
        draw_liquids: bool,
        draw_wires: bool,
        draw_paint: bool,
        min_x: int,
        min_y: int,
        region_width: int,
        region_height: int,
    ):
        # If at least a draw flag is set to True, default everything else to False
        if (
            draw_background is True
            or draw_blocks is True
            or draw_walls is True
            or draw_liquids is True
            or draw_wires is True
        ):
            draw_background = False if (draw_background is None or draw_background is False) else True
            draw_blocks = False if (draw_blocks is None or draw_blocks is False) else True
            draw_walls = False if (draw_walls is None or draw_walls is False) else True
            draw_liquids = False if (draw_liquids is None or draw_liquids is False) else True
            draw_wires = False if (draw_wires is None or draw_wires is False) else True

        # If at least a draw flag is set to False, default everything else to True
        if (
            draw_background is False
            or draw_blocks is False
            or draw_walls is False
            or draw_liquids is False
            or draw_wires is False
        ):
            draw_background = True if (draw_background is None or draw_background is True) else False
            draw_blocks = True if (draw_blocks is None or draw_blocks is True) else False
            draw_walls = True if (draw_walls is None or draw_walls is True) else False
            draw_liquids = True if (draw_liquids is None or draw_liquids is True) else False
            draw_wires = True if (draw_wires is None or draw_wires is True) else False

        # If no flags are set, draw everything
        if (
            draw_background is None
            and draw_blocks is None
            and draw_walls is None
            and draw_liquids is None
            and draw_wires is None
        ):
            draw_background = True
            draw_blocks = True
            draw_walls = True
            draw_liquids = True
            draw_wires = True

        # If all layers are disabled, raise an Error
        if (
            draw_background is False
            and draw_blocks is False
            and draw_walls is False
            and draw_liquids is False
            and draw_wires is False
        ):
            raise c.ClickException("All layers are disabled, nothing to render")

        c.echo(f"Draw background layer: {draw_background}")
        c.echo(f"Draw blocks layer: {draw_blocks}")
        c.echo(f"Draw walls layer: {draw_walls}")
        c.echo(f"Draw liquids layer: {draw_liquids}")
        c.echo(f"Draw wires layer: {draw_wires}")
        c.echo(f"Draw paints: {draw_paint}")
        if colors_file:
            c.echo(f"Colors: from {colors_file}")
        else:
            c.echo("Colors: TEdit defaults")
        c.echo("")

        if colors_file:
            c.echo("Reading colors...")
            with open(colors_file) as file:
                colors = json.load(file)
        else:
            colors = DEFAULT_COLORS

        to_merge = []

        c.echo("Parsing world...")
        world: li.World = li.World.create_from_file(input_file)
        min_x, min_y, max_x, max_y = self.get_region_size(
            world=world, min_x=min_x, min_y=min_y, region_width=region_width, region_height=region_height
        )
        c.echo(f"Rendering world coordinates between ({min_x}, {min_y}) to ({max_x}, {max_y}")
        width = max_x - min_x
        height = max_y - min_y
        if draw_background:
            c.echo("Drawing the background...")
            background = Image.new("RGBA", (width, height))
            draw = ImageDraw.Draw(background)
            curr_y = 0
            if min_y <= world.underground_level:
                sky_y = min(world.underground_level - min_y, height)
                draw.rectangle(((0, curr_y), (width, sky_y)), tuple(colors["Globals"].get("Sky", (0, 0, 0, 0))))
                curr_y = sky_y + 1
            if max_y > world.underground_level and min_y <= world.cavern_level:
                earth_y = min(world.cavern_level - min_y, height)
                draw.rectangle(((0, curr_y), (width, earth_y)), tuple(colors["Globals"].get("Earth", (0, 0, 0, 0))))
                curr_y = earth_y + 1
            edge_of_rock = world.size.y - 192
            if max_y > world.cavern_level and min_y <= edge_of_rock:
                rock_y = min(edge_of_rock - min_y, height)
                draw.rectangle(((0, curr_y), (width, rock_y)), tuple(colors["Globals"].get("Rock", (0, 0, 0, 0))))
                curr_y = rock_y + 1
            if max_y > edge_of_rock:
                draw.rectangle(((0, curr_y), (width, height)), tuple(colors["Globals"].get("Hell", (0, 0, 0, 0))))
            del draw
            to_merge.append(background)

        if draw_walls:
            c.echo("Drawing walls...")
            walls = Image.new("RGBA", (width, height))
            draw = ImageDraw.Draw(walls)
            for x in range(min_x, max_x):
                for y in range(min_y, max_y):
                    tile = world.tiles[x, y]
                    if tile.wall:
                        if draw_paint and tile.wall.paint:
                            color = tuple(colors["Paints"].get(str(tile.wall.paint), (0, 0, 0, 0)))
                        else:
                            color = tuple(colors["Walls"].get(str(tile.wall.type.value), (0, 0, 0, 0)))
                        draw.point((x - min_x, y - min_y), color)
                if not x % 100:
                    c.echo(f"{x} / {width} rows done")
            del draw
            to_merge.append(walls)

        if draw_liquids:
            c.echo("Drawing liquids...")
            liquids = Image.new("RGBA", (width, height))
            draw = ImageDraw.Draw(liquids)
            for x in range(min_x, max_x):
                for y in range(min_y, max_y):
                    tile = world.tiles[x, y]
                    if tile.liquid:
                        if tile.liquid.type == le.LiquidType.WATER:
                            color = tuple(colors["Globals"].get("Water", (0, 0, 0, 0)))
                        elif tile.liquid.type == le.LiquidType.LAVA:
                            color = tuple(colors["Globals"].get("Lava", (0, 0, 0, 0)))
                        elif tile.liquid.type == le.LiquidType.HONEY:
                            color = tuple(colors["Globals"].get("Honey", (0, 0, 0, 0)))
                        else:
                            continue
                        draw.point((x - min_x, y - min_y), color)
                if not x % 100:
                    c.echo(f"{x} / {width} rows done")
            del draw
            to_merge.append(liquids)

        if draw_blocks:
            c.echo("Drawing blocks...")
            blocks = Image.new("RGBA", (width, height))
            draw = ImageDraw.Draw(blocks)
            for x in range(min_x, max_x):
                for y in range(min_y, max_y):
                    tile = world.tiles[x, y]
                    if tile.block:
                        if draw_paint and tile.block.paint:
                            color = tuple(colors["Paints"].get(str(tile.block.paint), (0, 0, 0, 0)))
                        else:
                            color = tuple(colors["Blocks"].get(str(tile.block.type.value), (0, 0, 0, 0)))
                        draw.point((x - min_x, y - min_y), color)
                if not x % 100:
                    c.echo(f"{x} / {width} rows done")
            del draw
            to_merge.append(blocks)

        if draw_wires:
            c.echo("Drawing wires...")
            wires = Image.new("RGBA", (width, height))
            draw = ImageDraw.Draw(wires)
            for x in range(min_x, max_x):
                for y in range(min_y, max_y):
                    tile = world.tiles[x, y]
                    if tile.wiring:
                        if tile.wiring.red:
                            color = tuple(colors["Globals"].get("Wire", (0, 0, 0, 0)))
                        elif tile.wiring.blue:
                            color = tuple(colors["Globals"].get("Wire1", (0, 0, 0, 0)))
                        elif tile.wiring.green:
                            color = tuple(colors["Globals"].get("Wire2", (0, 0, 0, 0)))
                        elif tile.wiring.yellow:
                            color = tuple(colors["Globals"].get("Wire3", (0, 0, 0, 0)))
                        else:
                            continue
                        draw.point((x - min_x, y - min_y), color)
                if not x % 100:
                    c.echo(f"{x} / {width} rows done")
            del draw
            to_merge.append(wires)

        c.echo("Merging layers...")
        final = Image.new("RGBA", (width, height))
        while to_merge:
            final = Image.alpha_composite(final, to_merge.pop(0))

        c.echo("Saving image...")
        final.save(output_file)

        c.echo("Done!")

    def get_region_size(self,
        *,
        world: li.World,
        min_x: typing.Optional[int] = None,
        min_y: typing.Optional[int] = None,
        region_width: typing.Optional[int] = None,
        region_height: typing.Optional[int] = None,
    ):
        min_x = max(0, min_x or 0)
        min_y = max(0, min_y or 0)
        if region_width:
            max_x = min(world.size.x, (min_x or world.size.x) + region_width)
        else:
            max_x = world.size.x
        if region_height:
            max_y = min(world.size.y, (min_y or world.size.y) + region_height)
        else:
            max_y = world.size.y
        return min_x, min_y, max_x, max_y


if __name__ == "__main__":
    flyingsnake2.flyingsnake()
