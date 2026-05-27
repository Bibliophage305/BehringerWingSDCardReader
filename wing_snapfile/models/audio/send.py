from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate


@dataclass_validate
@dataclass(kw_only=True)
class BaseSend:
    on: bool
    fader_level: float


@dataclass_validate
@dataclass(kw_only=True)
class Send(BaseSend):
    pre_fader: bool


@dataclass_validate
@dataclass(kw_only=True)
class FullSend(BaseSend):
    pre_always_on: bool
    mode: str
    pan_link: int
    pan: int
