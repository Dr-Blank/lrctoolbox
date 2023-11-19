from pathlib import Path

import pytest

from lrctoolbox.exceptions import FileTypeError
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


def test_mixed_lyrics_type():
    synced_lyrics = SyncedLyrics()
    with pytest.raises(TypeError):
        synced_lyrics.lyrics = [
            "[00:00.00]Foo bar",
            "[00:05.00]Baz qux",
            Path("test.lrc"),
        ]


def test_unsupported_saving_file_type(
    tmp_path: Path,
    sample_synced_lyrics: SyncedLyrics,
):
    unsupported_file = tmp_path / "test.unsupported"
    with pytest.raises(FileTypeError):
        sample_synced_lyrics.save_to_file(unsupported_file)


def test_already_exists(tmp_path: Path, sample_synced_lyrics: SyncedLyrics):
    already_exists = tmp_path / "test.lrc"
    already_exists.touch()
    with pytest.raises(FileExistsError):
        sample_synced_lyrics.save_to_file(already_exists)

    already_exists.unlink()
