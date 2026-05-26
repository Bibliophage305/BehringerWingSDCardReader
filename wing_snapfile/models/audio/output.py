import msgspec

from wing_snapfile.types.one_indexed_list import OneIndexedList


class AudioOutput(msgspec.Struct, kw_only=True):
    input_group: str
    input_number: int


class AudioOutputBank(msgspec.Struct, kw_only=True):
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