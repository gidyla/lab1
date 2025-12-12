from my_project.auth.service import workplace_exchange_service
from my_project.auth.controller.general_controller import GeneralController


class WorkplaceExchangeController(GeneralController):

    _service = workplace_exchange_service
