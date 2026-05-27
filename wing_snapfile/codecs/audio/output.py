from wing_snapfile.models.audio.output import Output, OutputBank
from wing_snapfile.helpers.indexed import encode_indexed, parse_indexed


class OutputCodec:
    @staticmethod
    def decode(data: dict) -> Output:
        return Output(
            input_group=data["grp"],
            input_number=data["in"],
        )

    @staticmethod
    def encode(obj: Output) -> dict:
        return {
            "grp": obj.input_group,
            "in": obj.input_number,
        }


class OutputBankCodec:
    @staticmethod
    def decode(data: dict) -> OutputBank:
        return OutputBank(
            local_outputs=parse_indexed(data["LCL"], OutputCodec.decode),
            aux_outputs=parse_indexed(data["AUX"], OutputCodec.decode),
            aes50_a_outputs=parse_indexed(data["A"], OutputCodec.decode),
            aes50_b_outputs=parse_indexed(data["B"], OutputCodec.decode),
            aes50_c_outputs=parse_indexed(data["C"], OutputCodec.decode),
            stageconnect_outputs=parse_indexed(data["SC"], OutputCodec.decode),
            usb_outputs=parse_indexed(data["USB"], OutputCodec.decode),
            expansion_card_outputs=parse_indexed(data["CRD"], OutputCodec.decode),
            module_outputs=parse_indexed(data["MOD"], OutputCodec.decode),
            usb_recording_outputs=parse_indexed(data["REC"], OutputCodec.decode),
            aes3_outputs=parse_indexed(data["AES"], OutputCodec.decode),
        )

    @staticmethod
    def encode(obj: OutputBank) -> dict:
        return {
            "LCL": encode_indexed(obj.local_outputs, OutputCodec.encode),
            "AUX": encode_indexed(obj.aux_outputs, OutputCodec.encode),
            "A": encode_indexed(obj.aes50_a_outputs, OutputCodec.encode),
            "B": encode_indexed(obj.aes50_b_outputs, OutputCodec.encode),
            "C": encode_indexed(obj.aes50_c_outputs, OutputCodec.encode),
            "SC": encode_indexed(obj.stageconnect_outputs, OutputCodec.encode),
            "USB": encode_indexed(obj.usb_outputs, OutputCodec.encode),
            "CRD": encode_indexed(obj.expansion_card_outputs, OutputCodec.encode),
            "MOD": encode_indexed(obj.module_outputs, OutputCodec.encode),
            "REC": encode_indexed(obj.usb_recording_outputs, OutputCodec.encode),
            "AES": encode_indexed(obj.aes3_outputs, OutputCodec.encode),
        }