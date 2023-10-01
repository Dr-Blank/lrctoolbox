from lrctoolbox import SyncedLyrics
from lrctoolbox.synced_lyric_line import SyncedLyricLine

txt_lines = [
    "Foo bar",
    "Baz qux",
    "Quux quuz",
]

zero_timestamp_lines = [f"[00:00.00]{line}" for line in txt_lines]


def test_load_from_lines():
    synced_lyrics = SyncedLyrics.load_from_lines(zero_timestamp_lines)
    assert not synced_lyrics.is_synced


def test_print():
    synced_lyrics = SyncedLyrics.load_from_lines(zero_timestamp_lines)
    assert synced_lyrics.lyrics == txt_lines
