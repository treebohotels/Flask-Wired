import flask
import uuid


def generate_request_id(original_id=''):
    """
    if an original request id is given return the same
    """
    if original_id:
        return original_id
    new_id = uuid.uuid4().hex
    return new_id


def request_id():
    """
    Returns the current request ID or a new one if there is none
    In order of preference:
    * If we've already created a request ID and stored it in the flask.g context local, use that
    * If a client has passed in the X-Request-Id header, create a new ID
    * Otherwise, generate a request ID and store it in flask.g.request_id

    """
    if getattr(flask.g, 'request_id', None):
        return flask.g.request_id
    headers = flask.request.headers
    original_request_id = headers.get("X-Request-Id")
    new_uuid = generate_request_id(original_request_id)
    flask.g.request_id = new_uuid
    return new_uuid
