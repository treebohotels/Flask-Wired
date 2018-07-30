import os
import structlog
import click
from flask import Flask

from flagon.extensions import db, ma

logger = structlog.get_logger()


def create_app():
    click.echo("Creating App with name: %s" % __name__)
    app = Flask(__name__, instance_relative_config=True, instance_path=os.environ.get('FLASK_APP_INSTANCE_PATH'))
    setup_config(app)
    bps = get_blueprints(app)
    register_blueprints(app, bps)
    register_extensions(app)
    configure_logging(app)
    return app


def setup_config(app):
    app_name = os.environ.get('APP_NAME')
    environment = os.environ.get('APP_ENV')
    click.echo("Using environment: %s" % environment)
    app.config.from_object(app_name + '.settings.' + environment)
    # app.config.from_pyfile(app_name + 'settings' + environment, silent=True)


def get_blueprints(app):
    return app.config['BPS']


def register_blueprints(app, bps):
    for bp in bps:
        app.register_blueprint(bp)


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)


def configure_logging(app):
    import logging
    import sys

    from pythonjsonlogger import jsonlogger

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(jsonlogger.JsonFormatter())
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    app.logger.addHandler(handler)


def get_logging_config():
    logging_conf = {
        'filters': {
            'request_id': {
                '()': 'prometheus.log_filters.RequestIdFilter'
            }
        },
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'level': 'INFO', 'class': 'logging.StreamHandler',
                'formatter': 'verbose',
                'filters': ['request_id'],
            },
        }
    }
    import structlog

    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.stdlib.render_to_log_kwargs,
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
