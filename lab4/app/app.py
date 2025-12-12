import os
import yaml

from waitress import serve
from dotenv import load_dotenv
from my_project import create_app

load_dotenv()

DEVELOPMENT_PORT = 5000
PRODUCTION_PORT = 8080
HOST = "0.0.0.0"
DEVELOPMENT = "development"
PRODUCTION = "production"

CONFIG_PATH = "config.yaml"

if __name__ == '__main__':
    # ---- REQUIRED ENV VARS ----
    required_env_vars = [
        'DATABASE_HOST',
        'DATABASE_NAME',
        'DATABASE_USER',
        'DATABASE_PASSWORD'
    ]
    missing_vars = [var for var in required_env_vars if not os.environ.get(var)]

    if missing_vars:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing_vars)}\n"
            f"Please check your .env file."
        )

    # ---- LOAD YAML CONFIG ----
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            yaml_config = yaml.safe_load(f)
    else:
        yaml_config = {}

    additional_config = yaml_config.get("ADDITIONAL_CONFIG", {})

    flask_env = os.getenv('FLASK_ENV', DEVELOPMENT).lower()

    # ---- FLASK RUNTIME CONFIG ----
    db_user = os.getenv('DATABASE_USER')
    db_password = os.getenv('DATABASE_PASSWORD')
    db_host = os.getenv('DATABASE_HOST')
    db_name = os.getenv('DATABASE_NAME')

    config = {
        'DEBUG': os.getenv('DEBUG', 'False').lower() == 'true',
        'SQLALCHEMY_DATABASE_URI': f'mysql://{db_user}:{db_password}@{db_host}/{db_name}',
        'SQLALCHEMY_TRACK_MODIFICATIONS': os.getenv(
            'SQLALCHEMY_TRACK_MODIFICATIONS',
            'False'
        ).lower() == 'true'
    }

    # ---- START APP ----
    app = create_app(config, additional_config)

    if flask_env == DEVELOPMENT:
        app.run(host=HOST, port=DEVELOPMENT_PORT, debug=True)

    elif flask_env == PRODUCTION:
        serve(app, host=HOST, port=PRODUCTION_PORT)
