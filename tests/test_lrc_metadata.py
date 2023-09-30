from lrctoolbox.lrc_metadata import ModuleMetadata, TrackMetadata


def test_track_metadata():
    metadata = TrackMetadata(
        artist="Adele",
        title="Someone Like You",
        album="21",
        length="4:45",
        lyricist="Adele Adkins",
        uri="https://example.com/someone-like-you",
        mbid="12345678-1234-5678-1234-567812345678",
        language="en",
    )
    assert metadata.lrc_formatted_metadata == [
        "[ar:Adele]",
        "[ti:Someone Like You]",
        "[al:21]",
        "[au:Adele Adkins]",
        "[uri:https://example.com/someone-like-you]",
        "[mbid:12345678-1234-5678-1234-567812345678]",
        "[length:4:45]",
        "[language:en]",
    ]


def test_module_metadata():
    metadata = ModuleMetadata(
        re_name="lrctoolbox",
        version="1.0.0",
        author="John Doe",
    )
    assert metadata.lrc_formatted_metadata == [
        "[re:lrctoolbox]",
        "[ve:1.0.0]",
        "[by:John Doe]",
    ]
