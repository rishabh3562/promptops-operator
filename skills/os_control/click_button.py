# promptops/skills/os_control/click_button.py
import pyautogui
import pytesseract
from PIL import Image

from promptops.skills.base import BaseSkill

class ClickButtonSkill(BaseSkill):
    name = "click_button"
    description = "Find and click a button by its visible label"
    
    async def run(self, text: str, **kwargs):
        # 1) screenshot
        img = pyautogui.screenshot()
        # 2) OCR for all words with boxes
        data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
        # 3) find matching word
        for i, word in enumerate(data["text"]):
            if word.strip().lower() == text.lower():
                x = data["left"][i] + data["width"][i] // 2
                y = data["top"][i]  + data["height"][i] // 2
                pyautogui.moveTo(x, y, duration=0.2)
                pyautogui.click()
                return True
        print(f"[ClickButtonSkill] '{text}' not found on screen.")
        return False

# from promptops.skills.base import BaseSkill
# from typing import Optional

# class ClickButtonSkill(BaseSkill):
#     """
#     Skill to click a button on the screen by label.
#     """
#     name = "click_button"
#     description = "Clicks a button on the screen with the given label using OCR and pyautogui."
#     parameters = {
#         "button_label": "str - The visible text label of the button to click."
#     }

#     async def run(self, button_label: str, context: Optional[dict] = None) -> bool:
#         """
#         Find and click the button with the given label using OCR and pyautogui.
#         Includes logging and basic retry logic.
#         """
#         import pyautogui
#         from vision import screen_analyzer
#         from dispatcher import trace_logger
#         import asyncio

#         trace_logger.log_event(
#             event_type="skill_execution_start",
#             details={
#                 "skill": self.name,
#                 "button_label": button_label,
#                 "context": context
#             }
#         )

#         max_retries = 2
#         for attempt in range(max_retries):
#             coords = await screen_analyzer.find_button_coordinates(button_label)
#             if coords:
#                 pyautogui.moveTo(coords[0], coords[1], duration=0.2)
#                 pyautogui.click()
#                 trace_logger.log_event(
#                     event_type="skill_execution_success",
#                     details={
#                         "skill": self.name,
#                         "button_label": button_label,
#                         "coords": coords,
#                         "attempt": attempt + 1
#                     }
#                 )
#                 return True
#             await asyncio.sleep(0.5)  # Small delay before retry

#         trace_logger.log_event(
#             event_type="skill_execution_failure",
#             details={
#                 "skill": self.name,
#                 "button_label": button_label,
#                 "reason": "Button not found after retries"
#             }
#         )
#         return False
