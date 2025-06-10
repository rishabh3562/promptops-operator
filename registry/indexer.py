import time
from qdrant_client.http.models import PointStruct
from promptops.llm.embedder import get_embedding
from promptops.config.clients import qdrant, mongo_db
from uuid import uuid5, uuid4, NAMESPACE_DNS

async def index_skill(skill_name: str, file_path: str, code: str):
    print("indexer.py: Indexing skill")
    print(f"Indexing skill: {skill_name} from {file_path}")
    """
    1) Embed the skill_name
    2) Upsert into Qdrant (collection 'skills')
    3) Insert metadata into MongoDB.collection 'skills'
    """
    vec = await get_embedding(skill_name)
    if not vec:
        raise ValueError(f"Failed to generate embedding for skill name: {skill_name}")
    print(f"Generated embedding for skill '{skill_name}': [{len(vec)}]")

    tool_id = str(uuid4())  # Ensure unique tool_id
    payload = {
        "tool_id": tool_id,  # 🔑 prevent duplicate key issue
        "name": skill_name,
        "file_path": file_path,
        "class_name": skill_name.capitalize(),
        "created_at": time.time()
    }

    print(f"Payload for Qdrant: {payload}")
    skill_id = str(uuid5(NAMESPACE_DNS, skill_name))  # valid UUID from skill_name
    print(f"Generated skill ID: {skill_id}")
    point = PointStruct(id=skill_id, vector=vec, payload=payload)
    print(f"Upserting point to Qdrant: {len(point.vector)} dimensions, ID: {point.id}")
    qdrant.upsert(collection_name="skills", points=[point])
    print("Upserted skill to Qdrant successfully")

    await mongo_db.skills.update_one(
        {"tool_id": tool_id},  # match on tool_id instead of name
        {"$set": payload},
        upsert=True
    )
