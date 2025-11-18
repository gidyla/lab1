from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import workplace_bugfix_controller
from lab4.app.my_project.auth.domain import WorkplaceBugfix

workplace_bugfix_bp = Blueprint('WorkplaceBugfix', __name__, url_prefix='/workplace-bugfix')


@workplace_bugfix_bp.get('')
def get_all_workplace_bugfix() -> Response:
    """
    Get all workplace bugfix records
    ---
    tags:
      - WorkplaceBugfix
    responses:
      200:
        description: List of all workplace bugfix entries
    """
    return make_response(jsonify(workplace_bugfix_controller.find_all()), HTTPStatus.OK)


@workplace_bugfix_bp.post('')
def create_workplace_bugfix() -> Response:
    """
    Create new workplace bugfix record
    ---
    tags:
      - WorkplaceBugfix
    parameters:
      - in: body
        name: workplace_bugfix
        required: true
        description: Workplace bugfix data
        schema:
          type: object
          properties:
            workplace_id:
              type: integer
              description: Workplace ID
            bugfix_service_id:
              type: integer
              description: Bugfix service ID
            notes:
              type: string
              description: Additional details
    responses:
      201:
        description: Workplace bugfix created successfully
    """
    content = request.get_json()
    workplace_bugfix = WorkplaceBugfix.create_from_dto(content)
    workplace_bugfix_controller.create(workplace_bugfix)
    return make_response(jsonify(workplace_bugfix.put_into_dto()), HTTPStatus.CREATED)


@workplace_bugfix_bp.get('/<int:workplace_bugfix_id>')
def get_workplace_bugfix(workplace_bugfix_id: int) -> Response:
    """
    Get workplace bugfix record by ID
    ---
    tags:
      - WorkplaceBugfix
    parameters:
      - in: path
        name: workplace_bugfix_id
        type: integer
        required: true
        description: Workplace bugfix ID
    responses:
      200:
        description: Workplace bugfix data
      404:
        description: Record not found
    """
    return make_response(jsonify(workplace_bugfix_controller.find_by_id(workplace_bugfix_id)), HTTPStatus.OK)


@workplace_bugfix_bp.put('/<int:workplace_bugfix_id>')
def update_workplace_bugfix(workplace_bugfix_id: int) -> Response:
    """
    Update workplace bugfix record
    ---
    tags:
      - WorkplaceBugfix
    parameters:
      - in: path
        name: workplace_bugfix_id
        type: integer
        required: true
        description: Workplace bugfix ID
      - in: body
        name: workplace_bugfix
        description: Updated data
        required: true
        schema:
          type: object
          properties:
            workplace_id:
              type: integer
            bugfix_service_id:
              type: integer
            notes:
              type: string
    responses:
      200:
        description: Workplace bugfix updated successfully
      404:
        description: Record not found
    """
    content = request.get_json()
    workplace_bugfix = WorkplaceBugfix.create_from_dto(content)
    workplace_bugfix_controller.update(workplace_bugfix_id, workplace_bugfix)
    return make_response("WorkplaceBugfix updated", HTTPStatus.OK)


@workplace_bugfix_bp.patch('/<int:workplace_bugfix_id>')
def patch_workplace_bugfix(workplace_bugfix_id: int) -> Response:
    """
    Partially update workplace bugfix record
    ---
    tags:
      - WorkplaceBugfix
    parameters:
      - in: path
        name: workplace_bugfix_id
        type: integer
        required: true
        description: Workplace bugfix ID
      - in: body
        name: workplace_bugfix
        description: Partial update data
        required: true
        schema:
          type: object
          properties:
            workplace_id:
              type: integer
            bugfix_service_id:
              type: integer
            notes:
              type: string
    responses:
      200:
        description: Workplace bugfix updated successfully
      404:
        description: Record not found
    """
    content = request.get_json()
    workplace_bugfix_controller.patch(workplace_bugfix_id, content)
    return make_response("WorkplaceBugfix updated", HTTPStatus.OK)


@workplace_bugfix_bp.delete('/<int:workplace_bugfix_id>')
def delete_workplace_bugfix(workplace_bugfix_id: int) -> Response:
    """
    Delete workplace bugfix record
    ---
    tags:
      - WorkplaceBugfix
    parameters:
      - in: path
        name: workplace_bugfix_id
        type: integer
        required: true
        description: Workplace bugfix ID
    responses:
      200:
        description: Workplace bugfix deleted successfully
      404:
        description: Record not found
    """
    workplace_bugfix_controller.delete(workplace_bugfix_id)
    return make_response("WorkplaceBugfix deleted", HTTPStatus.OK)
