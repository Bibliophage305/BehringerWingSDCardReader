from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate

@dataclass_validate
@dataclass(kw_only=True)
class LightsConfig:
    buttons_backlight_intensity: int
    buttons_led_intensity: int
    meters_intensity: int
    color_led_intensity: int
    channel_lcd_intensity: int
    channel_lcd_contrast: int
    channel_strip_intensity: int
    touchscreen_intensity: int
    under_console_intensity: int
    patch_panel_intensity: int
    lamp_intensity: int

@dataclass_validate
@dataclass(kw_only=True)
class RTAConfig:
    home_size_mode: str
    home_color: str
    home_tap: str
    eq_size_mode: str
    eq_color: str
    eq_tap: str
    channel_filter_tap: str

@dataclass_validate
@dataclass(kw_only=True)
class ConsoleConfig:
    lights_config: LightsConfig
    rta_config: RTAConfig
    channel_mute_overrides_mute_group: bool
    exclusive_solo: bool
    select_follows_solo: bool
    solo_follows_select: bool
    bus_sends_on_fader_activates_solo: bool
    send_page_activates_solo: bool
    link_left_and_center_user_layers: bool
    link_right_and_center_user_layers: bool
    screen_follows_channel_strip: bool
    channel_strip_touch_select: bool
    channel_auto_select_left: bool
    channel_auto_select_center: bool
    channel_auto_select_right: bool
    compact_layer: bool
    rack_layer: bool
    external_layer: bool
    virtual_layer: bool
    wing_edit_layer: bool
    full_fader_paging: bool
    fader_screen_link: bool
    sends_on_fader_faders: str
    sends_on_fader_button_mode: str
    sends_on_fader_frame: bool
    alternative_sends_on_fader_mode: bool
    double_click_select_action: str
    user_button_mode: str
    compact_main_fader: str
    compact_main_fader_keep: bool
    compact_buttons_mode: str
    rack_channel_strip_mode: str
    bus_spill_mode: bool
    main_spill_mode: bool
    mtx_spill_mode: bool
    dca_spill_mode: bool
    compact_custom_control_buttons_activated: bool
    show_fader_value_on_scribble: bool