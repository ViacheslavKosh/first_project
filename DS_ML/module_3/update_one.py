from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://koshelevskiyv:GOIT2024_Zp@goitlearn.1laswll.mongodb.net/",
    server_api=ServerApi('1')
)
db = client.book

db.cats.update_one({"name": "barsik"}, {"$set": {"age": 4}})
result = db.cats.find_one({"name": "barsik"})
print(result)

