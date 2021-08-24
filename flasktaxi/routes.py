"""Роуты приложения."""
import json
from flasktaxi import app, db
from flasktaxi.models import Client, Driver, Order
from flask import abort, request


@app.route('/client', methods=['POST'])
@app.route('/client/<id>', methods=['GET', 'POST', 'DELETE'])
def crd_client(id=None):
    """Создание/получение/удаление данных клиента."""
    if request.method == "GET":
        client = Client.query.get(int(id))
        if client:
            return json.dumps({"id": client.id,
                               "name": client.name,
                               "is_vip": client.is_vip})
        else:
            return json.dumps({"error": f"client with id {id} not found"})
    elif request.method == "POST":
        json_client_data = request.get_json()
        if 'name' in json_client_data and 'is_vip' in json_client_data:
            new_client = Client(name=json_client_data['name'],
                                is_vip=json_client_data['is_vip'])
            new_client.create()
            return json.dumps({"id": new_client.id})
        return json.dumps(json_client_data)
    elif request.method == "DELETE":
        Client.query.filter(Client.id == int(id)).delete()
        db.session.commit()
        return json.dumps({"success": f"Client {id} deleted."})
    return abort(500)


@app.route('/driver', methods=['POST'])
@app.route('/driver/<id>', methods=['GET', 'POST', 'DELETE'])
def crd_driver(id=None):
    """Создание/получение/удаление данных водителя."""
    if request.method == "GET":
        driver = Driver.query.get(int(id))
        if driver:
            return json.dumps({"id": driver.id,
                               "name": driver.name,
                               "car": driver.car})
        else:
            return json.dumps({"error": f"driver with id {id} not found"})
    elif request.method == "POST":
        json_client_data = request.get_json()
        if 'name' in json_client_data and 'car' in json_client_data:
            new_driver = Driver(name=json_client_data['name'],
                                is_vip=json_client_data['car'])
            new_driver.create()
            return json.dumps({"id": new_driver.id})
        return json.dumps(json_client_data)
    elif request.method == "DELETE":
        Driver.query.filter(Driver.id == int(id)).delete()
        db.session.commit()
        return json.dumps({"success": f"Driver {id} deleted."})
    return abort(500)


@app.route('/order', methods=['POST'])
@app.route('/order/<id>', methods=['GET', 'POST', 'PUT'])
def cru_order(id=None):
    """Создание/получение/удаление данных заказа."""
    if request.method == "GET":
        order = Order.query.get(int(id))
        if order:
            return json.dumps({"id": order.id,
                               "address_from": order.address_from,
                               "address_to": order.address_to,
                               "driver": order.driver_id,
                               "client": order.client_id,
                               "date_created": order.date_created,
                               "status": order.status})
        else:
            return json.dumps({"error": f"order with id {id} not found"})
    elif request.method in ["POST", "PUT"]:
        json_order_data = request.get_json()
        if 'address_from' in json_order_data and \
           'address_to' in json_order_data and \
           'driver' in json_order_data and 'client' in json_order_data:
            new_order = Order(address_from=json_order_data['address_from'],
                              address_to=json_order_data['address_to'],
                              driver=json_order_data['driver'],
                              client=json_order_data['client'],)
            new_order.create()
            return json.dumps({"id": new_order.id})

        return json.dumps(json_order_data)
    return abort(500)
