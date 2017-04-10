from flask import Flask, render_template, request, session, flash, redirect, jsonify, json, Response
from flask.views import MethodView

from starbucksAPIService import StarbucksAPIService

app = Flask(__name__)
service = StarbucksAPIService()
# API list

'''

POST    /order
        Create a new order, and upon success,
        receive a Location header specifying the new order’s URI.

GET     /order/{order_id}
        Request the current state of the order specified by the URI.

PUT     /order/{order_id}
        Update an order at the given URI with new information,
        providing the full representation.

DELETE  /order/{order_id}
        Logically remove the order identified by the given URI.

POST    /order/{order_id}/pay
        Process payment for the order.

GET     /orders
        Get list of Open Orders

'''
@app.route("/v1/starbucks/order/<int:id>", methods=['GET'])
def getOrder(id):
    return json.dumps(service.getOrder(id))

@app.route("/v1/starbucks/order", methods=['POST'])
def placeOrder():
    return json.dumps(service.postOrder())

@app.route("/v1/starbucks/order/<int:id>", methods=['PUT'])
def updateOrder(id):
    return json.dumps(service.putOrder(id))

@app.route("/v1/starbucks/order/<int:id>", methods=['DELETE'])
def removeOrder(id):
    return json.dumps(service.deleteOrder(id))

@app.route("/v1/starbucks/order/<int:id>/pay", methods=['POST'])
def payOrder(id):
    return json.dumps(service.payOrder(id))

@app.route("/v1/starbucks/orders", methods=['GET'])
def getOrders():
    order = service.getOrders();
    return json.dumps(order)


if __name__ == "__main__":
    print("running on 0.0.0.0")
    app.run(debug=True,host='0.0.0.0')