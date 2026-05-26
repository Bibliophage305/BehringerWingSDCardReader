import msgspec


class AudioInputConnections(msgspec.Struct, kw_only=True):
    group: str
    input: int
    alt_group: str
    alt_input: int