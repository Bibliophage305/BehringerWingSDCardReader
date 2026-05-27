from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate


@dataclass_validate
@dataclass(kw_only=True)
class PlaySettings:
    repeat: bool
