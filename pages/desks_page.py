from pages.base_page import BasePage
from pages.locators import desks_locators as loc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DesksPage(BasePage):
    page_url = "/shop/category/desks-1"

    def click_first_product(self):
        wait = WebDriverWait(self.driver, 10)
        link = wait.until(EC.element_to_be_clickable(loc.first_product_link))
        link.click()

    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        btn = wait.until(EC.element_to_be_clickable(loc.add_to_cart_btn))
        btn.click()

    def check_continue_shopping_visible(self):
        self.is_element_visible(loc.continue_shopping_btn)

    def click_continue_shopping(self):
        wait = WebDriverWait(self.driver, 10)
        btn = wait.until(EC.element_to_be_clickable(loc.continue_shopping_btn))
        btn.click()

    def check_cart_quantity(self, expected_qty):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(loc.cart_quantity))
        result = wait.until(
            EC.text_to_be_present_in_element(loc.cart_quantity, expected_qty)
        )
        assert result

    def check_add_to_cart_visible(self):
        self.is_element_visible(loc.add_to_cart_btn)

    def check_product_title(self, expected_title):
        self.assert_text_equal(loc.product_title, expected_title)

    def click_logo(self):
        wait = WebDriverWait(self.driver, 10)
        logo = wait.until(EC.element_to_be_clickable(loc.logo_link))
        logo.click()

    def check_categories_title(self, expected_title):
        self.assert_text_equal(loc.categories_text, expected_title)
