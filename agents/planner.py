# Task Planner Agent: Splits prompt into sequential tasks
from typing import List
from promptops.llm.gemini_client import gemini_plan_tasks

async def plan_tasks(prompt: str) -> List[str]:
    # Use Gemini to break prompt into steps
    return await gemini_plan_tasks(prompt)
