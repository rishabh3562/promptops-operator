from promptops.skills.base import BaseSkill
import os

class Skill_create_a_new_folder_named_test(BaseSkill):
    async def run(self, **kwargs):
        try:
            os.makedirs("test", exist_ok=True)
            return True
        except OSError as e:
            return False
