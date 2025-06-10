# promptops/llm/embedder.py

import os
from openai import AsyncOpenAI
from promptops.config.settings import OPENAI_API_KEY, OPENAI_EMBED_MODEL

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def get_embedding(text: str) -> list[float]:
    resp = await client.embeddings.create(
        input=[text],
        model=OPENAI_EMBED_MODEL  # or your env value
    )
    return resp.data[0].embedding
