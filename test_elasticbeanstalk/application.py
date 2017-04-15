from flask import Flask, json

application = Flask(__name__)
application.debug=True


@application.route("/v1/starbucks/ping", methods=['GET'])
def testPing():
    print("ping successfull")
    return json.dumps({'status' : 'ok' , 'message': 'Starbucks API service :v1'})

if __name__ == "__main__":
    application.run(host='0.0.0.0')
