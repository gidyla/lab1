# my_project/auth/domain/orders/office_location.py

from .... import db
from sqlalchemy import Column, Integer, String


class OfficeLocation(db.Model):
    __tablename__ = 'office_location'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)

    def __init__(self, city: str, address: str):
        self.city = city
        self.address = address

    def to_dict(self):
        return {
            "id": self.id,
            "city": self.city,
            "address": self.address
        }
