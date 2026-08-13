from selenium.webdriver.common.by import By

product_title = (By.CSS_SELECTOR, "h1[itemprop='name']")
not_available_text = (By.CSS_SELECTOR, "#add_to_cart_wrap .text-danger")
contact_us_btn = (By.LINK_TEXT, "Contact Us")
add_to_cart_btn = (By.ID, "add_to_cart")
cart_quantity = (By.CSS_SELECTOR, ".my_cart_quantity")
breadcrumb_category = (By.CSS_SELECTOR, ".breadcrumb-item:nth-child(2) a")
terms_link = (By.CSS_SELECTOR, "a[href='/terms']")
terms_title = (By.TAG_NAME, "h1")
