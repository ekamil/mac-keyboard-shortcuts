from enum import Enum
from typing import Self

from mac_keyboard_shortcuts.types.key import Key


class KeysEnum(Enum):
    # fmt: off
    KEY_0 = Key(label='0', character='0', ascii_code=48, mac_key_code=29, layout_dependence='ANSI-US')
    KEY_1 = Key(label='1', character='1', ascii_code=49, mac_key_code=18, layout_dependence='ANSI-US')
    KEY_2 = Key(label='2', character='2', ascii_code=50, mac_key_code=19, layout_dependence='ANSI-US')
    KEY_3 = Key(label='3', character='3', ascii_code=51, mac_key_code=20, layout_dependence='ANSI-US')
    KEY_4 = Key(label='4', character='4', ascii_code=52, mac_key_code=21, layout_dependence='ANSI-US')
    KEY_5 = Key(label='5', character='5', ascii_code=53, mac_key_code=23, layout_dependence='ANSI-US')
    KEY_6 = Key(label='6', character='6', ascii_code=54, mac_key_code=22, layout_dependence='ANSI-US')
    KEY_7 = Key(label='7', character='7', ascii_code=55, mac_key_code=26, layout_dependence='ANSI-US')
    KEY_8 = Key(label='8', character='8', ascii_code=56, mac_key_code=28, layout_dependence='ANSI-US')
    KEY_9 = Key(label='9', character='9', ascii_code=57, mac_key_code=25, layout_dependence='ANSI-US')
    KEY_A = Key(label='A', character='a', ascii_code=97, mac_key_code=0, layout_dependence='ANSI-US')
    KEY_B = Key(label='B', character='b', ascii_code=98, mac_key_code=11, layout_dependence='ANSI-US')
    KEY_C = Key(label='C', character='c', ascii_code=99, mac_key_code=8, layout_dependence='ANSI-US')
    KEY_D = Key(label='D', character='d', ascii_code=100, mac_key_code=2, layout_dependence='ANSI-US')
    KEY_E = Key(label='E', character='e', ascii_code=101, mac_key_code=14, layout_dependence='ANSI-US')
    KEY_F = Key(label='F', character='f', ascii_code=102, mac_key_code=3, layout_dependence='ANSI-US')
    KEY_G = Key(label='G', character='g', ascii_code=103, mac_key_code=5, layout_dependence='ANSI-US')
    KEY_H = Key(label='H', character='h', ascii_code=104, mac_key_code=4, layout_dependence='ANSI-US')
    KEY_I = Key(label='I', character='i', ascii_code=105, mac_key_code=34, layout_dependence='ANSI-US')
    KEY_J = Key(label='J', character='j', ascii_code=106, mac_key_code=38, layout_dependence='ANSI-US')
    KEY_K = Key(label='K', character='k', ascii_code=107, mac_key_code=40, layout_dependence='ANSI-US')
    KEY_L = Key(label='L', character='l', ascii_code=108, mac_key_code=37, layout_dependence='ANSI-US')
    KEY_M = Key(label='M', character='m', ascii_code=109, mac_key_code=46, layout_dependence='ANSI-US')
    KEY_N = Key(label='N', character='n', ascii_code=110, mac_key_code=45, layout_dependence='ANSI-US')
    KEY_O = Key(label='O', character='o', ascii_code=111, mac_key_code=31, layout_dependence='ANSI-US')
    KEY_P = Key(label='P', character='p', ascii_code=112, mac_key_code=35, layout_dependence='ANSI-US')
    KEY_Q = Key(label='Q', character='q', ascii_code=113, mac_key_code=12, layout_dependence='ANSI-US')
    KEY_R = Key(label='R', character='r', ascii_code=114, mac_key_code=15, layout_dependence='ANSI-US')
    KEY_S = Key(label='S', character='s', ascii_code=115, mac_key_code=1, layout_dependence='ANSI-US')
    KEY_T = Key(label='T', character='t', ascii_code=116, mac_key_code=17, layout_dependence='ANSI-US')
    KEY_U = Key(label='U', character='u', ascii_code=117, mac_key_code=32, layout_dependence='ANSI-US')
    KEY_V = Key(label='V', character='v', ascii_code=118, mac_key_code=9, layout_dependence='ANSI-US')
    KEY_W = Key(label='W', character='w', ascii_code=119, mac_key_code=13, layout_dependence='ANSI-US')
    KEY_X = Key(label='X', character='x', ascii_code=120, mac_key_code=7, layout_dependence='ANSI-US')
    KEY_Y = Key(label='Y', character='y', ascii_code=121, mac_key_code=16, layout_dependence='ANSI-US')
    KEY_Z = Key(label='Z', character='z', ascii_code=122, mac_key_code=6, layout_dependence='ANSI-US')
    KEY_F1 = Key(label='F1', character='', ascii_code=65535, mac_key_code=122, layout_dependence='Independent')
    KEY_F2 = Key(label='F2', character='', ascii_code=65535, mac_key_code=120, layout_dependence='Independent')
    KEY_F3 = Key(label='F3', character='', ascii_code=65535, mac_key_code=99, layout_dependence='Independent')
    KEY_F4 = Key(label='F4', character='', ascii_code=65535, mac_key_code=118, layout_dependence='Independent')
    KEY_F5 = Key(label='F5', character='', ascii_code=65535, mac_key_code=96, layout_dependence='Independent')
    KEY_F6 = Key(label='F6', character='', ascii_code=65535, mac_key_code=97, layout_dependence='Independent')
    KEY_F7 = Key(label='F7', character='', ascii_code=65535, mac_key_code=98, layout_dependence='Independent')
    KEY_F8 = Key(label='F8', character='', ascii_code=65535, mac_key_code=100, layout_dependence='Independent')
    KEY_F9 = Key(label='F9', character='', ascii_code=65535, mac_key_code=101, layout_dependence='Independent')
    KEY_F10 = Key(label='F10', character='', ascii_code=65535, mac_key_code=109, layout_dependence='Independent')
    KEY_F11 = Key(label='F11', character='', ascii_code=65535, mac_key_code=103, layout_dependence='Independent')
    KEY_F12 = Key(label='F12', character='', ascii_code=65535, mac_key_code=111, layout_dependence='Independent')
    KEY_F13 = Key(label='F13', character='', ascii_code=65535, mac_key_code=105, layout_dependence='Independent')
    KEY_F14 = Key(label='F14', character='', ascii_code=65535, mac_key_code=107, layout_dependence='Independent')
    KEY_F15 = Key(label='F15', character='', ascii_code=65535, mac_key_code=113, layout_dependence='Independent')
    KEY_F16 = Key(label='F16', character='', ascii_code=65535, mac_key_code=106, layout_dependence='Independent')
    KEY_F17 = Key(label='F17', character='', ascii_code=65535, mac_key_code=64, layout_dependence='Independent')
    KEY_F18 = Key(label='F18', character='', ascii_code=65535, mac_key_code=79, layout_dependence='Independent')
    KEY_F19 = Key(label='F19', character='', ascii_code=65535, mac_key_code=80, layout_dependence='Independent')
    KEY_F20 = Key(label='F20', character='', ascii_code=65535, mac_key_code=90, layout_dependence='Independent')
    KEY_KEYPAD0 = Key(label='Keypad0', character='', ascii_code=65535, mac_key_code=82, layout_dependence='ANSI-US')
    KEY_KEYPAD1 = Key(label='Keypad1', character='', ascii_code=65535, mac_key_code=83, layout_dependence='ANSI-US')
    KEY_KEYPAD2 = Key(label='Keypad2', character='', ascii_code=65535, mac_key_code=84, layout_dependence='ANSI-US')
    KEY_KEYPAD3 = Key(label='Keypad3', character='', ascii_code=65535, mac_key_code=85, layout_dependence='ANSI-US')
    KEY_KEYPAD4 = Key(label='Keypad4', character='', ascii_code=65535, mac_key_code=86, layout_dependence='ANSI-US')
    KEY_KEYPAD5 = Key(label='Keypad5', character='', ascii_code=65535, mac_key_code=87, layout_dependence='ANSI-US')
    KEY_KEYPAD6 = Key(label='Keypad6', character='', ascii_code=65535, mac_key_code=88, layout_dependence='ANSI-US')
    KEY_KEYPAD7 = Key(label='Keypad7', character='', ascii_code=65535, mac_key_code=89, layout_dependence='ANSI-US')
    KEY_KEYPAD8 = Key(label='Keypad8', character='', ascii_code=65535, mac_key_code=91, layout_dependence='ANSI-US')
    KEY_KEYPAD9 = Key(label='Keypad9', character='', ascii_code=65535, mac_key_code=92, layout_dependence='ANSI-US')
    KEY_KEYPADCLEAR = Key(label='KeypadClear', character='', ascii_code=65535, mac_key_code=71,
                          layout_dependence='ANSI-US')
    KEY_KEYPADDECIMAL = Key(label='KeypadDecimal', character='', ascii_code=65535, mac_key_code=65,
                            layout_dependence='ANSI-US')
    KEY_KEYPADDIVIDE = Key(label='KeypadDivide', character='', ascii_code=65535, mac_key_code=75,
                           layout_dependence='ANSI-US')
    KEY_KEYPADENTER = Key(label='KeypadEnter', character='', ascii_code=65535, mac_key_code=76,
                          layout_dependence='ANSI-US')
    KEY_KEYPADEQUALS = Key(label='KeypadEquals', character='', ascii_code=65535, mac_key_code=81,
                           layout_dependence='ANSI-US')
    KEY_KEYPADMINUS = Key(label='KeypadMinus', character='', ascii_code=65535, mac_key_code=78,
                          layout_dependence='ANSI-US')
    KEY_KEYPADMULTIPLY = Key(label='KeypadMultiply', character='', ascii_code=65535, mac_key_code=67,
                             layout_dependence='ANSI-US')
    KEY_KEYPADPLUS = Key(label='KeypadPlus', character='', ascii_code=65535, mac_key_code=69,
                         layout_dependence='ANSI-US')
    KEY_BACKSLASH = Key(label='Backslash', character='\\', ascii_code=92, mac_key_code=42, layout_dependence='ANSI-US')
    KEY_CAPSLOCK = Key(label='CapsLock', character='', ascii_code=65535, mac_key_code=57,
                       layout_dependence='Independent')
    KEY_COMMA = Key(label='Comma', character=',', ascii_code=44, mac_key_code=43, layout_dependence='ANSI-US')
    KEY_COMMAND = Key(label='Command', character='', ascii_code=65535, mac_key_code=55, layout_dependence='Independent')
    KEY_CONTROL = Key(label='Control', character='', ascii_code=65535, mac_key_code=59, layout_dependence='Independent')
    KEY_DELETE = Key(label='Delete', character='\x7f', ascii_code=65535, mac_key_code=51,
                     layout_dependence='Independent')
    KEY_DOWNARROW = Key(label='DownArrow', character='', ascii_code=65535, mac_key_code=125,
                        layout_dependence='Independent')
    KEY_END = Key(label='End', character='', ascii_code=65535, mac_key_code=119, layout_dependence='Independent')
    KEY_EQUAL = Key(label='Equal', character='=', ascii_code=61, mac_key_code=24, layout_dependence='ANSI-US')
    KEY_ESCAPE = Key(label='Escape', character='\x1b', ascii_code=27, mac_key_code=53, layout_dependence='Independent')
    KEY_FORWARDDELETE = Key(label='ForwardDelete', character='', ascii_code=65535, mac_key_code=117,
                            layout_dependence='Independent')
    KEY_FUNCTION = Key(label='Function', character='', ascii_code=65535, mac_key_code=63,
                       layout_dependence='Independent')
    KEY_GRAVE = Key(label='Grave', character='`', ascii_code=96, mac_key_code=50, layout_dependence='ANSI-US')
    KEY_HELP = Key(label='Help', character='', ascii_code=65535, mac_key_code=114, layout_dependence='Independent')
    KEY_HOME = Key(label='Home', character='', ascii_code=65535, mac_key_code=115, layout_dependence='Independent')
    KEY_LEFTARROW = Key(label='LeftArrow', character='', ascii_code=65535, mac_key_code=123,
                        layout_dependence='Independent')
    KEY_LEFTBRACKET = Key(label='LeftBracket', character='[', ascii_code=91, mac_key_code=33,
                          layout_dependence='ANSI-US')
    KEY_MINUS = Key(label='Minus', character='-', ascii_code=45, mac_key_code=27, layout_dependence='ANSI-US')
    KEY_MUTE = Key(label='Mute', character='', ascii_code=65535, mac_key_code=74, layout_dependence='Independent')
    KEY_OPTION = Key(label='Option', character='', ascii_code=65535, mac_key_code=58, layout_dependence='Independent')
    KEY_PAGEDOWN = Key(label='PageDown', character='', ascii_code=65535, mac_key_code=121,
                       layout_dependence='Independent')
    KEY_PAGEUP = Key(label='PageUp', character='', ascii_code=65535, mac_key_code=116, layout_dependence='Independent')
    KEY_PERIOD = Key(label='Period', character='.', ascii_code=46, mac_key_code=47, layout_dependence='ANSI-US')
    KEY_QUOTE = Key(label='Quote', character="'", ascii_code=39, mac_key_code=39, layout_dependence='ANSI-US')
    KEY_RETURN = Key(label='Return', character='', ascii_code=65535, mac_key_code=36, layout_dependence='Independent')
    KEY_RIGHTARROW = Key(label='RightArrow', character='', ascii_code=65535, mac_key_code=124,
                         layout_dependence='Independent')
    KEY_RIGHTBRACKET = Key(label='RightBracket', character=']', ascii_code=93, mac_key_code=30,
                           layout_dependence='ANSI-US')
    KEY_RIGHTCOMMAND = Key(label='RightCommand', character='', ascii_code=65535, mac_key_code=54,
                           layout_dependence='Independent')
    KEY_RIGHTCONTROL = Key(label='RightControl', character='', ascii_code=65535, mac_key_code=62,
                           layout_dependence='Independent')
    KEY_RIGHTOPTION = Key(label='RightOption', character='', ascii_code=65535, mac_key_code=61,
                          layout_dependence='Independent')
    KEY_RIGHTSHIFT = Key(label='RightShift', character='', ascii_code=65535, mac_key_code=60,
                         layout_dependence='Independent')
    KEY_SEMICOLON = Key(label='Semicolon', character=';', ascii_code=59, mac_key_code=41, layout_dependence='ANSI-US')
    KEY_SHIFT = Key(label='Shift', character='', ascii_code=65535, mac_key_code=56, layout_dependence='Independent')
    KEY_SLASH = Key(label='Slash', character='/', ascii_code=47, mac_key_code=44, layout_dependence='ANSI-US')
    KEY_SPACE = Key(label='Space', character=' ', ascii_code=32, mac_key_code=49, layout_dependence='Independent')
    KEY_TAB = Key(label='Tab', character='\t', ascii_code=9, mac_key_code=48, layout_dependence='Independent')
    KEY_UPARROW = Key(label='UpArrow', character='', ascii_code=65535, mac_key_code=126,
                      layout_dependence='Independent')
    KEY_VOLUMEDOWN = Key(label='VolumeDown', character='', ascii_code=65535, mac_key_code=73,
                         layout_dependence='Independent')
    KEY_VOLUMEUP = Key(label='VolumeUp', character='', ascii_code=65535, mac_key_code=72,
                       layout_dependence='Independent')

    # fmt: on

    @classmethod
    def find_key_by_mac_key_code(cls, mac_key_code) -> Self | None:
        if matched := list(
            filter(lambda ke: ke.value.mac_key_code == int(mac_key_code), KeysEnum)
        ):
            return matched[0].value
        else:
            return None
