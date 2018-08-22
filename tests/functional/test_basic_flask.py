import pytest
from flask import Flask
from pytest_bdd import scenario, given, when, then, parsers


@scenario('basic_flask.feature', 'Basic Flask Application')
def test_hello_world_flask_application():
    pass


@pytest.fixture()
def scenario_context():
    return {}


@given('A Hello World Flask Application')
def hello_world_flask_app():
    app = Flask("hello_world")

    @app.route('/hello')
    def hello_world():
        return "Hello, World!!!"

    return app


@when(parsers.parse('Accessing {endpoint}'))
def http_get_endpoint(scenario_context, hello_world_flask_app, endpoint):
    client = hello_world_flask_app.test_client()
    response = client.get(endpoint)
    scenario_context['response'] = response
    parsers.parse('I get a {expected_status:d} Response')


@then(parsers.parse('I get a {expected_status:d} Response'))
def assert_response_status(scenario_context, expected_status):
    assert scenario_context['response'].status_code == expected_status


@then(parsers.parse('response body is {body}'))
def assert_response_body(scenario_context, body):
    assert str(scenario_context['response'].data, 'utf-8') == body
