import logging
import os
import pathlib
import platform
import sys

import click

from lihzahrd.terraria.common.file_metadata import FileMetadata
from lihzahrd.terraria.utils.file_processor import FileProcessor
from lihzahrd.terraria.world.frame_important.world_frame_important import WorldFrameImportant
from lihzahrd.terraria.world.header.world_header import WorldHeader
from lihzahrd.terraria.world.sections.world_sections import WorldSections

log = logging.getLogger(__name__)


@click.group()
@click.pass_context
@click.version_option(package_name="lihzahrd", prog_name="lihzahrd")
@click.option(
    "--force-color/--no-color",
    "color",
    is_flag=True,
    type=bool,
    default=None,
    envvar="LIHZAHRD_FORCE_COLOR",
    help="Force or disable the use of color in the output.",
)
@click.option(
    "-d",
    "--directory",
    type=click.Path(file_okay=False, dir_okay=True, readable=True, executable=True, path_type=pathlib.Path),
    envvar="TERRARIA_SAVE_DIRECTORY",
    help="The base directory containing the Terraria saves to display. If unset, attempts to use the default location for your platform.",
)
@click.option(
    "--directory-auto-proton",
    is_flag=True,
    type=bool,
    default=False,
    envvar="TERRARIA_SAVE_DIRECTORY_USE_PROTON",
    help="If --directory is not specified, and you're on Linux, attempt to use the Proton save directory instead of the native one.",
)
@click.option(
    "-q",
    "--quietness",
    type=int,
    default=60,
    envvar="LIHZAHRD_QUIETNESS",
    help="The quietness level of the debug logger. Defaults to 60 (no logging), but can be decreased in increments of 10 to gradually increase the amount of output messages, up to 0 (all messages).",
)
def core(
    ctx: click.Context,
    color: bool | None = None,
    directory: pathlib.Path | None = None,
    directory_auto_proton: bool = False,
    quietness: int = 60,
):
    """
    Interact with Terraria save files.
    """

    logging.basicConfig(
        level=quietness, format="%(asctime)s | %(name)56s | %(levelname)8s | %(message)s", stream=sys.stderr
    )
    log.debug("Set up logging with quietness level %r", quietness)

    ctx.max_content_width = 10000
    ctx.show_default = True
    ctx.color = color

    ctx.ensure_object(dict)

    if not directory:
        match platform.system():
            case "Windows":
                if "USERPROFILE" in os.environ:
                    directory = pathlib.Path(os.environ["USERPROFILE"]) / "Documents" / "My Games" / "Terraria"
                else:
                    directory = pathlib.Path.home() / "Documents" / "My Games" / "Terraria"
            case "Darwin":
                if "HOME" in os.environ:
                    directory = pathlib.Path(os.environ["HOME"]) / "Library" / "Application Support" / "Terraria"
                else:
                    directory = pathlib.Path.home() / "Library" / "Application Support" / "Terraria"
            case "Linux":
                if directory_auto_proton and "HOME" in os.environ:
                    directory = (
                        pathlib.Path(os.environ["HOME"])
                        / ".steam"
                        / "steam"
                        / "steamapps"
                        / "compatdata"
                        / "105600"
                        / "pfx"
                        / "drive_c"
                        / "users"
                        / "steamuser"
                        / "Documents"
                        / "My Games"
                        / "Terraria"
                    )
                elif directory_auto_proton:
                    directory = (
                        pathlib.Path.home()
                        / ".steam"
                        / "steam"
                        / "steamapps"
                        / "compatdata"
                        / "105600"
                        / "pfx"
                        / "drive_c"
                        / "users"
                        / "steamuser"
                        / "Documents"
                        / "My Games"
                        / "Terraria"
                    )
                elif "XDG_DATA_HOME" in os.environ:
                    directory = pathlib.Path(os.environ["XDG_DATA_HOME"]) / "Terraria"
                elif "HOME" in os.environ:
                    directory = pathlib.Path(os.environ["HOME"]) / ".local" / "share" / "Terraria"
                else:
                    directory = pathlib.Path.home() / ".local" / "share" / "Terraria"
            case _:
                raise click.ClickException(
                    "Could not determine Terraria save directory. Please specify `--directory` and try again."
                )

        if not directory.is_dir():
            raise click.ClickException(f"The specified `--directory` is not a directory: `{directory}`")

    ctx.obj["directory"] = directory


