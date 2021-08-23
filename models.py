from sqlalchemy import (Column, 
    Integer, String, Boolean, ForeignKey, DateTime)
from database import Base
import datetime

class Driver(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    car = Column(String(50), nullable=False)

    def __init__(self, name, car):
        self.name = name
        self.car = car

    def __repr__(self):
        return f'<Driver \# {self.id}: {self.name}>'


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    is_vip = Column(Boolean, nullable=False)

    def __init__(self, name, is_vip):
        self.name = name
        self.is_vip = is_vip

    def __repr__(self):
        return f'<Client \# {self.id}: {self.name}>'


class Orders(Base):
    
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    address_from = Column(String(200), nullable=False)
    address_to = Column(String(200), nullable=False)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    driver_id = Column(Integer, ForeignKey('driver.id'), nullable=False)
    date_created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    status = Column(String(200), nullable=False, default="not_accepted")

    def __init__(self, name, is_vip):
        self.name = name
        self.is_vip = is_vip

    def __repr__(self):
        return f'<Order \# {self.id}>'