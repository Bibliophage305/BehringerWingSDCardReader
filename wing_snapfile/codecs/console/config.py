from wing_snapfile.models.console.config import (
    ConsoleConfig,
    LightsConfig,
    RTAConfig,
)


class LightsConfigCodec:
    @staticmethod
    def decode(data: dict) -> LightsConfig:
        return LightsConfig(
            buttons_backlight_intensity=data["btns"],
            buttons_led_intensity=data["leds"],
            meters_intensity=data["meters"],
            color_led_intensity=data["rgbleds"],
            channel_lcd_intensity=data["chlcds"],
            channel_lcd_contrast=data["chlcdctr"],
            channel_strip_intensity=data["chedit"],
            touchscreen_intensity=data["main"],
            under_console_intensity=data["glow"],
            patch_panel_intensity=data["patch"],
            lamp_intensity=data["lamp"],
        )

    @staticmethod
    def encode(obj: LightsConfig) -> dict:
        return {
            "btns": obj.buttons_backlight_intensity,
            "leds": obj.buttons_led_intensity,
            "meters": obj.meters_intensity,
            "rgbleds": obj.color_led_intensity,
            "chlcds": obj.channel_lcd_intensity,
            "chlcdctr": obj.channel_lcd_contrast,
            "chedit": obj.channel_strip_intensity,
            "main": obj.touchscreen_intensity,
            "glow": obj.under_console_intensity,
            "patch": obj.patch_panel_intensity,
            "lamp": obj.lamp_intensity,
        }


class RTAConfigCodec:
    @staticmethod
    def decode(data: dict) -> RTAConfig:
        return RTAConfig(
            home_size_mode=data["homedisp"],
            home_color=data["homecol"],
            home_tap=data["hometap"],
            eq_size_mode=data["eqdisp"],
            eq_color=data["eqcol"],
            eq_tap=data["cheqtap"],
            channel_filter_tap=data["chflttap"],
        )

    @staticmethod
    def encode(obj: RTAConfig) -> dict:
        return {
            "homedisp": obj.home_size_mode,
            "homecol": obj.home_color,
            "hometap": obj.home_tap,
            "eqdisp": obj.eq_size_mode,
            "eqcol": obj.eq_color,
            "cheqtap": obj.eq_tap,
            "chflttap": obj.channel_filter_tap,
        }


class ConsoleConfigCodec:
    @staticmethod
    def decode(data: dict) -> ConsoleConfig:
        return ConsoleConfig(
            lights_config=LightsConfigCodec.decode(data["lights"]),
            rta_config=RTAConfigCodec.decode(data["rta"]),
            channel_mute_overrides_mute_group=data["muteovr"],
            exclusive_solo=data["soloexcl"],
            select_follows_solo=data["selfsolo"],
            solo_follows_select=data["solofsel"],
            bus_sends_on_fader_activates_solo=data["sof2solo"],
            send_page_activates_solo=data["sfdr2solo"],
            link_left_and_center_user_layers=data["layerlinkl"],
            link_right_and_center_user_layers=data["layerlinkr"],
            screen_follows_channel_strip=data["autoview"],
            channel_strip_touch_select=data["csctouch"],
            channel_auto_select_left=data["autosel_L"],
            channel_auto_select_center=data["autosel_C"],
            channel_auto_select_right=data["autosel_R"],
            compact_layer=data["autosel_CMPCT"],
            rack_layer=data["autosel_RCK"],
            external_layer=data["autosel_EXT"],
            virtual_layer=data["autosel_VRT"],
            wing_edit_layer=data["autosel_WEDIT"],
            full_fader_paging=data["fdrbanking"],
            fader_screen_link=data["fdrscrnlink"],
            sends_on_fader_faders=data["soffdr"],
            sends_on_fader_button_mode=data["sofbutton"],
            sends_on_fader_frame=data["sofframe"],
            alternative_sends_on_fader_mode=data["sofmode"],
            double_click_select_action=data["seldblclick"],
            user_button_mode=data["usrmode"],
            compact_main_fader=data["mfdr"],
            compact_main_fader_keep=data["mfdrkeep"],
            compact_buttons_mode=data["cscmode"],
            rack_channel_strip_mode=data["rackmode"],
            bus_spill_mode=data["busspill"],
            main_spill_mode=data["mainspill"],
            mtx_spill_mode=data["mtxspill"],
            dca_spill_mode=data["dcaspill"],
            compact_custom_control_buttons_activated=data["dcacc"],
            show_fader_value_on_scribble=data["showfdr"],
        )

    @staticmethod
    def encode(obj: ConsoleConfig) -> dict:
        return {
            "lights": LightsConfigCodec.encode(obj.lights_config),
            "rta": RTAConfigCodec.encode(obj.rta_config),
            "muteovr": obj.channel_mute_overrides_mute_group,
            "soloexcl": obj.exclusive_solo,
            "selfsolo": obj.select_follows_solo,
            "solofsel": obj.solo_follows_select,
            "sof2solo": obj.bus_sends_on_fader_activates_solo,
            "sfdr2solo": obj.send_page_activates_solo,
            "layerlinkl": obj.link_left_and_center_user_layers,
            "layerlinkr": obj.link_right_and_center_user_layers,
            "autoview": obj.screen_follows_channel_strip,
            "csctouch": obj.channel_strip_touch_select,
            "autosel_L": obj.channel_auto_select_left,
            "autosel_C": obj.channel_auto_select_center,
            "autosel_R": obj.channel_auto_select_right,
            "autosel_CMPCT": obj.compact_layer,
            "autosel_RCK": obj.rack_layer,
            "autosel_EXT": obj.external_layer,
            "autosel_VRT": obj.virtual_layer,
            "autosel_WEDIT": obj.wing_edit_layer,
            "fdrbanking": obj.full_fader_paging,
            "fdrscrnlink": obj.fader_screen_link,
            "soffdr": obj.sends_on_fader_faders,
            "sofbutton": obj.sends_on_fader_button_mode,
            "sofframe": obj.sends_on_fader_frame,
            "sofmode": obj.alternative_sends_on_fader_mode,
            "seldblclick": obj.double_click_select_action,
            "usrmode": obj.user_button_mode,
            "mfdr": obj.compact_main_fader,
            "mfdrkeep": obj.compact_main_fader_keep,
            "cscmode": obj.compact_buttons_mode,
            "rackmode": obj.rack_channel_strip_mode,
            "busspill": obj.bus_spill_mode,
            "mainspill": obj.main_spill_mode,
            "mtxspill": obj.mtx_spill_mode,
            "dcaspill": obj.dca_spill_mode,
            "dcacc": obj.compact_custom_control_buttons_activated,
            "showfdr": obj.show_fader_value_on_scribble,
        }
