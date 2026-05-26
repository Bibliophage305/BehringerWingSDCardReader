import msgspec


class AudioSend(msgspec.Struct, kw_only=True):
    on: bool
    fader_level: float


class AudioLimitedSend(AudioSend, kw_only=True):
    pre_fader: bool


class AudioFullSend(AudioSend, kw_only=True):
    pre_always_on: bool
    mode: str
    pan_link: int
    pan: int
