# Skill Namer: Consistent naming for generated skills
import re

def get_skill_name(task_text: str) -> str:
    # Simple slugify: lowercase, replace spaces with _, remove non-alphanum
    base = re.sub(r'[^a-zA-Z0-9 ]', '', task_text).strip().lower().replace(' ', '_')
    return f"skill_{base[:40]}"  # limit length
