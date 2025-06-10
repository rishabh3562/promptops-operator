# Skill Matcher: Qdrant + MongoDB search for similar skills
from promptops.llm.embedder import get_embedding
from promptops.registry.query import query_qdrant
from promptops.skills.base import BaseSkill
import importlib.util
from promptops.agents.skill_match_evaluator import evaluate_skill_match  # NEW

async def find_similar_skill(task_text: str) -> BaseSkill | None:
    print("skill_matcher.py: Finding similar skill for task:", task_text)
    emb = await get_embedding(task_text)
    if not emb:
        return None

    skill_meta = await query_qdrant(emb)
    print("skill_matcher.py: Skill metadata from Qdrant:", skill_meta)
    if not skill_meta:
        return None

    is_good_match = await evaluate_skill_match(task_text, skill_meta)  # NEW
    print("skill_matcher.py: Skill match evaluation result:", is_good_match)
    if not is_good_match:
        print("Evaluator: Match not confident. Skill will be generated.")
        return None

    # Dynamically load class
    file_path = skill_meta["file_path"]
    class_name = skill_meta["class_name"]
    spec = importlib.util.spec_from_file_location(class_name, file_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    SkillCls = getattr(mod, class_name)
    return SkillCls()
