from flask import Flask
import OrderResource
from flask.ext.restful import Api, Resource
import database
app = Flask(__name__)
api = Api(app)



if __name__ == "__main__":
    app.run(debug=True)
