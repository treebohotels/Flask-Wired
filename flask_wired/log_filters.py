# coding=utf-8
"""
Log filters
"""
import logging
import flask


class RequestIdFilter(logging.Filter):
    """
    This is a logging filter that makes the request ID available for use in the logging format.
    Note that we're checking if we're in a request context, as we may want to log things before
    Flask is fully loaded
    """

    def filter(self, record):
        """
        filter
        :param record:
        :return:
        """
        if flask.has_request_context():
            if hasattr(flask.g, "request_id"):
                record.request_id = flask.g.request_id
        if not hasattr(record, "request_id"):
            record.request_id = ""
        return True
