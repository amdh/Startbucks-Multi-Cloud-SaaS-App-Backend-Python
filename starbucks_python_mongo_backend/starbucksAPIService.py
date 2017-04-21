from enum import Enum
import uuid
import datamanager
import time
from threading import Thread
import socket
import _thread


class OrderStatus(Enum):
    PLACED = 1
    PAID = 2
    PREPARING = 3
    SERVED = 4
    COLLECTED = 5


class status(Thread):

    def _init_(self,order_id):
        super(status,self)._init_()
        self.order_id=order_id

    def run(self):
        time.sleep(5)
        datamanager.collection.update({'id': self.order_id}, {"$set": {'status': "PREPARING"}})
        time.sleep(2)
        datamanager.collection.update({'id': self.order_id}, {"$set": {'status': "SERVED"}})
        time.sleep(10)
        datamanager.collection.update({'id': self.order_id}, {"$set": {'status': "COLLECTED"}})

class StarbucksAPIService():

    def postOrder(self,Order):
        # POST THE ORDER IN THE DB
        print("post order", Order)
        order_id = uuid.uuid1()
        Order['id'] = str(order_id)
        links = {
            "payment": socket.gethostname()+"/v1/starbucks/order/" + str(order_id) + "/pay",
            "order": socket.gethostname()+"/v1/starbucks/order/" + str(order_id)
        }
        Order['links'] = links
        Order['status'] = "PLACED"
        Order['message'] = "Order has been placed"
        print(Order)
        datamanager.collection.insert_one(Order)
        return self.getOrder(str(order_id))

    def getOrder(self, id):
        # get THE ORDER IN THE DB
        print("get order")
        data = datamanager.collection.find_one({"id": id}, {"_id": 0})
        if data is None:
            data = {
                "status": "error",
                "message": "Order not found."
                }
        return data

    def putOrder(self, Order,id):
        # POST THE ORDER IN THE DB
        print("put order")
        order = self.getOrder(id)
        if order['status'] == "PAID" or order['status'] == "PREPARING" or order['status'] == "SERVED" or order[
            'status'] == "COLLECTED":
            message = {
                'status': "error",
                'message': "Order payment done hence cannot be updated "
            }
            return message
        else:
            datamanager.collection.update({'id': id}, {"$set":{"items":Order['items']}})  # updating the order
        return self.getOrder(id)

    def payOrder(self, id):
        # POST THE ORDER IN THE DB
        print("paid order")
        order = self.getOrder(id)
        if order['status'] == "PAID" or order['status'] == "PREPARING" or order['status'] == "SERVED" or order[
            'status'] == "COLLECTED":
            message = {
                'status': "error",
                'message': "Order payment rejected"
            }
            return message
        else:
            datamanager.collection.update({'id': id}, {"$set": {'status': "PAID", 'message': "Payment Accepted"}})
            datamanager.collection.update({'id': id}, {"$unset": {'links.payment': ''}})
            #statusAPI(None,id).start()
            _thread.start_new_thread(self.statusAPI, ("Thread-1", id,))
        return self.getOrder(id)

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

    def statusAPI(self,threadname,order_id):
        print(threadname)
        time.sleep(5)
        datamanager.collection.update({'id': order_id}, {"$set": {'status': "PREPARING"}})
        time.sleep(2)
        datamanager.collection.update({'id': order_id}, {"$set": {'status': "SERVED"}})
        time.sleep(10)
        datamanager.collection.update({'id': order_id}, {"$set": {'status': "COLLECTED"}})


