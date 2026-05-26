from wing_snapfile.models.audio.input_settings import (
    AudioInputSettings,
    AudioSourceSwitchableDelayableInputSettings,
)


class AudioInputSettingsCodec:
    @staticmethod
    def decode(data: dict) -> AudioInputSettings:
        return AudioInputSettings(
            is_phase_inverted=data["inv"],
            trim=float(data["trim"]),
            balance=float(data["bal"]),
        )

    @staticmethod
    def encode(obj: AudioInputSettings) -> dict:
        return {
            "inv": obj.is_phase_inverted,
            "trim": obj.trim,
            "bal": obj.balance,
        }


class AudioSourceSwitchableDelayableInputSettingsCodec:
    @staticmethod
    def decode(data: dict) -> AudioSourceSwitchableDelayableInputSettings:
        return AudioSourceSwitchableDelayableInputSettings(
            is_phase_inverted=data["inv"],
            trim=float(data["trim"]),
            balance=float(data["bal"]),
            auto_source_switch=data["srcauto"],
            use_alternate_source=data["altsrc"],
            delay_mode=data["dlymode"],
            delay_amount=float(data["dly"]),
            delay_on=data["dlyon"],
        )

    @staticmethod
    def encode(obj: AudioSourceSwitchableDelayableInputSettings) -> dict:
        return {
            "inv": obj.is_phase_inverted,
            "trim": obj.trim,
            "bal": obj.balance,
            "srcauto": obj.auto_source_switch,
            "altsrc": obj.use_alternate_source,
            "dlymode": obj.delay_mode,
            "dly": obj.delay_amount,
            "dlyon": obj.delay_on,
        }