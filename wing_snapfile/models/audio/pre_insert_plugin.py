import msgspec


class AudioPreInsertPlugin(msgspec.Struct, kw_only=True):
    on: bool
    insert: str
