import pytest

from lrctoolbox import SyncedLyrics

artist = "Pritam, Arijit Singh"
title = "Shayad"
album = "Love Aaj Kal"
lyricist = "Irshad Kamil"
uri = "spotify:track:foobarbazqux"
length = "200000"
re_name = "LRCMaker"
version = "1.0.0"
author = "DrB"
synced_lyrics_lines = [
    "[00:00.00]Foo bar",
    "[00:05.00]Baz qux",
    "[00:10.00]Quux quuz",
]

lines = [
    f"[ar:{artist}]",
    f"[ti:{title}]",
    f"[al:{album}]",
    f"[au:{lyricist}]",
    f"[by:{author}]",
    f"[re:{re_name}]",
    f"[ve:{version}]",
    f"[uri:{uri}]",
    f"[length:{length}]",
] + synced_lyrics_lines


@pytest.fixture(scope="module")
def only_lyrics():
    return synced_lyrics_lines


@pytest.fixture
def lines_with_metadata():
    return lines


@pytest.fixture
def metadata():
    return {
        "artist": artist,
        "title": title,
        "album": album,
        "lyricist": lyricist,
        "author": author,
        "re_name": re_name,
        "version": version,
        "uri": uri,
        "length": length,
    }


@pytest.fixture
def sample_synced_lyrics(lines_with_metadata):
    return SyncedLyrics.load_from_lines(lines_with_metadata)
