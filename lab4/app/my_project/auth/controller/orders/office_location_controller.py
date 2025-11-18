from typing import List

from lab4.app.my_project.auth.service import office_location_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class OfficeLocationController(GeneralController):

    _service = office_location_service

    def get_office_by_room(self, room_location_id: int) -> List[object]:
        return self._service.get_office_by_room(room_location_id)
