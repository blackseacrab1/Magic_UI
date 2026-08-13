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
        wait = WebDriverWait(self.driver, 10)
        btn = wait.until(EC.visibility_of_element_located(
            loc.continue_shopping_btn))
        assert btn.is_displayed(), "error the button is not visivle"

    def click_continue_shopping(self):
        wait = WebDriverWait(self.driver, 10)
        btn = wait.until(EC.element_to_be_clickable(loc.continue_shopping_btn))
        btn.click()

    def check_cart_quantity(self, expected_qty):
        wait = WebDriverWait(self.driver, 10)
        qty = wait.until(
            EC.visibility_of_element_located(loc.cart_quantity)
        )
        wait.until(
            EC.text_to_be_present_in_element(loc.cart_quantity, expected_qty)
        )
        assert qty.text == expected_qty


    def click_logo(self):
        wait = WebDriverWait(self.driver, 10)
        logo = wait.until(
            EC.element_to_be_clickable(loc.logo_link)
        )
        logo.click()

    def check_on_main_page(self):
        wait = WebDriverWait(self.driver, 10)
        categories = wait.until(
        EC.visibility_of_element_located(loc.categories_text)
        )
        assert categories.text == "Categories"