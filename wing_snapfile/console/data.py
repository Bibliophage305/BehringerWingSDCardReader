# TODO

from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from wing_snapfile.snapfile_reader import (
    ConsoleDataConfig,
    ConsoleDataDaw,
    ConsoleDataLayer,
    ConsoleDataUser,
    GpioPin,
    _parse_json_object_as_object,
    _parse_numbered_list,
    JsonObject,
)

@dataclass_validate
@dataclass
class ConsoleData:
    cfg: ConsoleDataConfig
    daw: ConsoleDataDaw
    gpio: list[GpioPin]
    layer: ConsoleDataLayer
    lib: dict
    midi: JsonObject
    osc: JsonObject
    safes: JsonObject
    user: ConsoleDataUser

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "ConsoleData":
        # key = "lib"
        # print(data[key])
        # print(data[key].keys())
        # for k, v in data[key].items():
        #     print(f"{key}.{k} = {v!r}")
        # exit()
        return ConsoleData(
            cfg=ConsoleDataConfig.from_dict(data["cfg"]),
            daw=ConsoleDataDaw.from_dict(data["daw"]),
            gpio=_parse_numbered_list(data["gpio"], GpioPin.from_dict),
            layer=ConsoleDataLayer.from_dict(data["layer"]),
            lib=data["lib"],
            midi=_parse_json_object_as_object(data["midi"]),
            osc=_parse_json_object_as_object(data["osc"]),
            safes=_parse_json_object_as_object(data["safes"]),
            user=ConsoleDataUser.from_dict(data["user"]),
        )