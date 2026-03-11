import pathlib

import pytest
from lihzahrd.terraria.utils.file_processor import FileProcessor

PATH_THIS = pathlib.Path(__file__)
PATH_THIS_DIR = PATH_THIS.parent

NAME_PLR = "player"
PATH_PLR = PATH_THIS_DIR / NAME_PLR
NAME_PLR_GWENT = "Gwent.plr"
PATH_PLR_GWENT = PATH_PLR / NAME_PLR_GWENT

NAME_WLD = "world"
PATH_WLD = PATH_THIS_DIR / NAME_WLD
NAME_WLD_THEBUGGINGZONE = "The_Bugging_Zone.wld"
PATH_WLD_THEBUGGINGZONE = PATH_WLD / NAME_WLD_THEBUGGINGZONE
NAME_WLD_THEDISHWASHERMIC = "The_Dishwasher_Mic.wld"
PATH_WLD_THEDISHWASHERMIC = PATH_WLD / NAME_WLD_THEDISHWASHERMIC
NAME_WLD_HONEYOFPRIVACY = "Honey_of_Privacy.wld"
PATH_WLD_HONEYOFPRIVACY = PATH_WLD / NAME_WLD_HONEYOFPRIVACY
NAME_WLD_RESTFULHEART = "Restful_Heart.wld"
PATH_WLD_RESTFULHEART = PATH_WLD / NAME_WLD_RESTFULHEART
NAME_WLD_UNSIGHTLYMAZE = "Unsightly_Maze.wld"
PATH_WLD_UNSIGHTLYMAZE = PATH_WLD / NAME_WLD_UNSIGHTLYMAZE
NAME_WLD_MIRAGEOFKINDNESS = "Mirage_of_Kindness.wld"
PATH_WLD_MIRAGEOFKINDNESS = PATH_WLD / NAME_WLD_MIRAGEOFKINDNESS
NAME_WLD_THEBLESSEDLAND = "The_Blessed_Land.wld"
PATH_WLD_THEBLESSEDLAND = PATH_WLD / NAME_WLD_THEBLESSEDLAND


@pytest.fixture(params=(pytest.param(PATH_PLR_GWENT, id=NAME_PLR_GWENT)))
def fp_plr_read(request):
    with open(request.param, mode="rb") as file:
        yield FileProcessor(stream=file)


@pytest.fixture(
    params=(
        # pytest.param(
        #     PATH_WLD_THEBUGGINGZONE,
        #     id=NAME_WLD_THEBUGGINGZONE,
        #     marks=pytest.mark.xfail(reason="Old version"),
        # ),
        # pytest.param(
        #     PATH_WLD_THEDISHWASHERMIC,
        #     id=NAME_WLD_THEDISHWASHERMIC,
        #     marks=pytest.mark.xfail(reason="Old version"),
        # ),
        pytest.param(PATH_WLD_HONEYOFPRIVACY, id=NAME_WLD_HONEYOFPRIVACY),
        pytest.param(PATH_WLD_RESTFULHEART, id=NAME_WLD_RESTFULHEART),
        pytest.param(PATH_WLD_UNSIGHTLYMAZE, id=NAME_WLD_UNSIGHTLYMAZE),
        pytest.param(PATH_WLD_MIRAGEOFKINDNESS, id=NAME_WLD_MIRAGEOFKINDNESS),
        pytest.param(PATH_WLD_THEBLESSEDLAND, id=NAME_WLD_THEBLESSEDLAND),
    )
)
def fp_wld_read(request):
    with open(request.param, mode="rb") as file:
        yield FileProcessor(stream=file)


@pytest.fixture()
def fp_plr_gwent_read():
    with open(PATH_PLR_GWENT, mode="rb") as file:
        yield FileProcessor(stream=file)


@pytest.fixture()
def fp_wld_read_thebuggingzone_read():
    with open(PATH_WLD_THEBUGGINGZONE, mode="rb") as file:
        yield FileProcessor(stream=file)


@pytest.fixture()
def fp_wld_read_thedishwashermic_read():
    with open(PATH_WLD_THEDISHWASHERMIC, mode="rb") as file:
        yield FileProcessor(stream=file)
