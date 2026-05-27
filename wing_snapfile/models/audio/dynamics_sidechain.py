from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate


@dataclass_validate
@dataclass(kw_only=True)
class DynamicsSidechain:
    type: str
    frequency: float
    q: float
    source: str
    tap: str
