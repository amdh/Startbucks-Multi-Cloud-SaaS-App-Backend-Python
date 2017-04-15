from pymongo import MongoClient

client = MongoClient()
client = MongoClient('starbucks-mongo', 27017)
db = client.starbucks_database
collection = db.orders