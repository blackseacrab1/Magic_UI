from pages.basket_page import BasketPage


def test_basket_header_text(driver):
    basket_page = BasketPage(driver)
    basket_page.open_page()
    basket_page.check_text("Order overview")


def test_empty_cart_message(driver):
    basket_page = BasketPage(driver)
    basket_page.open_page()
    basket_page.check_cart_message("Your cart is empty!")


def test_about_us_visible(driver):
    basket_page = BasketPage(driver)
    basket_page.open_page()
    basket_page.check_about_us_text(
        "This is a demo shop just to practice automated testing skills. No orders will be delivered"
    )
