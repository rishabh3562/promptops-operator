# Auto Skill Updater: Generates new skills using Gemini/OpenAI
from promptops.llm.gemini_client import gemini_generate_skill
from promptops.llm.openai_client import openai_generate_skill
from promptops.registry.skill_namer import get_skill_name
from promptops.skills.base import BaseSkill
from promptops.registry.indexer import index_skill
import importlib.util
import os
from typing import Optional

async def generate_new_skill(task_text: str, provider: str = "gemini") -> Optional[BaseSkill]:
    print(f"auto_skill_updater.py \n\n")
    print(f"[AutoSkillUpdater] Requested task   : {task_text}")
    print(f"[AutoSkillUpdater] LLM provider      : {provider}")

    # 1️⃣  Generate a deterministic, snake‑case file name
    skill_name = get_skill_name(task_text)
    print(f"[AutoSkillUpdater] Resolved skill name: {skill_name}")

    # 2️⃣  Ask chosen provider to create the code
    if provider == "gemini":
        code = await gemini_generate_skill(task_text, skill_name)
        print(f"[AutoSkillUpdater] ✅ Gemini returned code for {skill_name}")
    else:
        code = await openai_generate_skill(task_text, skill_name)
        print(f"[AutoSkillUpdater] ✅ OpenAI  returned code for {skill_name}")

    # Show a preview (first 200 chars)
    print(f"[AutoSkillUpdater] --- Code preview (first 200 chars) ---\n{code[:200]}\n")
    if code.strip().startswith("```"):
        code = code.strip().split("```")[1]  # removes first triple backtick
    if code.startswith("python"):
        code = "\n".join(code.splitlines()[1:])  # remove 'python' line

    # 3️⃣  Persist to /skills/generated/
    gen_dir   = os.path.join(os.path.dirname(__file__), "..", "skills", "generated")
    os.makedirs(gen_dir, exist_ok=True)
    file_path = os.path.join(gen_dir, f"{skill_name}.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"[AutoSkillUpdater] 💾 Saved to: {file_path}")

    # 4️⃣  Index in registry
    print(f"[AutoSkillUpdater] 🔄 Indexing skill in registry…")
    await index_skill(skill_name, file_path, code)
    print(f"[AutoSkillUpdater] ✅ Index complete")

    # 5️⃣  Dynamically import the new module
    print(f"[AutoSkillUpdater] 📦 Importing generated module…")
    spec = importlib.util.spec_from_file_location(skill_name, file_path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    print(f"[AutoSkillUpdater] ✅ Module imported: {mod}")

    # 6️⃣  Return the first subclass of BaseSkill found
    print(f"[AutoSkillUpdater] 🔍 Searching for BaseSkill subclass…")
    for attr in dir(mod):
        obj = getattr(mod, attr)
        if isinstance(obj, type) and issubclass(obj, BaseSkill) and obj is not BaseSkill:
            print(f"[AutoSkillUpdater] 🎉 Loaded skill class: {obj.__name__}")
            return obj()

    # 7️⃣  No valid skill detected
    print(f"[AutoSkillUpdater] ❌ No subclass of BaseSkill found in generated code.")
    raise RuntimeError("No valid skill class found in generated code.")
