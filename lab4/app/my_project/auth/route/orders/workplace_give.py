from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import workplace_give_controller
from lab4.app.my_project.auth.domain import WorkplaceGive

workplace_give_bp = Blueprint('WorkplaceGive', __name__, url_prefix='/workplace-give')


@workplace_give_bp.get('')
def get_all_workplace_give() -> Response:
    """
    Get all workplace give records
    ---
    tags:
      - WorkplaceGive
    responses:
      200:
        description: List of all workplace give records
    """
    return make_response(jsonify(workplace_give_controller.find_all()), HTTPStatus.OK)


@workplace_give_bp.post('')
def create_workplace_give() -> Response:
    """
    Create new workplace give record
    ---
    tags:
      - WorkplaceGive
    parameters:
      - in: body
        name: workplace_give
        required: true
        description: Workplace give data
        schema:
          type: object
          properties:
            workplace_id:
              type: integer
              description: Workplace ID
            give_service_id:
              type: integer
              description: Give service ID
            notes:
              type: string
              description: Additional notes
    responses:
      201:
        description: Workplace give created successfully
    """
    content = request.get_json()
    workplace_give = WorkplaceGive.create_from_dto(content)
    workplace_give_controller.create(workplace_give)
    return make_response(jsonify(workplace_give.put_into_dto()), HTTPStatus.CREATED)


@workplace_give_bp.get('/<int:workplace_give_id>')
def get_workplace_give(workplace_give_id: int) -> Response:
    """
    Get workplace give record by ID
    ---
    tags:
      - WorkplaceGive
    parameters:
      - in: path
        name: workplace_give_id
        type: integer
        required: true
        description: Workplace give ID
    responses:
      200:
        description: Workplace give data
      404:
        description: Record not found
    """
    return make_response(jsonify(workplace_give_controller.find_by_id(workplace_give_id)), HTTPStatus.OK)


@workplace_give_bp.put('/<int:workplace_give_id>')
def update_workplace_give(workplace_give_id: int) -> Response:
    """
    Update workplace give record
    ---
    tags:
      - WorkplaceGive
    parameters:
      - in: path
        name: workplace_give_id
        required: true
        type: integer
        description: Workplace give ID
      - in: body
        name: workplace_give
        required: true
        description: Updated workplace give data
        schema:
          type: object
          properties:
            workplace_id:
              type: integer
            give_service_id:
              type: integer
            notes:
              type: string
    responses:
      200:
        description: Workplace give updated successfully
      404:
        description: Record not found
    """
    content = request.get_json()
    workplace_give = WorkplaceGive.create_from_dto(content)
    workplace_give_controller.update(workplace_give_id, workplace_give)
    return make_response("WorkplaceGive updated", HTTPStatus.OK)


@workplace_give_bp.patch('/<int:workplace_give_id>')
def patch_workplace_give(workplace_give_id: int) -> Response:
    """
    Partially update workplace give record
    ---
    tags:
      - WorkplaceGive
    parameters:
      - in: path
        name: workplace_give_id
        required: true
        type: integer
        description: Workplace give ID
      - in: body
        name: workplace_give
        required: true
        description: Partial update data
        schema:
          type: object
          properties:
            workplace_id:
              type: integer
            give_service_id:
              type: integer
            notes:
              type: string
    responses:
      200:
        description: Workplace give updated successfully
      404:
        description: Record not found
    """
    content = request.get_json()
    workplace_give_controller.patch(workplace_give_id, content)
    return make_response("WorkplaceGive updated", HTTPStatus.OK)


@workplace_give_bp.delete('/<int:workplace_give_id>')
def delete_workplace_give(workplace_give_id: int) -> Response:
    """
    Delete workplace give record
    ---
    tags:
      - WorkplaceGive
    parameters:
      - in: path
        name: workplace_give_id
        required: true
        type: integer
        description: Workplace give ID
    responses:
      200:
        description: Workplace give deleted successfully
      404:
        description: Record not found
    """
    workplace_give_controller.delete(workplace_give_id)
    return make_response("WorkplaceGive deleted", HTTPStatus.OK)
