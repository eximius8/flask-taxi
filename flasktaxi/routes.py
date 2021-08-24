import json
from flasktaxi import app
from flasktaxi.models import Client, Driver, Order
from flask import abort, request


@app.route('/client', methods=['POST'])
@app.route('/client/<id>', methods=['GET', 'POST'])
def get_client(id=None):
    if request.method=="GET":
        client = Client.query.get(int(id))
        if client:
            return json.dumps({"dasds": 5})
        else:
            return json.dumps({"error": f"client with id {id} not found"})
    elif request.method=="POST":
        clientdata = request.data
        if clientdata:
            return clientdata
        else:
            return json.dumps({"error": "dsadasdas"})


