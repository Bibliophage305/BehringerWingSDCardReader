from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

from wing_snapfile.types import OneIndexedList

@dataclass_validate
@dataclass
class AudioOutput:
    input_group: str
    input_number: int

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioOutput":
        return AudioOutput(
            input_group=data["grp"],
            input_number=data["in"],
        )


@dataclass_validate
@dataclass
class AudioOutputBank:
    local_outputs: OneIndexedList[AudioOutput]
    aux_outputs: OneIndexedList[AudioOutput]
    aes50_a_outputs: OneIndexedList[AudioOutput]
    aes50_b_outputs: OneIndexedList[AudioOutput]
    aes50_c_outputs: OneIndexedList[AudioOutput]
    stageconnect_outputs: OneIndexedList[AudioOutput]
    usb_outputs: OneIndexedList[AudioOutput]
    expansion_card_outputs: OneIndexedList[AudioOutput]
    module_outputs: OneIndexedList[AudioOutput]
    usb_recording_outputs: OneIndexedList[AudioOutput]
    aes3_outputs: OneIndexedList[AudioOutput]

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AudioOutputBank":
        return cls(
            local_outputs=OneIndexedList.from_indexed_dict(
                data["LCL"], AudioOutput.from_dict
            ),
            aux_outputs=OneIndexedList.from_indexed_dict(
                data["AUX"], AudioOutput.from_dict
            ),
            aes50_a_outputs=OneIndexedList.from_indexed_dict(
                data["A"], AudioOutput.from_dict
            ),
            aes50_b_outputs=OneIndexedList.from_indexed_dict(
                data["B"], AudioOutput.from_dict
            ),
            aes50_c_outputs=OneIndexedList.from_indexed_dict(
                data["C"], AudioOutput.from_dict
            ),
            stageconnect_outputs=OneIndexedList.from_indexed_dict(
                data["SC"], AudioOutput.from_dict
            ),
            usb_outputs=OneIndexedList.from_indexed_dict(
                data["USB"], AudioOutput.from_dict
            ),
            expansion_card_outputs=OneIndexedList.from_indexed_dict(
                data["CRD"], AudioOutput.from_dict
            ),
            module_outputs=OneIndexedList.from_indexed_dict(
                data["MOD"], AudioOutput.from_dict
            ),
            usb_recording_outputs=OneIndexedList.from_indexed_dict(
                data["REC"], AudioOutput.from_dict
            ),
            aes3_outputs=OneIndexedList.from_indexed_dict(
                data["AES"], AudioOutput.from_dict
            ),
        )
