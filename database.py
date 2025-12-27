from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "assessment"

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]

user_collection = db["user"]
