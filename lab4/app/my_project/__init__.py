import os
import secrets
from typing import Dict, Any

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from .auth.route import register_routes

# CONFIG KEYS
SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"

db = SQLAlchemy()

todos = {}


def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    """
    Main application factory.
    """

    # safely merge DB credentials
    _process_input_config(app_config, additional_config)

    app = Flask(__name__)

    # generate secure random key
    app.config["SECRET_KEY"] = secrets.token_hex(16)

    # merge user config into app config
    app.config.update(app_config)

    # setup DB
    _init_db(app)

    # register API routes
    register_routes(app)

    return app


def _init_db(app: Flask) -> None:
    """
    Initializes DB, creates database if missing, imports models, creates tables.
    """
    db.init_app(app)

    # create database if it does not exist
    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    # Correct import of domain models
    # This guarantees SQLAlchemy discovers models
    from .auth import domain

    with app.app_context():
        db.create_all()


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    """
    Fills in database credentials either from environment or from YAML config.
    No KeyError possible.
    """
    additional_config = additional_config or {}

    root_user = (
        os.getenv(MYSQL_ROOT_USER)
        or additional_config.get(MYSQL_ROOT_USER)
    )

    root_password = (
        os.getenv(MYSQL_ROOT_PASSWORD)
        or additional_config.get(MYSQL_ROOT_PASSWORD)
    )

    if not root_user or not root_password:
        print("⚠ Warning: MYSQL_ROOT_USER or MYSQL_ROOT_PASSWORD is missing. "
              "If your SQL URI needs formatting, DB connection may fail.")

    # format SQL URI if it contains {} placeholders
    uri = app_config.get(SQLALCHEMY_DATABASE_URI)

    if isinstance(uri, str) and ("{}" in uri or "{0}" in uri):
        app_config[SQLALCHEMY_DATABASE_URI] = uri.format(root_user, root_password)
    else:
        app_config[SQLALCHEMY_DATABASE_URI] = uri
