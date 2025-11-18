from lab4.app.my_project.auth.dao import update_service_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class UpdateServiceService(GeneralService):

    _dao = update_service_dao