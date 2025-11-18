from lab4.app.my_project.auth.service import workplace_update_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class WorkplaceUpdateController(GeneralController):

    _service = workplace_update_service
