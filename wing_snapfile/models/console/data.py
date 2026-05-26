import msgspec

from wing_snapfile.types.one_indexed_list import OneIndexedList


class ConsoleData(msgspec.Struct, kw_only=True):
    config: dict
    layer: dict
    user: dict

    gpio: OneIndexedList[dict]

    global_safes: dict

    daw: dict
    midi: dict
    osc: dict

    library: dict