import msgspec


class AudioDynamicsCrossover(msgspec.Struct, kw_only=True):
    depth: int
    type: str
    frequency: float
    q: float