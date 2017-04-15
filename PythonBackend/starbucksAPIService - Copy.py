import models.Order
from enum import Enum
import uuid
import datamanager

class OrderStatus(Enum):
    PLACED = 1
    PAID = 2
    PREPARING = 3
    SERVED = 4
    COLLECTED = 5


class StarbucksAPIService():

    def postOrder(self,Order):
        # POST THE ORDER IN THE DB
        print("post order")
        order_id = uuid.uuid1()
        x = str(order_id)
        datamanager.collection.insert_one({"order": Order})
        return Order

    def getOrder(self, id):
        # POST THE ORDER IN THE DB
        print("get order")
        data = datamanager.collection.find_one({"order.id": id}, {"_id": 0})
        return data

    def putOrder(self, Order,id):
        # POST THE ORDER IN THE DB
        print("put order")
        datamanager.collection.update({'id': id}, {"$set": Order}, upsert=False)  # updating the order
        return {'status':'updated'}

    def payOrder(self, id):
        # POST THE ORDER IN THE DB
        print("paid order")
        datamanager.collection.update({'order.id': id}, {"$set": {'order.status': "Paid"}})
        return {'status':'paid'}

    def getOrders(self):
        print("inside getOrders")
        cursor = datamanager.collection.find()
        for document in cursor:
            print(document)
        return {'status': 'listoders'}

    def cancel_Order(order_id):
        print("Cancelling order with id", order_id)
        datamanager.collection.remove({"id": order_id})
        return "Order Cancelled"
