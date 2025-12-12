from typing import List

from my_project.auth.dao import office_location_dao
from my_project.auth.service.general_service import GeneralService


class OfficeLocationService(GeneralService):

    _dao = office_location_dao

    def get_office_by_room(self, room_location_id: int) -> List[object]:
        return self._dao.get_office_by_room(room_location_id)