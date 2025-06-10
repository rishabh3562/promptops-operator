from promptops.skills.base import BaseSkill
import os
import subprocess

class Skill_open_notepad(BaseSkill):
    async def run(self, **kwargs):
        try:
            os.startfile("notepad.exe")
            return True
        except FileNotFoundError:
            try:
                subprocess.run(["notepad.exe"], check=True)
                return True
            except FileNotFoundError:
                return False
        except Exception as e:
            return False
