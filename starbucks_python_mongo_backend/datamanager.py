from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.starbucks_database
collection = db.orders