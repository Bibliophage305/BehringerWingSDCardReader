import msgspec


class AudioGateSidechain(msgspec.Struct, kw_only=True):
    type: str
    frequency: float
    q: float
    source: str
    tap: str
