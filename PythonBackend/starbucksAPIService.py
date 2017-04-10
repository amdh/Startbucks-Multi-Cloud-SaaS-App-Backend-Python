import models.Order
from enum import Enum
#import database

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
        return {'status':'posted'}

    def getOrder(self, id):
        # POST THE ORDER IN THE DB
        print("get order")
        return {'name':'heloworld'}

    def putOrder(self, id):
        # POST THE ORDER IN THE DB
        print("put order")
        return {'status':'updated'}

    def deleteOrder(self, id):
        # POST THE ORDER IN THE DB
        print("delete order")
        return {'status':'deleted'}

    def payOrder(self, id):
        # POST THE ORDER IN THE DB
        print("paid order")
        return {'status':'paid'}

    def getOrders(self):
        print("inside getOrders")
        return {'status': 'listoders'}
