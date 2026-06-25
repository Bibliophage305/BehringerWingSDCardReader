from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.models.console.config import ConsoleConfig
from wing_snapfile.models.console.layers import LayerConfig

from wing_snapfile.types.one_indexed_list import OneIndexedList


@dataclass_validate
@dataclass(kw_only=True)
class ConsoleData:
    config: ConsoleConfig
    layer_config: LayerConfig
    user: dict

    gpio: OneIndexedList[dict]

    global_safes: dict

    daw: dict
    midi: dict
    osc: dict

    library: dict