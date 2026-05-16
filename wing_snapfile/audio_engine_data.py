# TODO: fx!

from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from .audio_engine_config import AudioEngineConfig
from .audio_engine_io import AudioEngineIo
from .audio_engine_channel import (
    AudioEngineAuxChannel,
    AudioEngineFullChannel,
    AudioEngineBusChannel,
    AudioEngineMainChannel,
    AudioEngineMatrixChannel,
)
from .audio_engine_dca import AudioEngineDCA
from .audio_engine_mute_group import AudioEngineMuteGroup
from .audio_engine_cards import AudioEngineCards
from .audio_engine_play_settings import AudioEnginePlaySettings
from .audio_engine_record_settings import AudioEngineRecordSettings
from .snapfile_reader import (
    _parse_json_object_list,
    JsonObject,
)
from .types import OneIndexedList


@dataclass_validate
@dataclass
class AudioEngineData:
    config: AudioEngineConfig
    io: AudioEngineIo
    channels: OneIndexedList[AudioEngineFullChannel]
    aux_channels: OneIndexedList[AudioEngineAuxChannel]
    busses: OneIndexedList[AudioEngineBusChannel]
    mains: OneIndexedList[AudioEngineMainChannel]
    matrices: OneIndexedList[AudioEngineMatrixChannel]
    dcas: OneIndexedList[AudioEngineDCA]
    mute_groups: OneIndexedList[AudioEngineMuteGroup]
    fx: list[JsonObject]
    cards: AudioEngineCards
    play_settings: AudioEnginePlaySettings
    record_settings: AudioEngineRecordSettings

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioEngineData":
        return AudioEngineData(
            config=AudioEngineConfig.from_dict(data["cfg"]),
            io=AudioEngineIo.from_dict(data["io"]),
            channels=OneIndexedList.from_indexed_dict(
                data["ch"], AudioEngineFullChannel.from_dict
            ),
            aux_channels=OneIndexedList.from_indexed_dict(
                data["aux"], AudioEngineAuxChannel.from_dict
            ),
            busses=OneIndexedList.from_indexed_dict(
                data["bus"], AudioEngineBusChannel.from_dict
            ),
            mains=OneIndexedList.from_indexed_dict(
                data["main"], AudioEngineMainChannel.from_dict
            ),
            matrices=OneIndexedList.from_indexed_dict(
                data["mtx"], AudioEngineMatrixChannel.from_dict
            ),
            dcas=OneIndexedList.from_indexed_dict(
                data["dca"], AudioEngineDCA.from_dict
            ),
            mute_groups=OneIndexedList.from_indexed_dict(
                data["mgrp"], AudioEngineMuteGroup.from_dict
            ),
            fx=_parse_json_object_list(data["fx"]),
            cards=AudioEngineCards.from_dict(data["cards"]),
            play_settings=AudioEnginePlaySettings.from_dict(data["play"]),
            record_settings=AudioEngineRecordSettings.from_dict(data["rec"]),
        )
