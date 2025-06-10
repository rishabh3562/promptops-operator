from promptops.skills.base import BaseSkill
import subprocess

class Skill_git_init(BaseSkill):
    async def run(self, **kwargs):
        try:
            subprocess.run(['git', 'init'], check=True, capture_output=True, text=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr}")
            return False
