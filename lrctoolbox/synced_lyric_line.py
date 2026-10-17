""" Class that represents a single synced lyric line. """

from dataclasses import dataclass
from datetime import datetime


@dataclass
class SyncedLyricLine:
    """A class that represents a single synced lyric line.
    Attributes:
        AddWhiteSpace (bool): whether to add white space between timestamp and text
        """
    text: str
    timestamp: int | None = None
    AddWhiteSpace: bool = False

    """in milliseconds"""

    @property
    def formatted_lyric(self) -> str:
        """returns the formatted lyric with timestamp"""
        if self.AddWhiteSpace:
            return f"{self._formatted_timestamp} {self.text}"
        else:
            return f"{self._formatted_timestamp}{self.text}"


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
