from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.types.one_indexed_list import OneIndexedList

@dataclass_validate
@dataclass(kw_only=True)
class Channel:
    type: str
    index: int
    destination_index: int

@dataclass_validate
@dataclass(kw_only=True)
class Layer:
    offset: int
    name: str
    channels: OneIndexedList[Channel]

@dataclass_validate
@dataclass(kw_only=True)
class Region:
    layer_select: int
    spilled_group: int
    layers: OneIndexedList[Layer]

@dataclass_validate
@dataclass(kw_only=True)
class LayerConfig:
    left_wing: Region
    center_wing: Region
    right_wing: Region
    compact: Region
    rack: Region
    external: Region
    virtual: Region
    wing_edit: Region