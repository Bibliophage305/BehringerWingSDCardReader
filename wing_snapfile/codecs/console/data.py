from wing_snapfile.models.console.data import ConsoleData

from wing_snapfile.codecs.console.config import ConsoleConfigCodec
from wing_snapfile.codecs.console.layers import LayerConfigCodec

from wing_snapfile.helpers.indexed import (
    decode_one_indexed_list,
)

import json

class ConsoleDataCodec:
    @staticmethod
    def decode(data: dict) -> ConsoleData:
        for k, v in data["user"].items():
            if not isinstance(v, dict) or any(not x.isdigit() for x in v.keys()):
                continue
            print(f"\n{k}")
            print(json.dumps(v["1"], indent=4))
            # for i in range(1, len(v) + 1):
            #     print(json.dumps(v[str(i)], indent=4))

        # print(*data["user"].items(), sep="\n")
        return ConsoleData(
            config=ConsoleConfigCodec.decode(data["cfg"]),
            layer_config=LayerConfigCodec.decode(data["layer"]),
            user=data["user"],

            gpio=decode_one_indexed_list(data["gpio"], lambda x: x),

            global_safes=data["safes"],

            daw=data["daw"],
            midi=data["midi"],
            osc=data["osc"],

            library=data["lib"],
        )

    @staticmethod
    def encode(obj: ConsoleData) -> dict:
        return {
            "cfg": ConsoleConfigCodec.encode(obj.config),
            "layer": LayerConfigCodec.encode(obj.layer_config),
            "user": obj.user,

            "gpio": obj.gpio.to_dict(),

            "safes": obj.global_safes,

            "daw": obj.daw,
            "midi": obj.midi,
            "osc": obj.osc,

            "lib": obj.library,
        }