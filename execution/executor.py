# promptops/execution/executor.py

from promptops.dispatcher.trace_logger import trace_logger
from promptops.memory.permission import check_permission
from typing import List, Dict, Any, Tuple

async def execute_skills(
    skills_with_params: List[Tuple[Any, Dict[str, Any]]],
    user_context: dict = None
) -> List[Dict[str, Any]]:
    print("executor.py: Executing skills...")
    print(f'Executing {len(skills_with_params)} skills with user context: {user_context}')
    results = []

    for skill, params in skills_with_params:
        entry = {"skill": skill.name, "params": params}
        allowed = await check_permission(skill, user_context)
        if not allowed:
            trace_logger.log_event("permission_denied", {"skill": skill.name})
            entry["status"] = "skipped_permission"
            results.append(entry)
            continue

        trace_logger.log_event("skill_execution_start", {"skill": skill.name, "params": params})
        try:
            ok = await skill.run(**params)
            trace_logger.log_event("skill_execution_success", {"skill": skill.name})
            entry["status"] = "success" if ok is not False else "failed"
        except Exception as e:
            trace_logger.log_event("skill_execution_error", {
                "skill": skill.name,
                "error": str(e)
            })
            entry["status"] = "error"
            entry["error"] = str(e)

        results.append(entry)

    return results

# # Skill Executor: Runs skills sequentially, checks permission, logs
# from promptops.dispatcher.trace_logger import trace_logger
# from promptops.memory.permission import check_permission

# async def execute_skills(skills: list, user_context: dict = None):
#     print("exector.py: Executing skills...")
#     print(f'Executing {len(skills)} skills with user context: {user_context}')
#     for skill in skills:
#         # Check user permission if persistent state exists
#         allowed = await check_permission(skill, user_context)
#         if not allowed:
#             trace_logger.log_event("permission_denied", {"skill": skill.name})
#             continue

#         trace_logger.log_event("skill_execution_start", {"skill": skill.name})
#         try:
#             await skill.run(**(user_context or {}))
#             trace_logger.log_event("skill_execution_success", {"skill": skill.name})
#         except Exception as e:
#             trace_logger.log_event("skill_execution_error", {
#                 "skill": skill.name,
#                 "error": str(e)
#             })
