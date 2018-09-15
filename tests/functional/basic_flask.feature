Feature: Basic Flask Application

  Scenario: Flask-Wired Hello World
    Given A Hello World Flask-Wired Application
    When Accessing /hello
    Then I get a 200 Response
    And response body is Hello, World!!!

  Scenario: Basic Flask-Wired Application
    Given A Hello World Flask-Wired Application
    When Accessing /hello
    Then I get a 200 Response
    And response body is Hello, World!!!
