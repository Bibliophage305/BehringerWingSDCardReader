from wing_snapfile.helpers.indexed import (
    decode_one_indexed_list,
    encode_one_indexed_list,
    filter_indexed_keys,
)
from wing_snapfile.models.console.layers import Channel, Layer, LayerConfig, Region


class ChannelCodec:
    @staticmethod
    def decode(data: dict) -> Channel:
        return Channel(
            type=data["type"],
            index=data["i"],
            destination_index=data["dst"],
        )

    @staticmethod
    def encode(obj: Channel) -> dict:
        return {
            "type": obj.type,
            "i": obj.index,
            "dst": obj.destination_index,
        }


class LayerCodec:
    @staticmethod
    def decode(data: dict) -> Layer:
        return Layer(
            offset=data["ofs"],
            name=data["name"],
            channels=decode_one_indexed_list(
                filter_indexed_keys(data),
                ChannelCodec.decode,
            ),
        )

    @staticmethod
    def encode(obj: Layer) -> dict:
        return {
            "ofs": obj.offset,
            "name": obj.name,
            **encode_one_indexed_list(obj.channels, ChannelCodec.encode),
        }


class RegionCodec:
    @staticmethod
    def decode(data: dict) -> Region:
        return Region(
            layer_select=data["sel"],
            spilled_group=data["spidx"],
            layers=decode_one_indexed_list(
                filter_indexed_keys(data),
                LayerCodec.decode,
            ),
        )

    @staticmethod
    def encode(obj: Region) -> dict:
        return {
            "sel": obj.layer_select,
            "spidx": obj.spilled_group,
            **encode_one_indexed_list(obj.layers, LayerCodec.encode),
        }


class LayerConfigCodec:
    @staticmethod
    def decode(data: dict) -> LayerConfig:
        return LayerConfig(
            left_wing=RegionCodec.decode(data["L"]),
            center_wing=RegionCodec.decode(data["C"]),
            right_wing=RegionCodec.decode(data["R"]),
            compact=RegionCodec.decode(data["CMPCT"]),
            rack=RegionCodec.decode(data["RCK"]),
            external=RegionCodec.decode(data["EXT"]),
            virtual=RegionCodec.decode(data["VRT"]),
            wing_edit=RegionCodec.decode(data["WEDIT"]),
        )

    @staticmethod
    def encode(obj: LayerConfig) -> dict:
        return {
            "L": RegionCodec.encode(obj.left_wing),
            "C": RegionCodec.encode(obj.center_wing),
            "R": RegionCodec.encode(obj.right_wing),
            "CMPCT": RegionCodec.encode(obj.compact),
            "RCK": RegionCodec.encode(obj.rack),
            "EXT": RegionCodec.encode(obj.external),
            "VRT": RegionCodec.encode(obj.virtual),
            "WEDIT": RegionCodec.encode(obj.wing_edit),
        }