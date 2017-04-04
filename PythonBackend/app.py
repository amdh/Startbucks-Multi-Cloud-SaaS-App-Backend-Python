from flask                          import Flask, render_template, request, session, flash, redirect, jsonify, json
from configparser                   import ConfigParser
from dynamodb.connectionManager     import ConnectionManager
from OrderResource					import OrderResource
from OrdersResource					import OrdersResource
from PaymentResource				import PaymentResource

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')