@core.group()
@click.pass_context
def worlds(ctx: click.Context):
    """
    Interact with world save files.
    """

    directory = ctx.obj["directory"]
    directory_worlds: pathlib.Path = directory / "Worlds"

    if not directory_worlds.is_dir():
        raise click.ClickException(f"No `Worlds` directory found at the specified `--directory`: `{directory_worlds}`")

    ctx.obj["directory_worlds"] = directory_worlds


# noinspection PyUnresolvedReferences
@worlds.command("list")
@click.pass_context
def list_(ctx: click.Context):
    """
    Display a brief summary of the available world save files.
    """

    directory_worlds: pathlib.Path = ctx.obj["directory_worlds"]

    paths_worlds = list(directory_worlds.glob("*.wld"))

    if len(paths_worlds) == 0:
        log.error("No worlds found.")
        exit(66)  # EX_NOINPUT

    for path_world in paths_worlds:
        with open(path_world, mode="rb") as file_world:
            fp = FileProcessor(stream=file_world)

            try:
                _file_meta = FileMetadata.read(fp, strict=True).instance
                _sections = WorldSections.read(fp, strict=True).instance
                _frame_important = WorldFrameImportant.read(fp, strict=True).instance
                world_header = WorldHeader.read(fp, strict=True).instance
            except Exception:
                log.error("Could not read data of: %r", path_world, exc_info=True)
                continue

            name = click.style(f"{world_header.name.value}", bold=True)

            difficulty = world_header.difficulty
            fortheworthy = world_header.special_fortheworthy

            if difficulty.is_journey():
                difficulty = click.style("Journey", fg="bright_magenta")
            elif difficulty.is_master() and fortheworthy:
                difficulty = click.style("Legendary", fg="bright_green")
            elif difficulty.is_expert() and fortheworthy or difficulty.is_master():
                difficulty = click.style("Master", fg="bright_red")
            elif difficulty.is_classic() and fortheworthy or difficulty.is_expert():
                difficulty = click.style("Expert", fg="bright_yellow")
            else:
                difficulty = click.style("Classic", fg="bright_white")

            golden = world_header.defeated_moonlord.value

            bosses = world_header.bosses()
            bosses_defeated = list(filter(bool, bosses))
            bosses_ratio = len(bosses_defeated) / len(bosses)

            progress = click.style(f"{bosses_ratio:.0%}", fg="bright_yellow" if golden else None, bold=golden)

            if world_header.size.value.x == 8400 and world_header.size.value.y == 2400:
                size = click.style("Large World", italic=True)
            elif world_header.size.value.x == 6400 and world_header.size.value.y == 1800:
                size = click.style("Medium World", italic=True)
            elif world_header.size.value.x == 4200 and world_header.size.value.y == 1200:
                size = click.style("Small World", italic=True)

            extra = ""
            if world_header.special_drunk:
                extra += " - "
                extra += click.style("Drunk", italic=True)
            if world_header.special_fortheworthy:
                extra += " - "
                extra += click.style("For The Worthy", italic=True)
            if world_header.special_anniversary:
                extra += " - "
                extra += click.style("10th Anniversary", italic=True)
            if world_header.special_dontstarve:
                extra += " - "
                extra += click.style("Don't Starve", italic=True)
            if world_header.special_notthebees:
                extra += " - "
                extra += click.style("Not The Bees", italic=True)
            if world_header.special_remix:
                extra += " - "
                extra += click.style("Remix", italic=True)
            if world_header.special_notraps:
                extra += " - "
                extra += click.style("No Traps", italic=True)
            if world_header.special_zenith:
                extra += " - "
                extra += click.style("Zenith", italic=True)
            if world_header.special_skyblock:
                extra += " - "
                extra += click.style("Skyblock", italic=True)

            click.echo(name + " - " + difficulty + " - " + progress + " - " + size + extra)
