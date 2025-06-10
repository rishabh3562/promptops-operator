from skills.base import BaseSkill
from pydantic import BaseModel
import pyautogui

class ScrollParams(BaseModel):
    clicks: int = 1  # Positive for up, negative for down
    x: int | None = None  # Optional x coordinate
    y: int | None = None  # Optional y coordinate

class ScrollSkill(BaseSkill):
    """
    Scrolls the screen up or down using pyautogui.
    Params:
        clicks: int (positive=up, negative=down)
        x, y: Optional coordinates to scroll at (default: current mouse position)
    """
    name = "scroll"
    description = "Scrolls the screen up or down."
    params_model = ScrollParams

    async def run(self, params: ScrollParams):
        # Optionally move mouse to (x, y) before scrolling
        if params.x is not None and params.y is not None:
            pyautogui.moveTo(params.x, params.y)
        pyautogui.scroll(params.clicks)
        return {"status": "scrolled", "clicks": params.clicks, "x": params.x, "y": params.y}
