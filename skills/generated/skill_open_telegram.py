from promptops.skills.base import BaseSkill
import subprocess

class Skill_open_telegram(BaseSkill):
    async def run(self, **kwargs):
        try:
            subprocess.run(["telegram-desktop"], check=True)
            return True
        except FileNotFoundError:
            return False
        except subprocess.CalledProcessError:
            return False
