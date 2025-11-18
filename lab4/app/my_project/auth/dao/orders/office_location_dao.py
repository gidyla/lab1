from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import OfficeLocation


class OfficeLocationDAO(GeneralDAO):
    _domain_type = OfficeLocation

    def get_office_by_room(self, room_location_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_office_by_room(:p1)"),
                                       {'p1': room_location_id}).mappings().all()
        return [dict(row) for row in result]
