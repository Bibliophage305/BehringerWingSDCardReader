import msgspec


class AudioPlaySettings(msgspec.Struct, kw_only=True):
    repeat: bool
