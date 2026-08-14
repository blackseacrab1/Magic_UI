from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    page_url = ""

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(f"http://testshop.qa-practice.com{self.page_url}")

    def find(self, locator):
        return self.driver.find_element(*locator)

    def assert_text_equal(self, locator, expected_text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(locator))
        assert (
            element.text == expected_text
        ), f"Expected '{expected_text}', got '{element.text}'"

    def is_element_visible(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(locator))
        assert element.is_displayed(), f"Element {locator} is not visible"
