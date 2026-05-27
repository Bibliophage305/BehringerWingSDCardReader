from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate


@dataclass_validate
@dataclass(kw_only=True)
class PostInsertBlock:
    on: bool
    insert: str


@dataclass_validate
@dataclass(kw_only=True)
class PostInsertBlockWithAutomix(PostInsertBlock):
    mode: str
    autogain_weight: float
