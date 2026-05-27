from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.types.one_indexed_list import OneIndexedList


@dataclass_validate
@dataclass(kw_only=True)
class WLiveCardSlotConfig:
    rectracks: int
    playmode: str


@dataclass_validate
@dataclass(kw_only=True)
class WLiveCardSlot:
    config: WLiveCardSlotConfig


@dataclass_validate
@dataclass(kw_only=True)
class WLiveCard:
    sd_link_mode: str
    auto_input: str
    show_meters: bool

    auto_stop: str
    auto_play: str
    auto_record: str

    slots: OneIndexedList[WLiveCardSlot]


@dataclass_validate
@dataclass(kw_only=True)
class WMADICard:
    mode: str
    rxclock: bool


@dataclass_validate
@dataclass(kw_only=True)
class ExpansionCards:
    wlive_card: WLiveCard
    wmadi_card: WMADICard