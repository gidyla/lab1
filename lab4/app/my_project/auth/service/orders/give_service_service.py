from lab4.app.my_project.auth.dao import give_service_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class GiveServiceService(GeneralService):

    _dao = give_service_dao