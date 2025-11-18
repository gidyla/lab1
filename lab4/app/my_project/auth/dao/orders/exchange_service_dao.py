from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import ExchangeService


class ExchangeServiceDAO(GeneralDAO):
    _domain_type = ExchangeService

    def get_exchange_by_device_type(self, device_type_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_exchange_by_device_type(:p1)"),
                                       {'p1': device_type_id}).mappings().all()
        return [dict(row) for row in result]

