from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import update_service_controller
from my_project.auth.domain import UpdateService

update_service_bp = Blueprint('UpdateService', __name__, url_prefix='/update-service')


@update_service_bp.get('')
def get_all_update_service() -> Response:
    """
    Get all update services
    ---
    tags:
      - UpdateService
    responses:
      200:
        description: List of all update services
    """
    return make_response(jsonify(update_service_controller.find_all()), HTTPStatus.OK)


@update_service_bp.post('')
def create_update_service() -> Response:
    """
    Create new update service
    ---
    tags:
      - UpdateService
    parameters:
      - in: body
        name: update_service
        required: true
        description: Update service data
        schema:
          type: object
          properties:
            device_id:
              type: integer
              description: Device that receives the update
            employee_id:
              type: integer
              description: Employee applying the update
            update_version:
              type: string
              description: Version of the update
            update_status:
              type: string
              description: Update status
    responses:
      201:
        description: Update service created successfully
    """
    content = request.get_json()
    update_service = UpdateService.create_from_dto(content)
    update_service_controller.create(update_service)
    return make_response(jsonify(update_service.put_into_dto()), HTTPStatus.CREATED)


@update_service_bp.get('/<int:update_service_id>')
def get_update_service(update_service_id: int) -> Response:
    """
    Get update service by ID
    ---
    tags:
      - UpdateService
    parameters:
      - in: path
        name: update_service_id
        required: true
        type: integer
        description: Update service ID
    responses:
      200:
        description: Update service data
      404:
        description: Update service not found
    """
    return make_response(jsonify(update_service_controller.find_by_id(update_service_id)), HTTPStatus.OK)


@update_service_bp.put('/<int:update_service_id>')
def update_update_service(update_service_id: int) -> Response:
    """
    Update update service
    ---
    tags:
      - UpdateService
    parameters:
      - in: path
        name: update_service_id
        required: true
        type: integer
        description: Update service ID
      - in: body
        name: update_service
        description: Updated update service data
        required: true
        schema:
          type: object
          properties:
            device_id:
              type: integer
            employee_id:
              type: integer
            update_version:
              type: string
            update_status:
              type: string
    responses:
      200:
        description: Update service updated successfully
      404:
        description: Update service not found
    """
    content = request.get_json()
    update_service = UpdateService.create_from_dto(content)
    update_service_controller.update(update_service_id, update_service)
    return make_response("UpdateService updated", HTTPStatus.OK)


@update_service_bp.patch('/<int:update_service_id>')
def patch_update_service(update_service_id: int) -> Response:
    """
    Partially update update service
    ---
    tags:
      - UpdateService
    parameters:
      - in: path
        name: update_service_id
        required: true
        type: integer
        description: Update service ID
      - in: body
        name: update_service
        description: Partial update service data
        required: true
        schema:
          type: object
          properties:
            device_id:
              type: integer
            employee_id:
              type: integer
            update_version:
              type: string
            update_status:
              type: string
    responses:
      200:
        description: Update service updated successfully
      404:
        description: Update service not found
    """
    content = request.get_json()
    update_service_controller.patch(update_service_id, content)
    return make_response("UpdateService updated", HTTPStatus.OK)


@update_service_bp.delete('/<int:update_service_id>')
def delete_update_service(update_service_id: int) -> Response:
    """
    Delete update service
    ---
    tags:
      - UpdateService
    parameters:
      - in: path
        name: update_service_id
        required: true
        type: integer
        description: Update service ID
    responses:
      200:
        description: Update service deleted successfully
      404:
        description: Update service not found
    """
    update_service_controller.delete(update_service_id)
    return make_response("UpdateService deleted", HTTPStatus.OK)
