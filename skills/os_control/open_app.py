# promptops/skills/os_control/open_app.py
import os, subprocess, sys
import pyautogui
from promptops.skills.base import BaseSkill
from promptops.skills.os_control.press_windows_search import WinSearchSkill  # reuse search

class Open_app(BaseSkill):
    """
    Launch an application on Windows.
    Strategy:
    1. If a known absolute path exists → Popen it.
    2. Else, press Win‑key and type the query, Enter.
    """
    name = "open_app"
    description = "Launch an application by name"

    # Common install paths (add more as you need)
    KNOWN_PATHS = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "discord": r"%LOCALAPPDATA%\Discord\Update.exe --processStart Discord.exe",
        "vs code": r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe",
        "telegram": r"%LOCALAPPDATA%\Programs\Telegram Desktop\Telegram.exe",
        "notepad": r"C:\Windows\System32\notepad.exe",
    }

    async def run(self, text: str, **kwargs):
        query = text.lower().strip()
        path  = self.KNOWN_PATHS.get(query)
        if path:
            path = os.path.expandvars(path)
            if os.path.exists(path.split()[0]):
                subprocess.Popen(path.split(), shell=False)
                return True

        # Fallback → WinSearch
        return await WinSearchSkill().run(query)
