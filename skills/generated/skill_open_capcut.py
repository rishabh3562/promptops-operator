from promptops.skills.base import BaseSkill
import subprocess

class Skill_open_capcut(BaseSkill):
    async def run(self, **kwargs):
        try:
            subprocess.run(["open", "-a", "CapCut"], check=True)
            return True
        except FileNotFoundError:
            return False
        except subprocess.CalledProcessError:
            return False
