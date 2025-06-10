from promptops.skills.base import BaseSkill

class Skill_create_a_text_file_and_write_hello_world(BaseSkill):
    async def run(self, **kwargs):
        try:
            with open("hello.txt", "w") as f:
                f.write("Hello, world!")
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
