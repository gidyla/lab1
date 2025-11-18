from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import bugfix_service_controller
from lab4.app.my_project.auth.domain import BugfixService

bugfix_service_bp = Blueprint('bugfix-service', __name__, url_prefix='/bugfix-service')


@bugfix_service_bp.get('')
def get_all_bugfix_service() -> Response:
    """
    Get all bugfix services
    ---
    tags:
      - BugfixService
    responses:
      200:
        description: List of all bugfix services
    """
    return make_response(jsonify(bugfix_service_controller.find_all()), HTTPStatus.OK)


@bugfix_service_bp.post('')
def create_bugfix_service() -> Response:
    """
    Create new bugfix service
    ---
    tags:
      - BugfixService
    parameters:
      - in: body
        name: bugfix_service
        description: Bugfix service data
        required: true
        schema:
          type: object
          properties:
            developer_id:
              type: integer
              description: Developer ID
            task_id:
              type: integer
              description: Task ID
            status:
              type: string
              description: Bugfix status
    responses:
      201:
        description: Bugfix service created successfully
    """
    content = request.get_json()
    bugfix_service = BugfixService.create_from_dto(content)
    bugfix_service_controller.create(bugfix_service)
    return make_response(jsonify(bugfix_service.put_into_dto()), HTTPStatus.CREATED)


@bugfix_service_bp.get('/<int:bugfix_service_id>')
def get_bugfix_service(bugfix_service_id: int) -> Response:
    """
    Get bugfix service by ID
    ---
    tags:
      - BugfixService
    parameters:
      - in: path
        name: bugfix_service_id
        type: integer
        required: true
        description: Bugfix service ID
    responses:
      200:
        description: Bugfix service data
      404:
        description: Bugfix service not found
    """
    return make_response(jsonify(bugfix_service_controller.find_by_id(bugfix_service_id)), HTTPStatus.OK)


@bugfix_service_bp.put('/<int:bugfix_service_id>')
def update_bugfix_service(bugfix_service_id: int) -> Response:
    """
    Update bugfix service by ID
    ---
    tags:
      - BugfixService
    parameters:
      - in: path
        name: bugfix_service_id
        type: integer
        required: true
        description: Bugfix service ID
      - in: body
        name: bugfix_service
        description: Updated bugfix service data
        required: true
        schema:
          type: object
          properties:
            developer_id:
              type: integer
            task_id:
              type: integer
            status:
              type: string
    responses:
      200:
        description: Bugfix service updated successfully
      404:
        description: Bugfix service not found
    """
    content = request.get_json()
    bugfix_service = BugfixService.create_from_dto(content)
    bugfix_service_controller.update(bugfix_service_id, bugfix_service)
    return make_response("BugfixService updated", HTTPStatus.OK)


@bugfix_service_bp.patch('/<int:bugfix_service_id>')
def patch_bugfix_service(bugfix_service_id: int) -> Response:
    """
    Partially update bugfix service by ID
    ---
    tags:
      - BugfixService
    parameters:
      - in: path
        name: bugfix_service_id
        type: integer
        required: true
        description: Bugfix service ID
      - in: body
        name: bugfix_service
        description: Partial bugfix service data
        required: true
        schema:
          type: object
          properties:
            status:
              type: string
              description: Bugfix status
    responses:
      200:
        description: Bugfix service updated successfully
      404:
        description: Bugfix service not found
    """
    content = request.get_json()
    bugfix_service_controller.patch(bugfix_service_id, content)
    return make_response("BugfixService updated", HTTPStatus.OK)


@bugfix_service_bp.delete('/<int:bugfix_service_id>')
def delete_bugfix_service(bugfix_service_id: int) -> Response:
    """
    Delete bugfix service by ID
    ---
    tags:
      - BugfixService
    parameters:
      - in: path
        name: bugfix_service_id
        type: integer
        required: true
        description: Bugfix service ID
    responses:
      200:
        description: Bugfix service deleted successfully
      404:
        description: Bugfix service not found
    """
    bugfix_service_controller.delete(bugfix_service_id)
    return make_response("BugfixService deleted", HTTPStatus.OK)
