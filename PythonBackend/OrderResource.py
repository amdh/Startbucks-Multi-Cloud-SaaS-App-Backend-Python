from flask import Flask, render_template, request, session, flash, redirect, jsonify, json, Response
from flask.views import MethodView
from flask.ext.restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class OrderResource(Resource):
	
	def get(self):
		ret_order = {
			"id": "3b91d4f0-444c-466e-87c9-7e38133e6c88",
			"location": "take-out",
			"items": [
				{
					"qty": 1,
					"name": "latte",
					"milk": "whole",
					"size": "large"
				}
			],
			"links": {
				"payment": "http://54.193.35.218:9090/v3/starbucks/order/3b91d4f0-444c-466e-87c9-7e38133e6c88/pay",
				"order": "http://54.193.35.218:9090/v3/starbucks/order/3b91d4f0-444c-466e-87c9-7e38133e6c88"
			},
			"status": "PLACED",
			"message": "Order has been placed."
		}
		res = Response(json.dumps(ret_order), status=200)
		return res

Api(app).add_resource(OrderResource,'/v1/order', endpoint = 'orders')
    
