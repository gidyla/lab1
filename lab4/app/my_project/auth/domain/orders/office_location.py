from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class OfficeLocation(db.Model, IDto):

    __tablename__ = "office_location"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    office_adress = db.Column(db.String(45), nullable=False)
    room_location_id = db.Column(db.Integer, db.ForeignKey('room_location.id'), nullable=False)
    room_location = db.relationship('RoomLocation', backref='office_location')

    def __repr__(self) -> str:
        return f"room_location({self.id}, '{self.office_adress}', {self.room_location_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "office_adress": self.office_adress,
            "room_location_id": self.room_location_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> OfficeLocation:
        obj = OfficeLocation(**dto_dict)
        return obj
