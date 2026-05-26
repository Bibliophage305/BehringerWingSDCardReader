import msgspec


class AudioRecordSettings(msgspec.Struct, kw_only=True):
    path: str
    resolution: str
    channels: str
