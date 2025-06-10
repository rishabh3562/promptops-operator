# Gemini LLM client for planning and skill generation
from promptops.config.clients import genai
async def gemini_plan_tasks(prompt: str):
    # TODO: Call Gemini API to split prompt into steps
    # For now, return a dummy split
    return [prompt]


async def gemini_generate_skill(task_text: str, skill_name: str):
    prompt = f"""
Generate a Python class named {skill_name.capitalize()} that inherits from `BaseSkill` 
(from `promptops.skills.base`) to perform this task:
\"{task_text}\"

Requirements:
- Import `BaseSkill` using `from promptops.skills.base import BaseSkill`.
- Use `async def run(self, **kwargs)` as the main method.
- The class name should be {skill_name.capitalize()}.
- Use only standard libraries.
- Do NOT redefine the BaseSkill class.
- Do NOT include `if __name__ == "__main__"` or any execution code.
- Return `True` on successful execution.
Only return the code — no explanations or markdown.
"""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = await model.generate_content_async(prompt)
    return response.text.strip()


# async def gemini_generate_skill(task_text: str, skill_name: str):
#     # TODO: Call Gemini API to generate skill code
#     # For now, return a dummy skill class
#     return f"""
# from promptops.skills.base import BaseSkill\nclass {skill_name.capitalize()}(BaseSkill):\n    name = '{skill_name}'\n    async def run(self, **kwargs):\n        print('Dummy skill executed')\n        return True\n"""
