from enum import Enum
from typing import Self


class Actions(Enum):
    """
    Lifted from https://github.com/NUIKit/CGSInternal/blob/master/CGSHotKeys.h#L38
    which probably is out of date
    """

    # fmt: off
    kCGSHotKeyToggleFullKeyboardAccess = 12
    kCGSHotKeyFocusMenubar = 7
    kCGSHotKeyFocusDock = 8
    kCGSHotKeyFocusNextGlobalWindow = 9
    kCGSHotKeyFocusToolbar = 10
    kCGSHotKeyFocusFloatingWindow = 11
    kCGSHotKeyFocusApplicationWindow = 27
    kCGSHotKeyFocusNextControl = 13
    kCGSHotKeyFocusDrawer = 51
    kCGSHotKeyFocusStatusItems = 57

    # screenshot hotkeys
    kCGSHotKeyScreenshot = 28
    kCGSHotKeyScreenshotToClipboard = 29
    kCGSHotKeyScreenshotRegion = 30
    kCGSHotKeyScreenshotRegionToClipboard = 31
    screenshot_and_recording_options = 184

    # universal access
    kCGSHotKeyToggleZoom = 15
    kCGSHotKeyZoomOut = 19
    kCGSHotKeyZoomIn = 17
    kCGSHotKeyZoomToggleSmoothing = 23
    kCGSHotKeyIncreaseContrast = 25
    kCGSHotKeyDecreaseContrast = 26
    kCGSHotKeyInvertScreen = 21
    kCGSHotKeyToggleVoiceOver = 59

    # Dock
    kCGSHotKeyToggleDockAutohide = 52
    kCGSHotKeyExposeAllWindows = 32
    kCGSHotKeyExposeAllWindowsSlow = 34
    kCGSHotKeyExposeApplicationWindows = 33
    kCGSHotKeyExposeApplicationWindowsSlow = 35
    kCGSHotKeyExposeDesktop = 36
    kCGSHotKeyExposeDesktopsSlow = 37
    kCGSHotKeyDashboard = 62
    kCGSHotKeyDashboardSlow = 63

    # spaces (Leopard and later)
    kCGSHotKeySpaces = 75
    kCGSHotKeySpacesSlow = 76
    # 77 - fn F7 (disabled)
    # 78 - ⇧fn F7 (disabled)
    kCGSHotKeySpaceLeft = 79
    kCGSHotKeySpaceLeftSlow = 80
    kCGSHotKeySpaceRight = 81
    kCGSHotKeySpaceRightSlow = 82
    kCGSHotKeySpaceDown = 83
    kCGSHotKeySpaceDownSlow = 84
    kCGSHotKeySpaceUp = 85
    kCGSHotKeySpaceUpSlow = 86

    # input
    kCGSHotKeyToggleCharacterPallette = 50
    kCGSHotKeySelectPreviousInputSource = 60
    kCGSHotKeySelectNextInputSource = 61

    # Spotlight
    kCGSHotKeySpotlightSearchField = 64
    kCGSHotKeySpotlightWindow = 65

    kCGSHotKeyToggleFrontRow = 73
    kCGSHotKeyLookUpWordInDictionary = 70
    kCGSHotKeyHelp = 98

    # displays - not verified
    kCGSHotKeyDecreaseDisplayBrightness = 53
    kCGSHotKeyIncreaseDisplayBrightness = 54
    # fmt: on

    @classmethod
    def get_by_value(cls, action_number: int | str) -> Self | None:
        if match := list(filter(lambda a: str(a.value) == str(action_number), Actions)):
            return match[0]
        else:
            return None
