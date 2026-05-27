from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate


@dataclass_validate
@dataclass(kw_only=True)
class DynamicsCrossover:
    depth: int
    type: str
    frequency: float
    q: float