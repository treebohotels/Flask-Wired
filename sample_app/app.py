from flask import Flask
from config import Config


def create_app(config_class=Config):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_class)
    from api import bp as api_bp
    flask_app.register_blueprint(api_bp, url_prefix='/api')
    return flask_app


app = create_app()
