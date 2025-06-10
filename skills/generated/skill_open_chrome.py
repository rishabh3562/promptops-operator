
from promptops.skills.base import BaseSkill
class Skill_open_chrome(BaseSkill):
    name = 'skill_open_chrome'
    async def run(self, **kwargs):
        print('Dummy skill executed')
        return True
