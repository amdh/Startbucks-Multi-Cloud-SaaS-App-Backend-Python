from flask import Flask, render_template, request, session, flash, redirect, jsonify, json
from flask.views import MethodView
from flask.ext.restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class OrdersResource(MethodView):
	
	def get(self):
		return {'hello': 'world'}

	def post(self):
			temp=request.get_json(force=True)
			item = OrderItem(temp['id'], temp['name'],temp['milk'], temp['size'],  temp['qty'])


			ret_order = {
				"id": "3b91d4f0-444c-466e-87c9-7e38133e6c88",
				"location": "take-out",
				"items": [
					{
					"qty": item.qty,
					"name": item.name,
					"milk": item.milk,
					"size": item.size
					}
				],	
				"status": "PLACED",
				"message": "Order has been placed."        

			}
			a= json.dumps(ret_order)
			res = Response(response=a,status= 201, mimetype='application/json')
			return res 

api.add_resource(OrdersResource,'/v1/orders', endpoint = 'orders')
