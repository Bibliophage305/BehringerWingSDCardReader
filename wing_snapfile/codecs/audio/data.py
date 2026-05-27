from wing_snapfile.models.audio.data import AudioData

from wing_snapfile.codecs.audio.config import AudioConfigCodec
from wing_snapfile.codecs.audio.io import IOCodec

from wing_snapfile.codecs.audio.channel import (
    FullChannelCodec,
    AuxChannelCodec,
    BusChannelCodec,
    MainChannelCodec,
    MatrixChannelCodec,
)

from wing_snapfile.codecs.audio.dca import DCACodec
from wing_snapfile.codecs.audio.mute_group import MuteGroupCodec
from wing_snapfile.codecs.audio.expansion_cards import ExpansionCardsCodec
from wing_snapfile.codecs.audio.play_settings import PlaySettingsCodec
from wing_snapfile.codecs.audio.record_settings import RecordSettingsCodec

from wing_snapfile.helpers.indexed import encode_one_indexed_list, decode_one_indexed_list


class AudioDataCodec:
    @staticmethod
    def decode(data: dict) -> AudioData:
        return AudioData(
            config=AudioConfigCodec.decode(data["cfg"]),
            io=IOCodec.decode(data["io"]),

            channels=decode_one_indexed_list(
                data["ch"],
                FullChannelCodec.decode,
            ),

            aux_channels=decode_one_indexed_list(
                data["aux"],
                AuxChannelCodec.decode,
            ),

            busses=decode_one_indexed_list(
                data["bus"],
                BusChannelCodec.decode,
            ),

            mains=decode_one_indexed_list(
                data["main"],
                MainChannelCodec.decode,
            ),

            matrices=decode_one_indexed_list(
                data["mtx"],
                MatrixChannelCodec.decode,
            ),

            dcas=decode_one_indexed_list(
                data["dca"],
                DCACodec.decode,
            ),

            mute_groups=decode_one_indexed_list(
                data["mgrp"],
                MuteGroupCodec.decode,
            ),

            fx=decode_one_indexed_list(
                data["fx"],
                lambda x: x,   # still raw dicts for now
            ),

            expansion_cards=ExpansionCardsCodec.decode(data["cards"]),
            play_settings=PlaySettingsCodec.decode(data["play"]),
            record_settings=RecordSettingsCodec.decode(data["rec"]),
        )

    @staticmethod
    def encode(obj: AudioData) -> dict:
        return {
            "cfg": AudioConfigCodec.encode(obj.config),
            "io": IOCodec.encode(obj.io),
            "ch": encode_one_indexed_list(obj.channels, FullChannelCodec.encode),
            "aux": encode_one_indexed_list(obj.aux_channels, AuxChannelCodec.encode),
            "bus": encode_one_indexed_list(obj.busses, BusChannelCodec.encode),
            "main": encode_one_indexed_list(obj.mains, MainChannelCodec.encode),
            "mtx": encode_one_indexed_list(obj.matrices, MatrixChannelCodec.encode),
            "dca": encode_one_indexed_list(obj.dcas, DCACodec.encode),
            "mgrp": encode_one_indexed_list(obj.mute_groups, MuteGroupCodec.encode),
            "fx": encode_one_indexed_list(obj.fx),

            "cards": ExpansionCardsCodec.encode(obj.expansion_cards),
            "play": PlaySettingsCodec.encode(obj.play_settings),
            "rec": RecordSettingsCodec.encode(obj.record_settings),
        }