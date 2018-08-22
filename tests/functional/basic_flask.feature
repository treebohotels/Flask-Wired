Feature: Basic Flask Application

  Scenario: Basic Flask Application
    Given A Hello World Flask Application
    When Accessing /hello
    Then I get a 200 Response
    And response body is Hello, World!!!

