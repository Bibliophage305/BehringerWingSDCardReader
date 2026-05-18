# TODO

from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from wing_snapfile.snapfile_reader import (
    _parse_json_node,
    _parse_json_object_list,
    JsonObject,
)
from wing_snapfile.types import OneIndexedList
from wing_snapfile.audio.monitor import AudioMonitor

@dataclass_validate
@dataclass
class AudioConfig:
    mainlink: str
    dcamgrp: bool
    mon: OneIndexedList[AudioMonitor]
    solo: JsonObject
    rta: JsonObject
    mtr: JsonObject
    talk: JsonObject
    amix: JsonObject

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioConfig":
        return AudioConfig(
            mainlink=data["mainlink"],
            dcamgrp=data["dcamgrp"],
            mon=OneIndexedList.from_indexed_dict(data["mon"], AudioMonitor.from_dict),
            solo=_parse_json_node(data["solo"]),
            rta=_parse_json_node(data["rta"]),
            mtr=_parse_json_node(data["mtr"]),
            talk=_parse_json_node(data["talk"]),
            amix=_parse_json_node(data["amix"]),
        )

