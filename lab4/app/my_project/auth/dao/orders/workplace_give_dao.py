from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import WorkplaceGive


class WorkplaceGiveDAO(GeneralDAO):
    _domain_type = WorkplaceGive
