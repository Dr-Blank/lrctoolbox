"""A module that contains classes that represent LRC metadata."""

import importlib.metadata
from dataclasses import dataclass
from typing import ClassVar


class BaseLRCMetadata:
    """A class that represents base LRC metadata."""

    LRC_METADATA_MAPPINGS: ClassVar[dict[str, str]] = {}

    @property
    def lrc_formatted_metadata(self) -> list[str]:
        """Return a list of formatted metadata."""
        formatted_metadata = []
        for key, value in self.LRC_METADATA_MAPPINGS.items():
            if not getattr(self, value):
                continue
            formatted_metadata.append(f"[{key}:{getattr(self, value)}]")
        return formatted_metadata


@dataclass()
class TrackMetadataMixin:
    """A class that represents track metadata."""

    artist: str | None = None
    title: str | None = None
    album: str | None = None
    length: str | None = None
    lyricist: str | None = None
    mbid: str | None = None
    uri: str | None = None
    language: str | None = None

    LRC_METADATA_MAPPINGS: ClassVar[dict[str, str]] = {
        "ar": "artist",
        "ti": "title",
        "al": "album",
        "au": "lyricist",
        "uri": "uri",
        "mbid": "mbid",
        "length": "length",
        "language": "language",
    }


@dataclass()
class ModuleMetadataMixin:
    """A class that represents module metadata."""

    re_name: str | None = None
    version: str | None = None
    author: str | None = None

    LRC_METADATA_MAPPINGS: ClassVar[dict[str, str]] = {
        "re": "re_name",
        "ve": "version",
        "by": "author",
    }


class LRCMetadata(BaseLRCMetadata, TrackMetadataMixin, ModuleMetadataMixin):
    """A class that represents combined metadata of module and track."""

    LRC_METADATA_MAPPINGS: ClassVar[dict[str, str]] = {
        **TrackMetadataMixin.LRC_METADATA_MAPPINGS,
        **ModuleMetadataMixin.LRC_METADATA_MAPPINGS,
    }


class TrackMetadata(BaseLRCMetadata, TrackMetadataMixin):
    """A class that represents track metadata."""

    LRC_METADATA_MAPPINGS = TrackMetadataMixin.LRC_METADATA_MAPPINGS


class ModuleMetadata(BaseLRCMetadata, ModuleMetadataMixin):
    """A class that represents module metadata."""

    LRC_METADATA_MAPPINGS = ModuleMetadataMixin.LRC_METADATA_MAPPINGS

    def __init__(
        self,
        re_name: str | None = None,
        version: str | None = None,
        author: str | None = None,
    ):
        """Initialize a new instance of ModuleMetadata."""
        if all(attr is None for attr in (re_name, version)):
            # Get the name and version of the module.
            re_name = __name__.split(".", 1)[0]
            metadata = importlib.metadata.metadata(re_name)
            version = metadata["Version"]
        super().__init__(re_name, version, author)
