from pages.base_page import BasePage
from pages.locators import product_locators as loc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    page_url = "/shop/furn-9999-office-design-software-7?category=9"

    def check_product_title(self, expected_title):
        wait = WebDriverWait(self.driver, 10)
        title = wait.until(EC.visibility_of_element_located(loc.product_title))
        assert title.text == expected_title

    def check_not_available_message(self):
        wait = WebDriverWait(self.driver, 10)
        msg = wait.until(EC.visibility_of_element_located(loc.not_available_text))
        assert msg.is_displayed()

    def check_contact_us_visible(self):
        wait = WebDriverWait(self.driver, 10)
        btn = wait.until(EC.visibility_of_element_located(loc.contact_us_btn))
        assert btn.is_displayed()

    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        btn = wait.until(EC.element_to_be_clickable(loc.add_to_cart_btn))
        btn.click()

    def check_cart_quantity(self, expected_qty):
        wait = WebDriverWait(self.driver, 10)
        result = wait.until(
        EC.text_to_be_present_in_element(loc.cart_quantity, expected_qty)
        )
        assert result


    def click_terms_and_conditions(self):
        wait = WebDriverWait(self.driver, 10)
        link = wait.until(EC.element_to_be_clickable(loc.terms_link))
        link.click()


    def check_terms_title(self, expected_title):
        wait = WebDriverWait(self.driver, 10)
        title = wait.until(EC.visibility_of_element_located(loc.terms_title))
        assert title.text == expected_title
