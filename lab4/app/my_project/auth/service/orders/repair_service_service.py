from lab4.app.my_project.auth.dao import repair_service_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class RepairServiceService(GeneralService):

    _dao = repair_service_dao