import msgspec


class AudioInputSettings(msgspec.Struct, kw_only=True):
    is_phase_inverted: bool
    trim: float
    balance: float


class AudioSourceSwitchableDelayableInputSettings(msgspec.Struct, kw_only=True):
    is_phase_inverted: bool
    trim: float
    balance: float
    auto_source_switch: bool
    use_alternate_source: bool
    delay_mode: str
    delay_amount: float
    delay_on: bool