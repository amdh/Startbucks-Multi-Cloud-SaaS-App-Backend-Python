from pymongo import MongoClient

client = MongoClient()
client = MongoClient('54.193.0.40', 27017)
db = client.starbucks_database
collection = db.orders