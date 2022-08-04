from pytest_bdd import scenarios, given, then, parsers, when

scenarios('', strict_gherkin=False)

@given("I am on Homepage")
def open_homepage(init_driver):
    init_driver.get("https://takehome.zeachable.com")

@given("Auth User")
def auth_user(init_driver):
    init_driver.get("https://sso.zeachable.com/secure/123/identity/login/password")
    init_driver.find_element_by_css_selector("[id='email']").send_keys("test@test.com")
    init_driver.find_element_by_css_selector("[id='password']").send_keys("123456")
    init_driver.find_element_by_css_selector("[data-testid='login-button']").click()

@given("I am on Homepage")
def open_homepage(init_driver):
    init_driver.get("https://takehome.zeachable.com")

@then(parsers.parse('I am validating url with "{PATH}"'))
def validate_sign_up_page(init_driver, PATH):
   assert PATH in init_driver.current_url, f"{PATH} not in {init_driver.current_url}"
