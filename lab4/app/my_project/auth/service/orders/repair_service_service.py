from my_project.auth.dao import repair_service_dao
from my_project.auth.service.general_service import GeneralService


class RepairServiceService(GeneralService):

    _dao = repair_service_dao