import pytest
from pages.desks_page import DesksPage


@pytest.mark.smoke
def test_add_new_desk(driver):
    desks_page = DesksPage(driver)
    desks_page.open_page()
    desks_page.click_first_product()
    desks_page.add_to_cart()
    desks_page.check_continue_shopping_visible()
    desks_page.click_continue_shopping()


@pytest.mark.regression
def test_cart_quantity_after_add(driver):
    desks_page = DesksPage(driver)
    desks_page.open_page()
    desks_page.click_first_product()
    desks_page.add_to_cart()
    desks_page.click_continue_shopping()
    desks_page.check_cart_quantity("1")


@pytest.mark.smoke
def test_go_to_main_page(driver):
    desks_page = DesksPage(driver)
    desks_page.open_page()
    desks_page.click_logo()
    desks_page.check_categories_title("Categories")
