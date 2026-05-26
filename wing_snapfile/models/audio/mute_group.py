import msgspec


class AudioMuteGroup(msgspec.Struct, kw_only=True):
    name: str
    mute_on: bool
