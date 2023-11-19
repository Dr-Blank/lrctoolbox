from pathlib import Path
import random

import pytest

from lrctoolbox.lrc_metadata import TrackMetadata
from lrctoolbox.synced_lyric_line import SyncedLyricLine
from lrctoolbox.synced_lyrics import SyncedLyrics


def test_load_from_lines(only_lyrics, metadata, lines_with_metadata):
    random.shuffle(lines_with_metadata)
    synced_lyrics = SyncedLyrics.load_from_lines(
        lines_with_metadata + [""] * 10
    )
    for key, value in metadata.items():
        assert getattr(synced_lyrics, key) == value
    assert synced_lyrics.lyrics == only_lyrics


def test_update_metadata(sample_synced_lyrics: SyncedLyrics):
    sample_synced_lyrics.update_metadata(
        {"artist": "New Artist", "album": "New Album"}
    )
    assert sample_synced_lyrics.artist == "New Artist"
    assert sample_synced_lyrics.album == "New Album"


def test_lines_setter_getter(sample_synced_lyrics: SyncedLyrics):
    lines = [
        SyncedLyricLine(text="Baz qux", timestamp=0),
        SyncedLyricLine(text="Quux quuz", timestamp=5000),
        SyncedLyricLine(text="Foo bar", timestamp=10000),
    ]
    sample_synced_lyrics.synced_lines = lines
    assert sample_synced_lyrics.lyrics == [
        "[00:00.00]Baz qux",
        "[00:05.00]Quux quuz",
        "[00:10.00]Foo bar",
    ]
    assert sample_synced_lyrics.synced_lines == lines
    assert list(sample_synced_lyrics) == lines


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
    assert synced_lyrics.synced_lines == synced_lines
    synced_lyrics.lyrics = []
    assert not synced_lyrics.lyrics
    assert not synced_lyrics.synced_lines

    synced_lyrics.lyrics = synced_lines
    assert synced_lyrics.lyrics == lyrics
    assert synced_lyrics.synced_lines == synced_lines


def test_timestamp_properties(sample_synced_lyrics):
    synced_lyrics = SyncedLyrics()
    assert synced_lyrics.has_timestamps_in_ascending_order is False
    assert synced_lyrics.has_timestamps_all_equal is False
    assert synced_lyrics.is_missing_any_timestamp is False
    lyrics = [
        "[00:00.00]Foo bar",
        "[00:05.00]Baz qux",
        "[00:10.00]Quux quuz",
    ]
    synced_lyrics.lyrics = lyrics
    assert synced_lyrics.is_missing_any_timestamp is False
    synced_lyrics.synced_lines[0].timestamp = None
    assert synced_lyrics.is_missing_any_timestamp is True
    synced_lyrics.synced_lines[0].timestamp = 0
    assert synced_lyrics.has_timestamps_in_ascending_order is True
    synced_lyrics.synced_lines[2].timestamp = 2500
    assert synced_lyrics.has_timestamps_in_ascending_order is False
    assert synced_lyrics.has_timestamps_all_equal is False
    synced_lyrics.synced_lines[1].timestamp = 0
    synced_lyrics.synced_lines[2].timestamp = 0
    assert synced_lyrics.has_timestamps_all_equal is True


@pytest.mark.parametrize(
    "line, expected",
    [
        ("[ar: Artist]", {"artist": "Artist"}),
        ("[by: DrB]", {"author": "DrB"}),
        ("[al: Album]", {"album": "Album"}),
        ("[ti: Title]", {"title": "Title"}),
        ("[re: LRCMaker]", {"re_name": "LRCMaker"}),
        ("[ve: 1.0.0]", {"version": "1.0.0"}),
        (
            "[uri: spotify:track:foobarbazqux]",
            {"uri": "spotify:track:foobarbazqux"},
        ),
        ("[length: 200000]", {"length": "200000"}),
        ("[00:00.00]Lyricist: DrB ", {"lyricist": "DrB"}),
        ("[random: 200000]", {"random": "200000"}),
    ],
)
def test_metadata_parsing(line, expected):
    synced_lyrics = SyncedLyrics()
    res = synced_lyrics.parse_str(line)
    assert isinstance(res, dict)
    assert res == expected


@pytest.mark.parametrize(
    "line, expected",
    [
        ("[00:00.00]Foo bar", SyncedLyricLine(text="Foo bar", timestamp=0)),
        ("[00:05.00]Baz qux", SyncedLyricLine(text="Baz qux", timestamp=5000)),
        (
            "[14:25.565]Quux quuz",
            SyncedLyricLine(
                text="Quux quuz", timestamp=(14 * 60 + 25) * 1000 + 565
            ),
        ),
        ("Quux quuz", SyncedLyricLine(text="Quux quuz")),
    ],
)
def test_string_parsing_lyrics(line, expected):
    synced_lyrics = SyncedLyrics()
    res = synced_lyrics.parse_str(line)
    assert isinstance(res, SyncedLyricLine)
    assert res == expected


def test_saving_to_file_no_metadata(
    tmp_path: Path,
    sample_synced_lyrics: SyncedLyrics,
    only_lyrics,
):
    path = tmp_path / "foo" / "example.lrc"
    sample_synced_lyrics.save_to_file(
        path, write_metadata=False, overwrite=True
    )
    assert path.exists()
    with path.open() as f:
        lines = f.read().splitlines()
    assert lines == only_lyrics
    path.unlink()


def test_saving_to_file_with_metadata(
    tmp_path: Path,
    sample_synced_lyrics: SyncedLyrics,
    lines_with_metadata,
    only_lyrics,
):
    path = tmp_path / "example.lrc"
    sample_synced_lyrics.re_name = None
    sample_synced_lyrics.version = None
    sample_synced_lyrics.save_to_file(
        path,
        write_metadata=True,
        overwrite=True,
        additional_metadata=TrackMetadata(
            language="gu",
            title="overwritten title",
        ),
    )
    assert path.exists()
    with path.open() as f:
        written_lyrics = SyncedLyrics.load_from_lines(f.read().splitlines())

    assert written_lyrics.artist == sample_synced_lyrics.artist
    assert written_lyrics.language == "gu"
    assert written_lyrics.title == "overwritten title"
    assert written_lyrics.re_name is not None
    assert written_lyrics.version is not None
