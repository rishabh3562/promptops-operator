# clients.py
from motor.motor_asyncio import AsyncIOMotorClient
from qdrant_client import QdrantClient
import google.generativeai as genai
from urllib.parse import urlparse
from .settings import QDRANT_URL, QDRANT_API_KEY, MONGO_URI,GEMINI_API_KEY
from dotenv import load_dotenv
# Qdrant client
qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

# Mongo client
mongo_client = AsyncIOMotorClient(MONGO_URI)
db_name = urlparse(MONGO_URI).path[1:]  # gets DB name from URI
mongo_db = mongo_client[db_name]

# Configure Gemini client
GOOGLE_API_KEY = GEMINI_API_KEY 
genai.configure(api_key=GOOGLE_API_KEY)

async def get_mongo_collection(collection_name: str):
    """
    Get a MongoDB collection by name.
    """
    return mongo_db[collection_name]


