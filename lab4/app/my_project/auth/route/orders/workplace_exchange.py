from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import workplace_exchange_controller
from my_project.auth.domain import WorkplaceExchange

workplace_exchange_bp = Blueprint('WorkplaceExchange', __name__, url_prefix='/workplace-exchange')


@workplace_exchange_bp.get('')
def get_all_workplace_exchange() -> Response:
    """
    Get all workplace exchange records
    ---
    tags:
      - WorkplaceExchange
    responses:
      200:
        description: List of all workplace exchange records
    """
    return make_response(jsonify(workplace_exchange_controller.find_all()), HTTPStatus.OK)


@workplace_exchange_bp.post('')
def create_workplace_exchange() -> Response:
    """
    Create new workplace exchange record
    ---
    tags:
      - WorkplaceExchange
    parameters:
      - in: body
        name: workplace_exchange
        required: true
        description: Workplace exchange data
        schema:
          type: object
          properties:
            workplace_id:
              type: integer
              description: Workplace ID
            exchange_service_id:
              type: integer
              description: Exchange service ID
            notes:
              type: string
              description: Additional details
    responses:
      201:
        description: Workplace exchange created successfully
    """
    content = request.get_json()
    workplace_exchange = WorkplaceExchange.create_from_dto(content)
    workplace_exchange_controller.create(workplace_exchange)
    return make_response(jsonify(workplace_exchange.put_into_dto()), HTTPStatus.CREATED)


@workplace_exchange_bp.get('/<int:workplace_exchange_id>')
def get_workplace_exchange(workplace_exchange_id: int) -> Response:
    """
    Get workplace exchange by ID
    ---
    tags:
      - WorkplaceExchange
    parameters:
      - in: path
        name: workplace_exchange_id
        type: integer
        required: true
        description: Workplace exchange record ID
    responses:
      200:
        description: Workplace exchange record data
      404:
        description: Record not found
    """
    return make_response(jsonify(workplace_exchange_controller.find_by_id(workplace_exchange_id)), HTTPStatus.OK)


@workplace_exchange_bp.put('/<int:workplace_exchange_id>')
def update_workplace_exchange(workplace_exchange_id: int) -> Response:
    """
    Update workplace exchange record
    ---
    tags:
      - WorkplaceExchange
    parameters:
      - in: path
        name: workplace_exchange_id
        type: integer
        required: true
        description: Workplace exchange ID
      - in: body
        name: workplace_exchange
        description: Updated workplace exchange data
        required: true
        schema:
          type: object
          properties:
            workplace_id:
              type: integer
            exchange_service_id:
              type: integer
            notes:
              type: string
    responses:
      200:
        description: Workplace exchange updated successfully
      404:
        description: Record not found
    """
    content = request.get_json()
    workplace_exchange = WorkplaceExchange.create_from_dto(content)
    workplace_exchange_controller.update(workplace_exchange_id, workplace_exchange)
    return make_response("WorkplaceExchange updated", HTTPStatus.OK)


@workplace_exchange_bp.patch('/<int:workplace_exchange_id>')
def patch_workplace_exchange(workplace_exchange_id: int) -> Response:
    """
    Partially update workplace exchange record
    ---
    tags:
      - WorkplaceExchange
    parameters:
      - in: path
        name: workplace_exchange_id
        type: integer
        required: true
        description: Workplace exchange ID
      - in: body
        name: workplace_exchange
        description: Partial update data
        required: true
        schema:
          type: object
          properties:
            workplace_id:
              type: integer
            exchange_service_id:
              type: integer
            notes:
              type: string
    responses:
      200:
        description: Workplace exchange updated successfully
      404:
        description: Record not found
    """
    content = request.get_json()
    workplace_exchange_controller.patch(workplace_exchange_id, content)
    return make_response("WorkplaceExchange updated", HTTPStatus.OK)


@workplace_exchange_bp.delete('/<int:workplace_exchange_id>')
def delete_workplace_exchange(workplace_exchange_id: int) -> Response:
    """
    Delete workplace exchange record
    ---
    tags:
      - WorkplaceExchange
    parameters:
      - in: path
        name: workplace_exchange_id
        required: true
        type: integer
        description: Workplace exchange ID
    responses:
      200:
        description: Workplace exchange deleted successfully
      404:
        description: Record not found
    """
    workplace_exchange_controller.delete(workplace_exchange_id)
    return make_response("WorkplaceExchange deleted", HTTPStatus.OK)
