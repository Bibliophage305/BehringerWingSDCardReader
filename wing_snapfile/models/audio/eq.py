import msgspec

from wing_snapfile.models.audio.eq_plugins import EQPlugin


class AudioEQ(msgspec.Struct, kw_only=True):
    on: bool
    model: str
    mix: int
    parameters: EQPlugin
