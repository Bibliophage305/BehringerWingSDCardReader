# TODO

from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from wing_snapfile.types.one_indexed_list import OneIndexedList


@dataclass_validate
@dataclass
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

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "ConsoleData":
        return ConsoleData(
            config=data["cfg"],
            layer=data["layer"],
            user=data["user"],
            gpio=OneIndexedList.from_indexed_dict(data["gpio"]),
            global_safes=data["safes"],
            daw=data["daw"],
            midi=data["midi"],
            osc=data["osc"],
            library=data["lib"],
        )

    def to_dict(self):
        return {
            "cfg": self.config,
            "layer": self.layer,
            "user": self.user,
            "gpio": self.gpio.to_dict(),
            "safes": self.global_safes,
            "daw": self.daw,
            "midi": self.midi,
            "osc": self.osc,
            "lib": self.library,
        }
