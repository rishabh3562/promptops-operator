from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance
from promptops.config.clients import qdrant

collection_name = "skills"

# Only create if it doesn't exist
if not qdrant.collection_exists(collection_name=collection_name):
    qdrant.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
    )
    print(f"Created collection: {collection_name}")
else:
    print(f"Collection '{collection_name}' already exists.")
