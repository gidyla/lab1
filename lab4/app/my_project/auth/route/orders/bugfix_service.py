from flask import Blueprint, request
from http import HTTPStatus

from ...controller import bugfix_service_controller


bugfix_service_bp = Blueprint(
    "bugfix_service",
    __name__,
    url_prefix="/bugfix-service"
)


@bugfix_service_bp.route("/", methods=["GET"])
def get_all():
    return bugfix_service_controller.get_all(), HTTPStatus.OK


@bugfix_service_bp.route("/<int:item_id>", methods=["GET"])
def get_by_id(item_id: int):
    result = bugfix_service_controller.get_by_id(item_id)
    if result is None:
        return {"message": "Not found"}, HTTPStatus.NOT_FOUND
    return result, HTTPStatus.OK


@bugfix_service_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    return bugfix_service_controller.create(data), HTTPStatus.CREATED


@bugfix_service_bp.route("/<int:item_id>", methods=["PUT"])
def update(item_id: int):
    data = request.get_json()
    result = bugfix_service_controller.update(item_id, data)
    if result is None:
        return {"message": "Not found"}, HTTPStatus.NOT_FOUND
    return result, HTTPStatus.OK


@bugfix_service_bp.route("/<int:item_id>", methods=["DELETE"])
def delete(item_id: int):
    result = bugfix_service_controller.delete(item_id)
    if not result:
        return {"message": "Not found"}, HTTPStatus.NOT_FOUND
    return {}, HTTPStatus.NO_CONTENT
