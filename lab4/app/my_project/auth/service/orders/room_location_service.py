from lab4.app.my_project.auth.dao import room_location_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class RoomLocationService(GeneralService):

    _dao = room_location_dao