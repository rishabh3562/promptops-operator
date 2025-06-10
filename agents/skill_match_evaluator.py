"""
Evaluator Agent
‒ Given the planner’s task text and the best‑match metadata from Qdrant,
  decide whether the match is good enough (→ use it) or bad (→ trigger
  Auto‑Skill‑Updater).

Default LLM = Gemini 1.5‑Flash.  
Fallback = OpenAI Chat (3.5‑turbo) if `LLM_PROVIDER=openai`.
"""

import os, asyncio
from promptops.config.settings import GEMINI_API_KEY, OPENAI_API_KEY
from promptops.config.settings import os as _os  # for LLM_PROVIDER var

###############################################################################
# Low‑level LLM helpers
###############################################################################

async def _call_gemini(prompt: str) -> str:
    import google.generativeai as genai

    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    # google‑generative‑ai is sync → off‑thread to not block
    def _sync_call():
        return model.generate_content(prompt).text.strip()
    return await asyncio.to_thread(_sync_call)


async def _call_openai(prompt: str) -> str:
    from openai import AsyncOpenAI

    client = AsyncOpenAI(api_key=OPENAI_API_KEY)
    resp = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return resp.choices[0].message.content.strip()

###############################################################################
# Public helper with provider switch
###############################################################################

async def call_llm(prompt: str) -> str:
    provider = _os.getenv("LLM_PROVIDER", "gemini").lower()
    if provider == "openai":
        return await _call_openai(prompt)
    # default → gemini
    return await _call_gemini(prompt)

###############################################################################
# Main evaluator API
###############################################################################

async def evaluate_skill_match(task: str, matched_skill: dict) -> bool:
    """
    Returns True  → use matched_skill
            False → generate a new skill
    """
    eval_prompt = f"""
You are an evaluator for an LLM automation system.

TASK: "{task}"
MATCHED_SKILL_NAME: {matched_skill['name']}
MATCHED_SKILL_CLASS: {matched_skill['class_name']}

Answer ONLY "yes" (good match) or "no" (poor match).
"""
    response = await call_llm(eval_prompt)
    return response.lower().strip().startswith("y")
