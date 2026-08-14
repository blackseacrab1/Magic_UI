from pages.product_page import ProductPage


def test_product_title(driver):
    product_page = ProductPage(driver)
    product_page.open_page()
    product_page.open_first_product()
    product_page.check_product_title_visible()


def test_add_to_cart(driver):
    product_page = ProductPage(driver)
    product_page.open_page()
    product_page.open_first_product()
    product_page.add_to_cart()
    product_page.check_cart_quantity("1")


def test_terms_and_conditions(driver):
    product_page = ProductPage(driver)
    product_page.open_page()
    product_page.open_first_product()
    product_page.click_terms_and_conditions()
    product_page.check_terms_title("STANDARD TERMS AND CONDITIONS OF SALE")
