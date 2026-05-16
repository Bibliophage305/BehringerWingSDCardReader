# TODO

from dataclasses import dataclass
from .snapfile_reader import (
    _parse_json_node,
    _parse_json_object_list,
    JsonObject,
)

@dataclass
class AudioEngineConfig:
    mainlink: str
    dcamgrp: bool
    mon: list[JsonObject]
    solo: JsonObject
    rta: JsonObject
    mtr: JsonObject
    talk: JsonObject
    amix: JsonObject

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioEngineConfig":
        return AudioEngineConfig(
            mainlink=data["mainlink"],
            dcamgrp=data["dcamgrp"],
            mon=_parse_json_object_list(data["mon"]),
            solo=_parse_json_node(data["solo"]),
            rta=_parse_json_node(data["rta"]),
            mtr=_parse_json_node(data["mtr"]),
            talk=_parse_json_node(data["talk"]),
            amix=_parse_json_node(data["amix"]),
        )

