from selenium.webdriver.common.by import By

first_product_link = (By.CSS_SELECTOR, "a.oe_product_image_link")
add_to_cart_btn = (By.ID, "add_to_cart")
continue_shopping_btn = (By.CSS_SELECTOR, "button.btn-secondary")
cart_quantity = (By.CSS_SELECTOR, ".my_cart_quantity")
product_title = (By.CSS_SELECTOR, "h1[itemprop='name']")
logo_link = (By.CSS_SELECTOR, "a.navbar-brand")
categories_text = (By.CSS_SELECTOR, "#top_menu .dropdown-toggle span")
