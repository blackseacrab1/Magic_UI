from pages.base_page import BasePage
from pages.locators import basket_locators as loc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):
    page_url = "/shop/cart"

    def check_text(self, expected_text):
        header_text = self.find(loc.header_text_loc)
        assert header_text.text == expected_text

    def check_empty_cart_message(self):
        wait = WebDriverWait(self.driver, 10)
        msg = wait.until(EC.visibility_of_element_located(loc.empty_cart_text))
        assert msg.text == "Your cart is empty!"


    def check_about_us_text(self):
        wait = WebDriverWait(self.driver, 10)
        text = wait.until(EC.visibility_of_element_located(loc.about_us_text))
        assert "demo shop" in text.text
