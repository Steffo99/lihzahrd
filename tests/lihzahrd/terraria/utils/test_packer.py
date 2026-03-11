from io import BytesIO

import pytest
from lihzahrd.terraria.utils.file_processor import FileProcessor


@pytest.mark.parametrize(
    "write_val",
    [
        0,
        1,
        12,
        123,
        1234,
        12345,
    ],
)
def test_rw_uleb128(write_val):
    stream = BytesIO()
    fp = FileProcessor(stream)

    fp.write_uleb128(write_val)
    fp.stream.seek(0)
    read_val = fp.read_uleb128()

    assert read_val == write_val


@pytest.mark.parametrize(
    "write_val",
    [
        (False, False, False, False, False, False, False, False),
        (False, False, False, False, False, False, False, True),
        (False, True, False, True, False, True, False, True),
        (True, True, True, True, True, True, True, True),
    ],
)
def test_rw_bits(write_val):
    stream = BytesIO()
    fp = FileProcessor(stream)

    fp.write_bits(write_val)
    fp.stream.seek(0)
    read_val = fp.read_bits()

    assert read_val == write_val
