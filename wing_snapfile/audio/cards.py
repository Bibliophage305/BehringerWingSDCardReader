from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.types import OneIndexedList


@dataclass_validate
@dataclass
class AudioWLiveCardSlotConfig:
    rectracks: int
    playmode: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            rectracks=int(data["rectracks"]),
            playmode=data["playmode"],
        )

    def to_dict(self):
        return {
            "rectracks": str(self.rectracks),
            "playmode": self.playmode,
        }


@dataclass_validate
@dataclass
class AudioWLiveCardSlot:
    config: AudioWLiveCardSlotConfig

    @classmethod
    def from_dict(cls, data: dict):
        return cls(config=AudioWLiveCardSlotConfig.from_dict(data["cfg"]))

    def to_dict(self):
        return {
            "cfg": self.config.to_dict(),
        }


@dataclass_validate
@dataclass
class AudioWLiveCard:
    sd_link_mode: str
    auto_input: str
    show_meters: bool
    auto_stop: str
    auto_play: str
    auto_record: str
    slots: OneIndexedList[AudioWLiveCardSlot]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            sd_link_mode=data["sdlink"],
            auto_input=data["autoin"],
            show_meters=data["meters"],
            auto_stop=data["auto_stop"],
            auto_play=data["auto_play"],
            auto_record=data["auto_rec"],
            slots=OneIndexedList.from_indexed_dict(
                {k: v for k, v in data.items() if k.isdigit()},
                AudioWLiveCardSlot.from_dict,
            ),
        )

    def to_dict(self):
        data = {
            "sdlink": self.sd_link_mode,
            "autoin": self.auto_input,
            "meters": self.show_meters,
            "auto_stop": self.auto_stop,
            "auto_play": self.auto_play,
            "auto_rec": self.auto_record,
            **self.slots.to_dict(),
        }
        return data


@dataclass_validate
@dataclass
class AudioWMADICard:
    mode: str
    rxclock: bool

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            mode=data["mode"],
            rxclock=data["rxclock"],
        )

    def to_dict(self):
        return {
            "mode": self.mode,
            "rxclock": self.rxclock,
        }


@dataclass_validate
@dataclass
class AudioCards:
    wlive_card: AudioWLiveCard
    wmadi_card: AudioWMADICard

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            wlive_card=AudioWLiveCard.from_dict(data["wlive"]),
            wmadi_card=AudioWMADICard.from_dict(data["wmadi"]),
        )

    def to_dict(self):
        return {
            "wlive": self.wlive_card.to_dict(),
            "wmadi": self.wmadi_card.to_dict(),
        }
