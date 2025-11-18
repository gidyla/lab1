from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class GiveService(db.Model, IDto):

    __tablename__ = "give_service"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    describtion = db.Column(db.String(45), nullable=False)
    service_time = db.Column(db.Date, nullable=False)
    device_condition = db.Column(db.String(45), nullable=False)
    device_type_id = db.Column(db.Integer, db.ForeignKey('device_type.id'), nullable=False)
    device_type = db.relationship('DeviceType', backref='give_service')

    def __repr__(self) -> str:
        return f"give_service({self.id}, '{self.describtion}', '{self.service_time}', '{self.device_condition}', {self.device_type_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "describtion": self.describtion,
            "service_time": self.service_time,
            "device_condition": self.device_condition,
            "device_type_id": self.device_type_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> GiveService:
        obj = GiveService(**dto_dict)
        return obj
