
from promptops.skills.base import BaseSkill
class Skill_take_a_screenshot(BaseSkill):
    name = 'skill_take_a_screenshot'
    async def run(self, **kwargs):
        print('Dummy skill executed')
        return True
