from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.types.one_indexed_list import OneIndexedList


@dataclass_validate
@dataclass(kw_only=True)
class Output:
    input_group: str
    input_number: int


@dataclass_validate
@dataclass(kw_only=True)
class OutputBank:
    local_outputs: OneIndexedList[Output]
    aux_outputs: OneIndexedList[Output]
    aes50_a_outputs: OneIndexedList[Output]
    aes50_b_outputs: OneIndexedList[Output]
    aes50_c_outputs: OneIndexedList[Output]
    stageconnect_outputs: OneIndexedList[Output]
    usb_outputs: OneIndexedList[Output]
    expansion_card_outputs: OneIndexedList[Output]
    module_outputs: OneIndexedList[Output]
    usb_recording_outputs: OneIndexedList[Output]
    aes3_outputs: OneIndexedList[Output]