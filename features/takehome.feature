Feature: Takehome zeachable

    Scenario: Validating Home page
        Given I am on Homepage
        Then I am validating url with "https://takehome.zeachable.com"

    Scenario: Auth user
        Given Auth User
        Then Validate that Profile icon exist

    Scenario: User is able to open Terms of Use
        Given I am on Homepage
        Then Click on tou
        Then Validate page title with text "takehome"

    Scenario: User is able to open Privacy Policy
        Given I am on Homepage
        Then Click on Privacy Policy
        Then Validate page title with text "takehome"

    Scenario: User Logout
        Given I am on Homepage
        Then Validate that Profile icon exist
        Then Logout User