from typing import List

from lab4.app.my_project.auth.dao import exchange_service_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class ExchangeServiceService(GeneralService):

    _dao = exchange_service_dao

    def get_exchange_by_device_type(self, device_type_id: int) -> List[object]:
        return self._dao.get_exchange_by_device_type(device_type_id)
