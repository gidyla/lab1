from lab4.app.my_project.auth.dao import workplace_repair_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class WorkplaceRepairService(GeneralService):

    _dao = workplace_repair_dao