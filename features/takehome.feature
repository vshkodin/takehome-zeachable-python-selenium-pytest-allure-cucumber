Feature: Takehome zeachable

    Scenario: Validating Home page
        Given I am on Homepage
        Then I am validating url with "https://takehome.zeachable.com"

    Scenario: Auth user
        Given Auth User
        Then Validate that Profile icon exist

    Scenario: User is able to open Privacy Policy
        Given I am on Homepage
        Then Click on tou