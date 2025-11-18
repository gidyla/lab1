from lab4.app.my_project.auth.dao import workplace_exchange_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class WorkplaceExchangeService(GeneralService):

    _dao = workplace_exchange_dao