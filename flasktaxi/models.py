"""Модели приложения."""
import datetime
from flasktaxi import db


class Driver(db.Model):
    """Класс водителя."""

    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    car = db.Column(db.String(50), nullable=False)
    orders = db.relationship('Order', backref='driver', lazy=True)

    def create(self):
        """Создание экземпляра водителя."""
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, name, car):
        """Инициализация экземпляра водителя."""
        self.name = name
        self.car = car


class Client(db.Model):
    """Класс клиента."""

    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    is_vip = db.Column(db.Boolean, nullable=False)
    orders = db.relationship('Order', backref='client', lazy=True)

    def create(self):
        """Создание экземпляра клиента."""
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, name, is_vip):
        """Инициализация экземпляра клиента."""
        self.name = name
        self.is_vip = is_vip


class Order(db.Model):
    """Класс заказа."""

    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    address_from = db.Column(db.String(200), nullable=False)
    address_to = db.Column(db.String(200), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'),
                          nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'),
                          nullable=False)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.datetime.utcnow)
    status = db.Column(db.String(200), nullable=False, default="not_accepted")

    def create(self):
        """Создание экземпляра заказа."""
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, name, is_vip):
        """Инициализация экземпляра заказа."""
        self.name = name
        self.is_vip = is_vip


db.create_all()
