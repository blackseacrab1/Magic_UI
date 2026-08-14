from pages.base_page import BasePage
from pages.locators import product_locators as loc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    page_url = "/shop"

    def open_first_product(self):
        wait = WebDriverWait(self.driver, 10)
        link = wait.until(EC.element_to_be_clickable(loc.first_product_link))
        link.click()

    def check_product_title_visible(self):
        self.is_element_visible(loc.product_title)

    def check_not_available_message(self):
        self.is_element_visible(loc.not_available_text)

    def check_contact_us_visible(self):
        self.is_element_visible(loc.contact_us_btn)

    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        btn = wait.until(EC.element_to_be_clickable(loc.add_to_cart_btn))
        btn.click()

    def check_cart_quantity(self, expected_qty):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(loc.cart_quantity))
        result = wait.until(
            EC.text_to_be_present_in_element(loc.cart_quantity, expected_qty)
        )
        assert result

    def click_terms_and_conditions(self):
        wait = WebDriverWait(self.driver, 10)
        link = wait.until(EC.element_to_be_clickable(loc.terms_link))
        link.click()

    def check_terms_title(self, expected_title):
        self.assert_text_equal(loc.terms_title, expected_title)
