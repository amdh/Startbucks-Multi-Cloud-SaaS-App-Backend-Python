from enum import Enum
import uuid
import datamanager
import time
from threading import Thread
import socket

class OrderStatus(Enum):
    PLACED = 1
    PAID = 2
    PREPARING = 3
    SERVED = 4
    COLLECTED = 5

class worker(Thread):

    def _init_(self,order_id):
        super(worker,self)._init_()
        self.order_id=order_id

    def run(self):
        datamanager.collection.update({'order.id': self.order_id}, {"$set": {'order.status': "PREPARING"}})
        time.sleep(2)
        datamanager.collection.update({'order.id': self.order_id}, {"$set": {'order.status': "SERVED"}})
        time.sleep(10)
        datamanager.collection.update({'order.id': self.order_id}, {"$set": {'order.status': "COLLECTED"}})

class StarbucksAPIService():

    def postOrder(self,Order):
        # POST THE ORDER IN THE DB
        print("post order")
        order_id = uuid.getnode()
        Order['id'] = str(order_id)
        links = {
            "payment": socket.gethostname()+"/v1/starbucks/order/" + str(order_id) + "/pay",
            "order": socket.gethostname()+"/v1/starbucks/order/" + str(order_id)
        }
        Order['links'] = links
        Order['status'] = "PLACED"
        Order['message'] = "Order has been placed"
        print(Order)
        datamanager.collection.insert_one({"order": Order})
        return Order

    def getOrder(self, id):
        # POST THE ORDER IN THE DB
        print("get order")
        data = datamanager.collection.find_one({"id": id}, {"_id": 0})
        return data

    def putOrder(self, Order,id):
        # POST THE ORDER IN THE DB
        print("put order")
        datamanager.collection.update({'id': id}, {"$set": Order}, upsert=False)  # updating the order
        return {'status':'updated'}

    def payOrder(self, id):
        # POST THE ORDER IN THE DB
        print("paid order")
        datamanager.collection.update({'id': id}, {"$set": {'status': "Paid"}})
        worker(id).start()
        return {'status':'paid'}

    def getOrders(self):
        print("inside getOrders")
        cursor = datamanager.collection.find({}, {"_id": 0})
        orders = {}
        for document in cursor:
            print(document)
            orders.update(document)
        return orders

    def deleteOrder(self,id):
        print("Cancelling order with id", id)
        order = datamanager.collection.find_one({"id": id}, {"_id": 0})
        print(order)
        if order is None:
            message = {
                'status': "error",
                'message': "Order not found"
            }
            return (message)
        else:
            datamanager.collection.remove({"id": id})
        return "Order Cancelled"
