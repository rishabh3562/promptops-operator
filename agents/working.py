# promptops/agents/working.py

from promptops.agents.planner import plan_tasks
from promptops.registry.skill_matcher import find_similar_skill
from promptops.agents.auto_skill_updater import generate_new_skill
from promptops.execution.executor import execute_skills
from promptops.dispatcher import trace_logger

async def handle_user_prompt(prompt: str, user_context: dict = None):
    print("Working Agent(working.py): Handling user prompt...")
    trace_logger.log_event("user_prompt_received", {"prompt": prompt})
    if not prompt:
        trace_logger.log_event("empty_prompt", {})
        return

    print("Working Agent(working.py): Received user prompt:", prompt)
    tasks = await plan_tasks(prompt)
    if not tasks:
        trace_logger.log_event("no_tasks_planned", {"prompt": prompt})
        return

    print("Working Agent(working.py): Planned tasks:", tasks)
    trace_logger.log_event("tasks_planned", {"tasks": tasks})

    # Collect (skill, params) tuples
    skills_with_params = []
    for task in tasks:
        skill = await find_similar_skill(task)
        print("\nWorking Agent(working.py): Found similar skill:", skill)
        if not skill:
            trace_logger.log_event("skill_not_found", {"task": task})
            skill = await generate_new_skill(task)

        trace_logger.log_event("skill_generated", {"task": task, "skill": skill.name})
        # Default parameter key "text" for your OS/control skills
        params = {"text": task}
        skills_with_params.append((skill, params))

    # Execute all skills with their params
    results = await execute_skills(skills_with_params, user_context)
    print("Working Agent(working.py): Execution result:", results)
    trace_logger.log_event("execution_complete", {"tasks": tasks, "results": results})


# # Working Agent: Receives user prompt, coordinates with planner, registry, executor
# from promptops.agents.planner import plan_tasks
# from promptops.registry.skill_matcher import find_similar_skill
# from promptops.agents.auto_skill_updater import generate_new_skill
# from promptops.execution.executor import execute_skills
# from promptops.dispatcher import trace_logger

# async def handle_user_prompt(prompt: str, user_context: dict = None):
#     print("Working Agent(working.py): Handling user prompt...")
#     trace_logger.log_event("user_prompt_received", {"prompt": prompt})
#     if not prompt:
#         trace_logger.log_event("empty_prompt", {})
#         return
#     print("Working Agent(working.py): Received user prompt:", prompt)
#     tasks = await plan_tasks(prompt)
#     if not tasks:
#         trace_logger.log_event("no_tasks_planned", {"prompt": prompt})
#         return
#     print("Working Agent(working.py): Planned tasks:", tasks)
#     trace_logger.log_event("tasks_planned", {"tasks": tasks})
#     skills = []
#     for task in tasks:
#         skill = await find_similar_skill(task)
#         print("\nWorking Agent(working.py): Found similar skill:", skill)
#         if not skill:
#             trace_logger.log_event("skill_not_found", {"task": task})
#             skill = await generate_new_skill(task)
            
#         trace_logger.log_event("skill_generated", {"task": task, "skill": skill.name})
#         skills.append(skill)
#     res=await execute_skills(skills, user_context)
#     print("Working Agent(working.py): Execution result:", res)
#     trace_logger.log_event("execution_complete", {"tasks": tasks})
