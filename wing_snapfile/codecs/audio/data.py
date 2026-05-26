from wing_snapfile.models.audio.data import AudioData

from wing_snapfile.codecs.audio.config import AudioConfigCodec
from wing_snapfile.codecs.audio.io import AudioIoCodec

from wing_snapfile.codecs.audio.channel import (
    AudioFullChannelCodec,
    AudioAuxChannelCodec,
    AudioBusChannelCodec,
    AudioMainChannelCodec,
    AudioMatrixChannelCodec,
)

from wing_snapfile.codecs.audio.dca import AudioDCACodec
from wing_snapfile.codecs.audio.mute_group import AudioMuteGroupCodec
from wing_snapfile.codecs.audio.cards import AudioCardsCodec
from wing_snapfile.codecs.audio.play_settings import AudioPlaySettingsCodec
from wing_snapfile.codecs.audio.record_settings import AudioRecordSettingsCodec

from wing_snapfile.helpers.indexed import encode_indexed, parse_indexed


class AudioDataCodec:
    @staticmethod
    def decode(data: dict) -> AudioData:
        return AudioData(
            config=AudioConfigCodec.decode(data["cfg"]),
            io=AudioIoCodec.decode(data["io"]),

            channels=parse_indexed(
                data["ch"],
                AudioFullChannelCodec.decode,
            ),

            aux_channels=parse_indexed(
                data["aux"],
                AudioAuxChannelCodec.decode,
            ),

            busses=parse_indexed(
                data["bus"],
                AudioBusChannelCodec.decode,
            ),

            mains=parse_indexed(
                data["main"],
                AudioMainChannelCodec.decode,
            ),

            matrices=parse_indexed(
                data["mtx"],
                AudioMatrixChannelCodec.decode,
            ),

            dcas=parse_indexed(
                data["dca"],
                AudioDCACodec.decode,
            ),

            mute_groups=parse_indexed(
                data["mgrp"],
                AudioMuteGroupCodec.decode,
            ),

            fx=parse_indexed(
                data["fx"],
                lambda x: x,   # still raw dicts for now
            ),

            cards=AudioCardsCodec.decode(data["cards"]),
            play_settings=AudioPlaySettingsCodec.decode(data["play"]),
            record_settings=AudioRecordSettingsCodec.decode(data["rec"]),
        )

    @staticmethod
    def encode(obj: AudioData) -> dict:
        return {
            "cfg": AudioConfigCodec.encode(obj.config),
            "io": AudioIoCodec.encode(obj.io),
            "ch": encode_indexed(obj.channels, AudioFullChannelCodec.encode),
            "aux": encode_indexed(obj.aux_channels, AudioAuxChannelCodec.encode),
            "bus": encode_indexed(obj.busses, AudioBusChannelCodec.encode),
            "main": encode_indexed(obj.mains, AudioMainChannelCodec.encode),
            "mtx": encode_indexed(obj.matrices, AudioMatrixChannelCodec.encode),
            "dca": encode_indexed(obj.dcas, AudioDCACodec.encode),
            "mgrp": encode_indexed(obj.mute_groups, AudioMuteGroupCodec.encode),
            "fx": encode_indexed(obj.fx),

            "cards": AudioCardsCodec.encode(obj.cards),
            "play": AudioPlaySettingsCodec.encode(obj.play_settings),
            "rec": AudioRecordSettingsCodec.encode(obj.record_settings),
        }