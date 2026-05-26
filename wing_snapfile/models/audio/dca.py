import msgspec


class AudioDCA(msgspec.Struct, kw_only=True):
    name: str
    color: int
    icon: int
    led_on: bool
    mute_on: bool
    fader_level: float
    monitor_mode: str
