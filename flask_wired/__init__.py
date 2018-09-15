from flask import Flask

FlaskWired = Flask


def create_app(config):
    app = Flask(__name__)
    setup_config(app, config)
    bps = get_blueprints(app)
    register_blueprints(app, bps)
    return app


def setup_config(app, config):
    app.config.from_object(config)


def get_blueprints(app):
    return app.config['BPS']


def register_blueprints(app, bps):
    for bp in bps:
        app.register_blueprint(bp)
