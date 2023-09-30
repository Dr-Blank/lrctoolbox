from pathlib import Path

import pytest

from lrctoolbox.exceptions import FileTypeError, LRCError
from lrctoolbox.synced_lyric_line import SyncedLyricLine
from lrctoolbox.synced_lyrics import SyncedLyrics


def test_unsupported_file_type():
    unsupported_file = Path("test.unsupported")
    unsupported_file.touch()
    with pytest.raises(FileTypeError):
        SyncedLyrics.load_from_file(unsupported_file)

    unsupported_file.unlink()


def test_empty_file():
    empty_file = Path("test.lrc")
    empty_file.touch()
    with pytest.raises(ValueError):
        SyncedLyrics.load_from_file(empty_file)

    empty_file.unlink()


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        SyncedLyrics.load_from_file(Path("nonexistent.lrc"))


def test_load_from_lines():
    artist = "Pritam, Arijit Singh"
    title = "Shayad"
    album = "Love Aaj Kal"
    lyricist = "Irshad Kamil"

    lines = [
        f"[ar:{artist}]",
        f"[ti:{title}]",
        f"[al:{album}]",
        f"[au:{lyricist}]",
        "[00:00.00]Foo bar",
        "[00:05.00]Baz qux",
        "[00:10.00]Quux quuz",
    ]

    synced_lyrics = SyncedLyrics.load_from_lines(lines)
    assert synced_lyrics.artist == artist
    assert synced_lyrics.title == title
    assert synced_lyrics.album == album
    assert synced_lyrics.lyricist == lyricist
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
    synced_lyrics.update_metadata({"artist": "New Artist", "album": "New Album"})
    assert synced_lyrics.artist == "New Artist"
    assert synced_lyrics.title == "Title"
    assert synced_lyrics.album == "New Album"
