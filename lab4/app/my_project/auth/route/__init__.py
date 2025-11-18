from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:

    app.register_blueprint(err_handler_bp)

    from .orders.bugfix_service import bugfix_service_bp
    from .orders.device_type import device_type_bp
    from .orders.employee import employee_bp
    from .orders.exchange_service import exchange_service_bp
    from .orders.give_service import give_service_bp
    from .orders.office_location import office_location_bp
    from .orders.repair_service import repair_service_bp
    from .orders.room_location import room_location_bp
    from .orders.update_service import update_service_bp
    from .orders.workplace_bugfix import workplace_bugfix_bp
    from .orders.workplace_exchange import workplace_exchange_bp
    from .orders.workplace_give import workplace_give_bp
    from .orders.workplace_repair import workplace_repair_bp
    from .orders.workplace_update import workplace_update_bp
    from .orders.workplace import workplace_bp

    app.register_blueprint(bugfix_service_bp)
    app.register_blueprint(device_type_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(exchange_service_bp)
    app.register_blueprint(give_service_bp)
    app.register_blueprint(office_location_bp)
    app.register_blueprint(repair_service_bp)
    app.register_blueprint(room_location_bp)
    app.register_blueprint(update_service_bp)
    app.register_blueprint(workplace_bugfix_bp)
    app.register_blueprint(workplace_exchange_bp)
    app.register_blueprint(workplace_give_bp)
    app.register_blueprint(workplace_repair_bp)
    app.register_blueprint(workplace_update_bp)
    app.register_blueprint(workplace_bp)

    