from typing import List

from my_project.auth.service import exchange_service_service
from my_project.auth.controller.general_controller import GeneralController


class ExchangeServiceController(GeneralController):

    _service = exchange_service_service

    def get_exchange_by_device_type(self, device_type_id: int) -> List[object]:
        return self._service.get_exchange_by_device_type(device_type_id)
