import msgspec


class AudioPostInsertPlugin(msgspec.Struct, kw_only=True):
    on: bool
    insert: str


class AudioPostInsertPluginWithAutomix(AudioPostInsertPlugin, kw_only=True):
    mode: str
    autogain_weight: float
