from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Workplace


class WorkplaceDAO(GeneralDAO):
    _domain_type = Workplace

    def get_employee_by_office(self, office_location_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_employee_by_office(:p1)"),
                                       {'p1': office_location_id}).mappings().all()
        return [dict(row) for row in result]

    def get_office_by_employee(self, employee_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_office_by_employee(:p1)"),
                                       {'p1': employee_id}).mappings().all()
        return [dict(row) for row in result]
