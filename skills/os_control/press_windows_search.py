# promptops/skills/os_control/press_windows_search.py
import pyautogui
from promptops.skills.base import BaseSkill

class WinSearchSkill(BaseSkill):
    name = "win_search"
    description = "Press Windows key, type query, and press Enter"
    
    async def run(self, query: str, **kwargs):
        pyautogui.press('win')
        pyautogui.write(query, interval=0.05)
        pyautogui.press('enter')
        return True
