# promptops/skills/os_control/launch_app.py
import os, subprocess
from promptops.skills.base import BaseSkill

class LaunchAppSkill(BaseSkill):
    name = "launch_app"
    description = "Launch an application via known paths or WinSearch"
    
    async def run(self, app_name: str, **kwargs):
        common_paths = {
            "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            "discord": r"C:\Users\%USERNAME%\AppData\Local\Discord\Update.exe --processStart Discord.exe",
            # add more...
        }
        path = common_paths.get(app_name.lower())
        if path:
            path = os.path.expandvars(path)
            if os.path.exists(path):
                subprocess.Popen(path.split())
                return True
        # fallback to WinSearch skill
        from promptops.skills.os_control.press_windows_search import WinSearchSkill
        return await WinSearchSkill().run(app_name)
