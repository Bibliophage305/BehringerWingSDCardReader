from wing_snapfile.models.audio.output import AudioOutput, AudioOutputBank
from wing_snapfile.helpers.indexed import encode_indexed, parse_indexed


class AudioOutputCodec:
    @staticmethod
    def decode(data: dict) -> AudioOutput:
        return AudioOutput(
            input_group=data["grp"],
            input_number=data["in"],
        )

    @staticmethod
    def encode(obj: AudioOutput) -> dict:
        return {
            "grp": obj.input_group,
            "in": obj.input_number,
        }


class AudioOutputBankCodec:
    @staticmethod
    def decode(data: dict) -> AudioOutputBank:
        return AudioOutputBank(
            local_outputs=parse_indexed(data["LCL"], AudioOutputCodec.decode),
            aux_outputs=parse_indexed(data["AUX"], AudioOutputCodec.decode),
            aes50_a_outputs=parse_indexed(data["A"], AudioOutputCodec.decode),
            aes50_b_outputs=parse_indexed(data["B"], AudioOutputCodec.decode),
            aes50_c_outputs=parse_indexed(data["C"], AudioOutputCodec.decode),
            stageconnect_outputs=parse_indexed(data["SC"], AudioOutputCodec.decode),
            usb_outputs=parse_indexed(data["USB"], AudioOutputCodec.decode),
            expansion_card_outputs=parse_indexed(data["CRD"], AudioOutputCodec.decode),
            module_outputs=parse_indexed(data["MOD"], AudioOutputCodec.decode),
            usb_recording_outputs=parse_indexed(data["REC"], AudioOutputCodec.decode),
            aes3_outputs=parse_indexed(data["AES"], AudioOutputCodec.decode),
        )

    @staticmethod
    def encode(obj: AudioOutputBank) -> dict:
        return {
            "LCL": encode_indexed(obj.local_outputs, AudioOutputCodec.encode),
            "AUX": encode_indexed(obj.aux_outputs, AudioOutputCodec.encode),
            "A": encode_indexed(obj.aes50_a_outputs, AudioOutputCodec.encode),
            "B": encode_indexed(obj.aes50_b_outputs, AudioOutputCodec.encode),
            "C": encode_indexed(obj.aes50_c_outputs, AudioOutputCodec.encode),
            "SC": encode_indexed(obj.stageconnect_outputs, AudioOutputCodec.encode),
            "USB": encode_indexed(obj.usb_outputs, AudioOutputCodec.encode),
            "CRD": encode_indexed(obj.expansion_card_outputs, AudioOutputCodec.encode),
            "MOD": encode_indexed(obj.module_outputs, AudioOutputCodec.encode),
            "REC": encode_indexed(obj.usb_recording_outputs, AudioOutputCodec.encode),
            "AES": encode_indexed(obj.aes3_outputs, AudioOutputCodec.encode),
        }