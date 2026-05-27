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

from wing_snapfile.helpers.indexed import encode_indexed, parse_indexed


class AudioDataCodec:
    @staticmethod
    def decode(data: dict) -> AudioData:
        return AudioData(
            config=AudioConfigCodec.decode(data["cfg"]),
            io=IOCodec.decode(data["io"]),

            channels=parse_indexed(
                data["ch"],
                FullChannelCodec.decode,
            ),

            aux_channels=parse_indexed(
                data["aux"],
                AuxChannelCodec.decode,
            ),

            busses=parse_indexed(
                data["bus"],
                BusChannelCodec.decode,
            ),

            mains=parse_indexed(
                data["main"],
                MainChannelCodec.decode,
            ),

            matrices=parse_indexed(
                data["mtx"],
                MatrixChannelCodec.decode,
            ),

            dcas=parse_indexed(
                data["dca"],
                DCACodec.decode,
            ),

            mute_groups=parse_indexed(
                data["mgrp"],
                MuteGroupCodec.decode,
            ),

            fx=parse_indexed(
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
            "ch": encode_indexed(obj.channels, FullChannelCodec.encode),
            "aux": encode_indexed(obj.aux_channels, AuxChannelCodec.encode),
            "bus": encode_indexed(obj.busses, BusChannelCodec.encode),
            "main": encode_indexed(obj.mains, MainChannelCodec.encode),
            "mtx": encode_indexed(obj.matrices, MatrixChannelCodec.encode),
            "dca": encode_indexed(obj.dcas, DCACodec.encode),
            "mgrp": encode_indexed(obj.mute_groups, MuteGroupCodec.encode),
            "fx": encode_indexed(obj.fx),

            "cards": ExpansionCardsCodec.encode(obj.expansion_cards),
            "play": PlaySettingsCodec.encode(obj.play_settings),
            "rec": RecordSettingsCodec.encode(obj.record_settings),
        }