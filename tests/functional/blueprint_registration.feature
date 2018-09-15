Feature: Blueprint Registration

  Scenario: Blueprint Registration /ping
    Given A /ping Blueprint
    And A config with ping blueprint
    And A Flask-Wired Application with config
    When Accessing /ping
    Then I get a 200 Response
    And response body is pong

  Scenario: Blueprint Registration /ping
    Given A /ping Blueprint
    Given A /echo Blueprint
    And A config with ping and echo blueprints
    And A Flask-Wired Application with config multiple
    When GET /ping
    When GET /echo
    Then I get a 200 Response for /ping
    And /ping response body is pong
    And I get a 200 Response for /echo
    And /echo response body is echo

