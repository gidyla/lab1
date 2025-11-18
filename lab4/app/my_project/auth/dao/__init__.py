from .orders.bugfix_service_dao import BugfixServiceDAO 
from .orders.device_type_dao import DeviceTypeDAO
from .orders.employee_dao import EmployeeDAO
from .orders.exchange_service_dao import ExchangeServiceDAO
from .orders.give_service_dao import GiveServiceDAO
from .orders.office_location_dao import OfficeLocationDAO
from .orders.repair_service_dao import RepairServiceDAO
from .orders.room_location_dao import RoomLocationDAO
from .orders.update_service_dao import UpdateServiceDAO
from .orders.workplace_bugfix_dao import WorkplaceBugfixDAO
from .orders.workplace_exchange_dao import WorkplaceExchangeDAO
from .orders.workplace_give_dao import WorkplaceGiveDAO
from .orders.workplace_repair_dao import WorkplaceRepairDAO
from .orders.workplace_update_dao import WorkplaceUpdateDAO
from .orders.workplace_dao import WorkplaceDAO

bugfix_service_dao = BugfixServiceDAO()
device_type_dao = DeviceTypeDAO()
employee_dao = EmployeeDAO()
exchange_service_dao = ExchangeServiceDAO()
give_service_dao = GiveServiceDAO()
office_location_dao = OfficeLocationDAO()
repair_service_dao = RepairServiceDAO()
room_location_dao = RoomLocationDAO()
update_service_dao = UpdateServiceDAO()
workplace_bugfix_dao = WorkplaceBugfixDAO()
workplace_exchange_dao = WorkplaceExchangeDAO()
workplace_give_dao = WorkplaceGiveDAO()
workplace_repair_dao = WorkplaceRepairDAO()
workplace_update_dao = WorkplaceUpdateDAO()
workplace_dao = WorkplaceDAO()
