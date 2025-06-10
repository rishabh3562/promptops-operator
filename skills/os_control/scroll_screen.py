# promptops/skills/os_control/submit.py
import pyautogui
from promptops.skills.base import BaseSkill

class Submit(BaseSkill):
    name = "submit"
    description = "Press Enter or click default Submit button"

    async def run(self, **kwargs):
        pyautogui.press('enter')
        return True
