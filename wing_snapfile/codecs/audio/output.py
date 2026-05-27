from wing_snapfile.models.audio.output import Output, OutputBank
from wing_snapfile.helpers.indexed import encode_one_indexed_list, decode_one_indexed_list


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
            local_outputs=decode_one_indexed_list(data["LCL"], OutputCodec.decode),
            aux_outputs=decode_one_indexed_list(data["AUX"], OutputCodec.decode),
            aes50_a_outputs=decode_one_indexed_list(data["A"], OutputCodec.decode),
            aes50_b_outputs=decode_one_indexed_list(data["B"], OutputCodec.decode),
            aes50_c_outputs=decode_one_indexed_list(data["C"], OutputCodec.decode),
            stageconnect_outputs=decode_one_indexed_list(data["SC"], OutputCodec.decode),
            usb_outputs=decode_one_indexed_list(data["USB"], OutputCodec.decode),
            expansion_card_outputs=decode_one_indexed_list(data["CRD"], OutputCodec.decode),
            module_outputs=decode_one_indexed_list(data["MOD"], OutputCodec.decode),
            usb_recording_outputs=decode_one_indexed_list(data["REC"], OutputCodec.decode),
            aes3_outputs=decode_one_indexed_list(data["AES"], OutputCodec.decode),
        )

    @staticmethod
    def encode(obj: OutputBank) -> dict:
        return {
            "LCL": encode_one_indexed_list(obj.local_outputs, OutputCodec.encode),
            "AUX": encode_one_indexed_list(obj.aux_outputs, OutputCodec.encode),
            "A": encode_one_indexed_list(obj.aes50_a_outputs, OutputCodec.encode),
            "B": encode_one_indexed_list(obj.aes50_b_outputs, OutputCodec.encode),
            "C": encode_one_indexed_list(obj.aes50_c_outputs, OutputCodec.encode),
            "SC": encode_one_indexed_list(obj.stageconnect_outputs, OutputCodec.encode),
            "USB": encode_one_indexed_list(obj.usb_outputs, OutputCodec.encode),
            "CRD": encode_one_indexed_list(obj.expansion_card_outputs, OutputCodec.encode),
            "MOD": encode_one_indexed_list(obj.module_outputs, OutputCodec.encode),
            "REC": encode_one_indexed_list(obj.usb_recording_outputs, OutputCodec.encode),
            "AES": encode_one_indexed_list(obj.aes3_outputs, OutputCodec.encode),
        }