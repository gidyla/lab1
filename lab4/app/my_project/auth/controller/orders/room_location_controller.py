from my_project.auth.service import room_location_service
from my_project.auth.controller.general_controller import GeneralController


class RoomLocationController(GeneralController):

    _service = room_location_service