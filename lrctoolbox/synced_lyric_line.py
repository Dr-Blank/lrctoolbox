""" Class that represents a single synced lyric line. """

from dataclasses import dataclass
from datetime import datetime


@dataclass
class SyncedLyricLine:
    """A class that represents a single synced lyric line."""

    text: str
    timestamp: int | None = None
    """in milliseconds"""

    @property
    def formatted_lyric(self) -> str:
        """returns the formatted lyric with timestamp"""
        return self.format()

    def format(self, *, add_whitespace: bool = False) -> str:
        """returns the lyric with timestamp, optionally separated by a space"""
        if self.timestamp is None:
            return self.text

        separator = " " if add_whitespace and self.text else ""
        return f"{self._formatted_timestamp}{separator}{self.text}"

    def __str__(self) -> str:
        return self.formatted_lyric

    @property
    def _formatted_timestamp(self) -> str:
        """returns the formatted timestamp"""
        if self.timestamp is None:
            return ""

        timestamp = datetime.utcfromtimestamp(self.timestamp // 1000).replace(
            microsecond=self.timestamp % 1000 * 1000
        )
        timestamp_str = "[" + f"{timestamp:%M:%S.%f}"[:-4] + "]"
        return timestamp_str
