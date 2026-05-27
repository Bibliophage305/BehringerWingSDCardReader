from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.models.audio.source import SourceBank
from wing_snapfile.models.audio.output import OutputBank


@dataclass_validate
@dataclass(kw_only=True)
class IO:
    sources: SourceBank
    outputs: OutputBank

    alternate_inputs: bool
    global_input_select_override: bool