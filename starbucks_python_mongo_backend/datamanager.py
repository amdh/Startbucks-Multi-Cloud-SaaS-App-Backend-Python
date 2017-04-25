from pymongo import MongoClient

client = MongoClient()
client = MongoClient('54.153.87.36', 27017)
db = client.starbucks_database
collection = db.orders