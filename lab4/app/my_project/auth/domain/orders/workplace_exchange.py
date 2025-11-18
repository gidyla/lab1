from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class WorkplaceExchange(db.Model, IDto):

    __tablename__ = "workplace_exchange"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    exchange_service_id = db.Column(db.Integer, db.ForeignKey('exchange_service.id'), nullable=False)
    exchange_service = db.relationship('ExchangeService', backref='workplace_exchange')
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplace.id'), nullable=False)
    workplace = db.relationship('Workplace', backref='workplace_exchange')

    def __repr__(self) -> str:
        return f"room_location({self.id}, {self.exchange_service_id}, {self.workplace_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "exchange_service_id": self.exchange_service_id,
            "workplace_id": self.workplace_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> WorkplaceExchange:
        obj = WorkplaceExchange(**dto_dict)
        return obj
