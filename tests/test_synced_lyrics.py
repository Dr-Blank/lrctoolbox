from pathlib import Path

import pytest

from lrctoolbox.exceptions import FileTypeError, LRCError
from lrctoolbox.synced_lyric_line import SyncedLyricLine
from lrctoolbox.synced_lyrics import SyncedLyrics


def test_load_from_lines():
    artist = "Pritam, Arijit Singh"
    title = "Shayad"
    album = "Love Aaj Kal"
    lyricist = "Irshad Kamil"
    uri = "spotify:track:foobarbazqux"
    length = "200000"
    re_name = "LRCMaker"
    version = "1.0.0"
    author = "DrB"

    lines = [
        f"[ar:{artist}]",
        f"[ti: {title}]",
        f"[al:{album}]",
        f"[au:{lyricist}]",
        f"[by:{author}]",
        f"[re:{re_name}]",
        f"[ve:{version}]",
        f"[uri:{uri}]",
        f"[length:{length}]",
        "[00:00.00]Foo bar",
        "[00:10.00]Quux quuz",
        "[00:05.00]Baz qux",
        "",
        "",
    ]

    synced_lyrics = SyncedLyrics.load_from_lines(lines)
    assert synced_lyrics.artist == artist
    assert synced_lyrics.title == title
    assert synced_lyrics.album == album
    assert synced_lyrics.lyricist == lyricist
    assert synced_lyrics.author == author
    assert synced_lyrics.re_name == re_name
    assert synced_lyrics.version == version
    assert synced_lyrics.uri == uri
    assert synced_lyrics.length == length
    assert synced_lyrics.lyrics == [
        "[00:00.00]Foo bar",
        "[00:05.00]Baz qux",
        "[00:10.00]Quux quuz",
    ]


def test_update_metadata():
    synced_lyrics = SyncedLyrics()
    synced_lyrics.update_metadata(
        {"artist": "Artist", "album": "Album", "title": "Title"}
    )
    synced_lyrics.update_metadata(
        {"artist": "New Artist", "album": "New Album"}
    )
    assert synced_lyrics.artist == "New Artist"
    assert synced_lyrics.title == "Title"
    assert synced_lyrics.album == "New Album"


def test_lines_setter_getter():
    synced_lyrics = SyncedLyrics()
    lines = [
        SyncedLyricLine(text="Foo bar", timestamp=0),
        SyncedLyricLine(text="Baz qux", timestamp=5000),
        SyncedLyricLine(text="Quux quuz", timestamp=10000),
    ]
    synced_lyrics.lines = lines
    assert synced_lyrics.lyrics == [
        "[00:00.00]Foo bar",
        "[00:05.00]Baz qux",
        "[00:10.00]Quux quuz",
    ]
    assert synced_lyrics.lines == lines


def test_lyrics_setter_getter():
    synced_lyrics = SyncedLyrics()
    lyrics = [
        "[00:00.00]Foo bar",
        "[00:05.00]Baz qux",
        "[00:10.00]Quux quuz",
    ]
    synced_lines = [
        SyncedLyricLine(text="Foo bar", timestamp=0),
        SyncedLyricLine(text="Baz qux", timestamp=5000),
        SyncedLyricLine(text="Quux quuz", timestamp=10000),
    ]
    synced_lyrics.lyrics = lyrics
    assert synced_lyrics.lyrics == lyrics
    assert synced_lyrics.lines == synced_lines
    synced_lyrics.lyrics = []
    assert not synced_lyrics.lyrics
    assert not synced_lyrics.lines

    synced_lyrics.lyrics = synced_lines
    assert synced_lyrics.lyrics == lyrics
    assert synced_lyrics.lines == synced_lines


def test_timestamp_properties():
    synced_lyrics = SyncedLyrics()
    assert synced_lyrics._is_timestamp_in_ascending_order is False
    assert synced_lyrics._is_timestamp_all_same is False
    assert synced_lyrics._is_missing_any_timestamp is False
    lyrics = [
        "[00:00.00]Foo bar",
        "[00:05.00]Baz qux",
        "[00:10.00]Quux quuz",
    ]
    synced_lyrics.lyrics = lyrics
    assert synced_lyrics._is_missing_any_timestamp is False
    synced_lyrics.lines[0].timestamp = None
    assert synced_lyrics._is_missing_any_timestamp is True
    synced_lyrics.lines[0].timestamp = 0
    assert synced_lyrics._is_timestamp_in_ascending_order is True
    synced_lyrics.lines[2].timestamp = 2500
    assert synced_lyrics._is_timestamp_in_ascending_order is False
    assert synced_lyrics._is_timestamp_all_same is False
    synced_lyrics.lines[1].timestamp = 0
    synced_lyrics.lines[2].timestamp = 0
    assert synced_lyrics._is_timestamp_all_same is True


@pytest.mark.parametrize(
    "line, expected",
    [
        ("[au: DrB]", "DrB"),
        ("[00:00.00]Lyricist: DrB ", "DrB"),
    ],
)
def test_string_parsing_lyricist(line, expected):
    synced_lyrics = SyncedLyrics()
    res = synced_lyrics.parse_str(line)
    assert isinstance(res, dict)
    assert res.get("lyricist") == expected


@pytest.mark.parametrize(
    "line, expected",
    [
        ("[00:00.00]Foo bar", SyncedLyricLine(text="Foo bar", timestamp=0)),
        ("[00:05.00]Baz qux", SyncedLyricLine(text="Baz qux", timestamp=5000)),
        (
            "[14:25.565]Quux quuz",
            SyncedLyricLine(text="Quux quuz", timestamp=865565),
        ),
        ("Quux quuz", SyncedLyricLine(text="Quux quuz")),
    ],
)
def test_string_parsing_lyrics(line, expected):
    synced_lyrics = SyncedLyrics()
    res = synced_lyrics.parse_str(line)
    assert isinstance(res, SyncedLyricLine)
    assert res == expected
