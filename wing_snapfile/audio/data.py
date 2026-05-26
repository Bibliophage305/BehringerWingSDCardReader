# TODO: fx!

from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from wing_snapfile.audio.config import AudioConfig
from wing_snapfile.audio.io import AudioIo
from wing_snapfile.audio.channel import (
    AudioAuxChannel,
    AudioFullChannel,
    AudioBusChannel,
    AudioMainChannel,
    AudioMatrixChannel,
)
from wing_snapfile.audio.dca import AudioDCA
from wing_snapfile.audio.mute_group import AudioMuteGroup
from wing_snapfile.audio.cards import AudioCards
from wing_snapfile.audio.play_settings import AudioPlaySettings
from wing_snapfile.audio.record_settings import AudioRecordSettings
from wing_snapfile.types import OneIndexedList


@dataclass_validate
@dataclass
class AudioData:
    config: AudioConfig
    io: AudioIo
    channels: OneIndexedList[AudioFullChannel]
    aux_channels: OneIndexedList[AudioAuxChannel]
    busses: OneIndexedList[AudioBusChannel]
    mains: OneIndexedList[AudioMainChannel]
    matrices: OneIndexedList[AudioMatrixChannel]
    dcas: OneIndexedList[AudioDCA]
    mute_groups: OneIndexedList[AudioMuteGroup]
    fx: OneIndexedList[dict]
    cards: AudioCards
    play_settings: AudioPlaySettings
    record_settings: AudioRecordSettings

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioData":
        return AudioData(
            config=AudioConfig.from_dict(data["cfg"]),
            io=AudioIo.from_dict(data["io"]),
            channels=OneIndexedList.from_indexed_dict(
                data["ch"], AudioFullChannel.from_dict
            ),
            aux_channels=OneIndexedList.from_indexed_dict(
                data["aux"], AudioAuxChannel.from_dict
            ),
            busses=OneIndexedList.from_indexed_dict(
                data["bus"], AudioBusChannel.from_dict
            ),
            mains=OneIndexedList.from_indexed_dict(
                data["main"], AudioMainChannel.from_dict
            ),
            matrices=OneIndexedList.from_indexed_dict(
                data["mtx"], AudioMatrixChannel.from_dict
            ),
            dcas=OneIndexedList.from_indexed_dict(data["dca"], AudioDCA.from_dict),
            mute_groups=OneIndexedList.from_indexed_dict(
                data["mgrp"], AudioMuteGroup.from_dict
            ),
            fx=OneIndexedList.from_indexed_dict(data["fx"]),
            cards=AudioCards.from_dict(data["cards"]),
            play_settings=AudioPlaySettings.from_dict(data["play"]),
            record_settings=AudioRecordSettings.from_dict(data["rec"]),
        )

    def to_dict(self):
        return {
            "cfg": self.config.to_dict(),
            "io": self.io.to_dict(),
            "ch": self.channels.to_dict(),
            "aux": self.aux_channels.to_dict(),
            "bus": self.busses.to_dict(),
            "main": self.mains.to_dict(),
            "mtx": self.matrices.to_dict(),
            "dca": self.dcas.to_dict(),
            "mgrp": self.mute_groups.to_dict(),
            "fx": self.fx.to_dict(),
            "cards": self.cards.to_dict(),
            "play": self.play_settings.to_dict(),
            "rec": self.record_settings.to_dict(),
        }
