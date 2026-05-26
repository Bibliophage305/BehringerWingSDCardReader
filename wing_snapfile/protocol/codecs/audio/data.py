from wing_snapfile.models.audio.data import AudioData

from wing_snapfile.protocol.codecs.audio.config import AudioConfigCodec
from wing_snapfile.protocol.codecs.audio.io import AudioIoCodec

from wing_snapfile.protocol.codecs.audio.channel import (
    AudioFullChannelCodec,
    AudioAuxChannelCodec,
    AudioBusChannelCodec,
    AudioMainChannelCodec,
    AudioMatrixChannelCodec,
)

from wing_snapfile.protocol.codecs.audio.dca import AudioDCACodec
from wing_snapfile.protocol.codecs.audio.mute_group import AudioMuteGroupCodec
from wing_snapfile.protocol.codecs.audio.cards import AudioCardsCodec
from wing_snapfile.protocol.codecs.audio.play_settings import AudioPlaySettingsCodec
from wing_snapfile.protocol.codecs.audio.record_settings import AudioRecordSettingsCodec

from wing_snapfile.protocol.helpers.indexed import parse_indexed


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

            "ch": obj.channels.to_dict(
                serializer=AudioFullChannelCodec.encode
            ),

            "aux": obj.aux_channels.to_dict(
                serializer=AudioAuxChannelCodec.encode
            ),

            "bus": obj.busses.to_dict(
                serializer=AudioBusChannelCodec.encode
            ),

            "main": obj.mains.to_dict(
                serializer=AudioMainChannelCodec.encode
            ),

            "mtx": obj.matrices.to_dict(
                serializer=AudioMatrixChannelCodec.encode
            ),

            "dca": obj.dcas.to_dict(
                serializer=AudioDCACodec.encode
            ),

            "mgrp": obj.mute_groups.to_dict(
                serializer=AudioMuteGroupCodec.encode
            ),

            "fx": obj.fx.to_dict(),

            "cards": AudioCardsCodec.encode(obj.cards),
            "play": AudioPlaySettingsCodec.encode(obj.play_settings),
            "rec": AudioRecordSettingsCodec.encode(obj.record_settings),
        }