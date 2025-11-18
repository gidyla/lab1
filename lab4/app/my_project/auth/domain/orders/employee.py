from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Employee(db.Model, IDto):

    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"room_location({self.id}, '{self.name}', '{self.surname}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Employee:
        obj = Employee(**dto_dict)
        return obj
