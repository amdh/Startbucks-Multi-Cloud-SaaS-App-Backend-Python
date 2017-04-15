from flask import Flask, json

app = Flask(__name__)


@app.route("/v1/starbucks/ping", methods=['GET'])
def testPing():
    print("ping successfull")
    return json.dumps({'status' : 'ok' , 'message': 'Starbucks API service :v1'})

if __name__ == "__main__":
    app.run(debug=True)
