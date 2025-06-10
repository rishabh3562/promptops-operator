# promptops/scripts/index_core_skills.py
import os, asyncio
from promptops.registry.indexer import index_skill

async def main():
    base = os.path.join(os.path.dirname(__file__), "..", "skills", "os_control")
    for fname in os.listdir(base):
        if not fname.endswith(".py"): continue
        skill_name = fname[:-3]                      # e.g. "click_button"
        file_path = os.path.join(base, fname)
        code = open(file_path, "r", encoding="utf-8").read()
        await index_skill(skill_name, file_path, code)
        print(f"Indexed core skill: {skill_name}")

if __name__ == "__main__":
    asyncio.run(main())
