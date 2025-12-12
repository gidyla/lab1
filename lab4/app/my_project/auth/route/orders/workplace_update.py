from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import workplace_update_controller
from my_project.auth.domain import WorkplaceUpdate

workplace_update_bp = Blueprint('WorkplaceUpdate', __name__, url_prefix='/workplace-update')


@workplace_update_bp.get('')
def get_all_workplace_update() -> Response:
    """
    Get all workplace update records
    ---
    tags:
      - WorkplaceUpdate
    responses:
      200:
        description: List of all workplace update records
    """
    return make_response(jsonify(workplace_update_controller.find_all()), HTTPStatus.OK)


@workplace_update_bp.post('')
def create_workplace_update() -> Response:
    """
    Create new workplace update record
    ---
    tags:
      - WorkplaceUpdate
    parameters:
      - in: body
        name: workplace_update
        required: true
        description: Workplace update data
        schema:
          type: object
          properties:
            workplace_id:
              type: integer
              description: Workplace ID
            update_service_id:
              type: integer
              description: Update service ID
            description:
              type: string
              description: Update details
    responses:
      201:
        description: Workplace update created successfully
    """
    content = request.get_json()
    workplace_update = WorkplaceUpdate.create_from_dto(content)
    workplace_update_controller.create(workplace_update)
    return make_response(jsonify(workplace_update.put_into_dto()), HTTPStatus.CREATED)


@workplace_update_bp.get('/<int:workplace_update_id>')
def get_workplace_update(workplace_update_id: int) -> Response:
    """
    Get workplace update record by ID
    ---
    tags:
      - WorkplaceUpdate
    parameters:
      - in: path
        name: workplace_update_id
        type: integer
        required: true
        description: Workplace update ID
    responses:
      200:
        description: Workplace update record
      404:
        description: Record not found
    """
    return make_response(jsonify(workplace_update_controller.find_by_id(workplace_update_id)), HTTPStatus.OK)


@workplace_update_bp.put('/<int:workplace_update_id>')
def update_workplace_update(workplace_update_id: int) -> Response:
    """
    Update workplace update record
    ---
    tags:
      - WorkplaceUpdate
    parameters:
      - in: path
        name: workplace_update_id
        required: true
        type: integer
        description: Workplace update ID
      - in: body
        name: workplace_update
        required: true
        description: Updated workplace update data
        schema:
          type: object
          properties:
            workplace_id:
              type: integer
            update_service_id:
              type: integer
            description:
              type: string
    responses:
      200:
        description: Workplace update updated successfully
      404:
        description: Record not found
    """
    content = request.get_json()
    workplace_update = WorkplaceUpdate.create_from_dto(content)
    workplace_update_controller.update(workplace_update_id, workplace_update)
    return make_response("WorkplaceUpdate updated", HTTPStatus.OK)


@workplace_update_bp.patch('/<int:workplace_update_id>')
def patch_workplace_update(workplace_update_id: int) -> Response:
    """
    Partially update workplace update record
    ---
    tags:
      - WorkplaceUpdate
    parameters:
      - in: path
        name: workplace_update_id
        required: true
        type: integer
        description: Workplace update ID
      - in: body
        name: workplace_update
        required: true
        description: Partial update data
        schema:
          type: object
          properties:
            workplace_id:
              type: integer
            update_service_id:
              type: integer
            description:
              type: string
    responses:
      200:
        description: Workplace update updated successfully
      404:
        description: Record not found
    """
    content = request.get_json()
    workplace_update_controller.patch(workplace_update_id, content)
    return make_response("WorkplaceUpdate updated", HTTPStatus.OK)


@workplace_update_bp.delete('/<int:workplace_update_id>')
def delete_workplace_update(workplace_update_id: int) -> Response:
    """
    Delete workplace update record
    ---
    tags:
      - WorkplaceUpdate
    parameters:
      - in: path
        name: workplace_update_id
        required: true
        type: integer
        description: Workplace update ID
    responses:
      200:
        description: Workplace update deleted successfully
      404:
        description: Record not found
    """
    workplace_update_controller.delete(workplace_update_id)
    return make_response("WorkplaceUpdate deleted", HTTPStatus.OK)
