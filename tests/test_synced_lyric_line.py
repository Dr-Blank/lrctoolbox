import pytest
from lrctoolbox.synced_lyric_line import SyncedLyricLine


def test_formatted_lyric_without_timestamp():
    line = SyncedLyricLine(text="Hello")
    assert line.formatted_lyric == "Hello"


@pytest.mark.parametrize(
    "line, expected",
    [
        (
            SyncedLyricLine(text="Hello", timestamp=1000),
            "[00:01.00]Hello",
        ),
        (
            SyncedLyricLine(text="Hello", timestamp=200001),
            "[03:20.00]Hello",
        ),
        (
            SyncedLyricLine(text="Hello", timestamp=200111),
            "[03:20.11]Hello",
        ),
    ],
)
def test_formatted_lyric_with_timestamp(line: SyncedLyricLine, expected):
    assert line.formatted_lyric == expected
