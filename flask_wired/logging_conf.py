# coding=utf-8
import os


def configure_logging(app):
    import logging.config
    environment = os.environ.get('APP_ENV', 'local')

    logging_conf = {
        'version': 1,
        'filters': {
            'request_id': {
                '()': 'prometheus.log_filters.RequestIdFilter'
            }
        },
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': "[%(asctime)s] %(levelname)s %(request_id)s - [%(name)s:%("
                          "lineno)s] %(message)s",
                'datefmt': "%Y-%m-%d %H:%M:%S"
            },
            'logstash': {
                '()': 'logstash_formatter.LogstashFormatterV1'
            }
        },
        'handlers': {
            'null': {
                'level': 'INFO', 'class': 'logging.NullHandler',
                'filters': ['request_id'],
            },
            'console': {
                'level': 'INFO', 'class': 'logging.StreamHandler',
                'formatter': 'verbose',
                'filters': ['request_id'],
            },
            'prometheus': {
                'level': 'DEBUG',
                'class': 'logging.handlers.WatchedFileHandler',
                'filename': app.config['LOG_ROOT'] + '/prometheus.log',
                'formatter': 'logstash' if environment == 'production' else 'verbose',
                'filters': ['request_id'],
            },
            'request': {
                'level': 'DEBUG',
                'class': 'logging.handlers.WatchedFileHandler',
                'filename': app.config['LOG_ROOT'] + '/request.log',
                'formatter': 'logstash' if environment == 'production' else 'verbose',
                'filters': ['request_id']
            }
        },
        'loggers': {
            'prometheus': {
                'handlers': ['console', 'prometheus'],
                'level': 'INFO' if environment == 'production' else 'DEBUG',
                'propagate': False
            },
            '': {
                'handlers': ['console'],
                'level': 'INFO' if environment == 'production' else 'DEBUG',
            },
            'request_handler': {
                'handlers': ['console', 'request'],
                'level': 'INFO' if environment == 'production' else 'DEBUG',
                'propagate': False
            }
        }
    }
    logging.config.dictConfig(logging_conf)
