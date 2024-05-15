from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://koshelevskiyv:GOIT2024_Zp@goitlearn.1laswll.mongodb.net/",
    server_api=ServerApi('1')
)

db = client.book

result = db.cats.find_one({"_id": ObjectId("66447768974e39b92c163340")})
print(result)

