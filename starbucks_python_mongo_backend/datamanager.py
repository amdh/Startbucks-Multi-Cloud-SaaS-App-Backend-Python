from pymongo import MongoClient

client = MongoClient()
client = MongoClient('ec2-54-215-205-70.us-west-1.compute.amazonaws.com', 27017)
db = client.starbucks_database
collection = db.orders