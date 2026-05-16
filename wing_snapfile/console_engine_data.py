# TODO

from dataclasses import dataclass
from .snapfile_reader import (
    ConsoleEngineDataConfig,
    ConsoleEngineDataDaw,
    ConsoleEngineDataLayer,
    ConsoleEngineDataUser,
    GpioPin,
    _parse_json_object_as_object,
    _parse_numbered_list,
    JsonObject,
)

from typing import Any

@dataclass
class ConsoleEngineData:
    cfg: ConsoleEngineDataConfig
    daw: ConsoleEngineDataDaw
    gpio: list[GpioPin]
    layer: ConsoleEngineDataLayer
    lib: Any | None
    midi: JsonObject
    osc: JsonObject
    safes: JsonObject
    user: ConsoleEngineDataUser

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "ConsoleEngineData":
        # key = "lib"
        # print(data[key])
        # print(data[key].keys())
        # for k, v in data[key].items():
        #     print(f"{key}.{k} = {v!r}")
        # exit()
        return ConsoleEngineData(
            cfg=ConsoleEngineDataConfig.from_dict(data["cfg"]),
            daw=ConsoleEngineDataDaw.from_dict(data["daw"]),
            gpio=_parse_numbered_list(data["gpio"], GpioPin.from_dict),
            layer=ConsoleEngineDataLayer.from_dict(data["layer"]),
            lib=data["lib"] or None,
            midi=_parse_json_object_as_object(data["midi"]),
            osc=_parse_json_object_as_object(data["osc"]),
            safes=_parse_json_object_as_object(data["safes"]),
            user=ConsoleEngineDataUser.from_dict(data["user"]),
        )