from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.types.one_indexed_list import OneIndexedList


@dataclass_validate
@dataclass(kw_only=True)
class ConsoleData:
    config: dict
    layer: dict
    user: dict

    gpio: OneIndexedList[dict]

    global_safes: dict

    daw: dict
    midi: dict
    osc: dict

    library: dict