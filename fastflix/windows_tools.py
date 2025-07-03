# -*- coding: utf-8 -*-
import logging

import reusables
from fastflix.language import t

logger = logging.getLogger("fastflix")

tool_window = None
tool_icon = None
CONTINUOUS = 0x80000000
SYSTEM_REQUIRED = 0x00000001


def prevent_sleep_mode():
    """https://msdn.microsoft.com/en-us/library/windows/desktop/aa373208(v=vs.85).aspx"""
    if reusables.win_based:
        import ctypes

        try:
            ctypes.windll.kernel32.SetThreadExecutionState(CONTINUOUS | SYSTEM_REQUIRED)
        except Exception:
            logger.exception(t("Could not prevent system from possibly going to sleep during conversion"))
        else:
            logger.debug(t("System has been asked to not sleep"))


def allow_sleep_mode():
    if reusables.win_based:
        import ctypes

        try:
            ctypes.windll.kernel32.SetThreadExecutionState(CONTINUOUS)
        except Exception:
            logger.exception(t("Could not allow system to resume sleep mode"))
        else:
            logger.debug(t("System has been allowed to enter sleep mode again"))
