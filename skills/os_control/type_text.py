# promptops/skills/os_control/type_text.py
import pyautogui
from promptops.skills.base import BaseSkill

class TypeTextSkill(BaseSkill):
    name = "type_text"
    description = "Type given text at current focus"
    
    async def run(self, text: str, **kwargs):
        pyautogui.click()  # ensure focus
        pyautogui.write(text, interval=0.05)
        return True

# from promptops.skills.base import BaseSkill
# from typing import Optional
# import pyautogui

# class TypeTextSkill(BaseSkill):
#     name = "type_text"
#     description = "Types the given text using pyautogui."
#     parameters = {
#         "text": "str - The text to type."
#     }

#     async def run(self, text: str, context: Optional[dict] = None) -> bool:
#         pyautogui.write(text)
#         return True
