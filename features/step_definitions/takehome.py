from pytest_bdd import scenarios, given, then, parsers, when
from selenium.webdriver.common.by import By


scenarios('', strict_gherkin=False)

@given("I am on Homepage")
def open_homepage(init_driver):
    init_driver.get("https://takehome.zeachable.com")

@given("Auth User")
def auth_user(init_driver):
    init_driver.get("https://sso.zeachable.com/secure/123/identity/login/password")
    init_driver.find_element(By.CSS_SELECTOR, "[id='email']").send_keys("test@test.com")
    init_driver.find_element(By.CSS_SELECTOR, "[id='password']").send_keys("123456")
    init_driver.find_element(By.CSS_SELECTOR, "[data-testid='login-button']").click()

@given("I am on Homepage")
def open_homepage(init_driver):
    init_driver.get("https://takehome.zeachable.com")

@then(parsers.parse('I am validating url with "{PATH}"'))
def validate_sign_up_page(init_driver, PATH):
   assert PATH in init_driver.current_url, f"{PATH} not in {init_driver.current_url}"

@then(parsers.parse('Validate that Profile icon exist'))
def validate_sign_up_page(init_driver):
    prifile = init_driver.find_element(By.CSS_SELECTOR, "[data-toggle='dropdown']")
    assert prifile.accessible_name == "test@test.com", 'Profile icon is not present'

@then(parsers.parse('Click on tou'))
def validate_sign_up_page(init_driver):
    init_driver.find_element(By.CSS_SELECTOR, "[href='/p/terms']").click()

@then(parsers.parse('Validate page title with text "{TEXT}"'))
def validate_page_title(init_driver, TEXT):
   assert TEXT in init_driver.title, f"{TEXT} not in {init_driver.title}"
