from my_project.auth.dao import room_location_dao
from my_project.auth.service.general_service import GeneralService


class RoomLocationService(GeneralService):

    _dao = room_location_dao