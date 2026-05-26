from wing_snapfile.models.console.data import ConsoleData

from wing_snapfile.protocol.helpers.indexed import (
    parse_indexed,
)


class ConsoleDataCodec:
    @staticmethod
    def decode(data: dict) -> ConsoleData:
        return ConsoleData(
            config=data["cfg"],
            layer=data["layer"],
            user=data["user"],

            gpio=parse_indexed(data["gpio"]),

            global_safes=data["safes"],

            daw=data["daw"],
            midi=data["midi"],
            osc=data["osc"],

            library=data["lib"],
        )

    @staticmethod
    def encode(obj: ConsoleData) -> dict:
        return {
            "cfg": obj.config,
            "layer": obj.layer,
            "user": obj.user,

            "gpio": obj.gpio.to_dict(),

            "safes": obj.global_safes,

            "daw": obj.daw,
            "midi": obj.midi,
            "osc": obj.osc,

            "lib": obj.library,
        }