import pytest
from flask.blueprints import Blueprint as bp
from pytest_bdd import scenario, given, when, then, parsers


@scenario('blueprint_registration.feature', 'Blueprint Registration /ping')
def test_hello_world_flask_wired_application():
    pass


@pytest.fixture()
def scenario_context():
    return {
        'response': {}
    }


@given("A /ping Blueprint")
def ping_blueprint():
    ping_bp = bp('ping', import_name="import_name")

    @ping_bp.route('/ping', )
    def hello_world():
        return "pong"

    return ping_bp


@given("A /echo Blueprint")
def echo_blueprint():
    echo_bp = bp('echo', import_name="import_name")

    @echo_bp.route('/echo', )
    def hello_world():
        return "echo"

    return echo_bp


@given("A config with ping blueprint")
def config(ping_blueprint):
    class Config(object):
        BPS = [ping_blueprint]

    return Config()


@given("A config with ping and echo blueprints")
def config_multiple(ping_blueprint, echo_blueprint):
    class Config(object):
        BPS = [ping_blueprint, echo_blueprint]

    return Config()


@given("A Flask-Wired Application with config")
def flask_wired_app(config):
    from flask_wired import create_app
    app = create_app(config)
    return app


@given("A Flask-Wired Application with config multiple")
def flask_wired_app_config_multiple(config_multiple):
    from flask_wired import create_app
    app = create_app(config_multiple)
    return app


@when(parsers.parse('Accessing {endpoint}'))
def http_get_endpoint(scenario_context, flask_wired_app, endpoint):
    client = flask_wired_app.test_client()
    response = client.get(endpoint)
    scenario_context['response'] = response


@then(parsers.parse('I get a {expected_status:d} Response for {endpoint}'))
def assert_response_status(scenario_context, endpoint, expected_status):
    assert scenario_context['response'][endpoint].status_code == expected_status


@then(parsers.parse('{endpoint} response body is {body}'))
def assert_response_body(scenario_context, endpoint, body):
    assert str(scenario_context['response'][endpoint].data, 'utf-8') == body


@when(parsers.parse("GET {endpoint}"))
def get(scenario_context, flask_wired_app_config_multiple, endpoint):
    client = flask_wired_app_config_multiple.test_client()
    response = client.get(endpoint)
    scenario_context['response'][endpoint] = response
