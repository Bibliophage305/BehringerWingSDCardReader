from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from .types import OneIndexedList

@dataclass_validate
@dataclass
class AudioEngineWLiveCardSlotConfig:
    rectracks: int
    playmode: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            rectracks=int(data["rectracks"]),
            playmode=data["playmode"],
        )
    
@dataclass_validate
@dataclass
class AudioEngineWLiveCardSlot:
    config: AudioEngineWLiveCardSlotConfig

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            config=AudioEngineWLiveCardSlotConfig.from_dict(data["cfg"])
        )

@dataclass_validate
@dataclass
class AudioEngineWLiveCard:
    sd_link_mode: str
    auto_input: str
    show_meters: bool
    auto_stop: str
    auto_play: str
    auto_record: str
    slots: OneIndexedList[AudioEngineWLiveCardSlot]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            sd_link_mode=data["sdlink"],
            auto_input=data["autoin"],
            show_meters=data["meters"],
            auto_stop=data["auto_stop"],
            auto_play=data["auto_play"],
            auto_record=data["auto_rec"],
            slots=OneIndexedList.from_indexed_dict({k: v for k, v in data.items() if k.isdigit()}, AudioEngineWLiveCardSlot.from_dict),
        )
    
@dataclass_validate
@dataclass
class AudioEngineWMADICard:
    mode: str
    rxclock: bool

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            mode=data["mode"],
            rxclock=data["rxclock"],
        )

@dataclass_validate
@dataclass
class AudioEngineCards:
    wlive_card: AudioEngineWLiveCard
    wmadi_card: AudioEngineWMADICard

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            wlive_card=AudioEngineWLiveCard.from_dict(data["wlive"]),
            wmadi_card=AudioEngineWMADICard.from_dict(data["wmadi"]),
        )