from typing import Optional, Dict
from promptops.config.clients import qdrant, mongo_db

async def query_qdrant(embedding: list[float]) -> Optional[Dict]:
    """
    Query Qdrant for the nearest skill vector.
    """
    results = qdrant.search(
        collection_name="skills",
        query_vector=embedding,
        limit=1,
        with_payload=True
    )
    if results:
        return results[0].payload
    return None

async def query_mongo(skill_name: str) -> Optional[Dict]:
    """
    Fetch skill metadata from MongoDB by skill name.
    """
    return await mongo_db.skills.find_one({"name": skill_name})
