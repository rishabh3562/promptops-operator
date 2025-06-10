
from promptops.skills.base import BaseSkill
class Skill_open_spotify(BaseSkill):
    name = 'skill_open_spotify'
    async def run(self, **kwargs):
        print('Dummy skill executed')
        return True
