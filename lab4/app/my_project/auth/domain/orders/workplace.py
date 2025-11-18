from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Workplace(db.Model, IDto):

    __tablename__ = "workplace"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    employee = db.relationship('Employee', backref='workplace')
    office_location_id = db.Column(db.Integer, db.ForeignKey('office_location.id'), nullable=False)
    office_location = db.relationship('OfficeLocation', backref='workplace')

    def __repr__(self) -> str:
        return f"room_location({self.id}, {self.employee_id}, {self.office_location_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "office_location_id": self.office_location_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Workplace:
        obj = Workplace(**dto_dict)
        return obj
