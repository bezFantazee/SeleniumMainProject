from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_CARD_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success:first-of-type strong")
    ALERT_CARD_COST = (By.CSS_SELECTOR, ".alert-info strong")
    H1 = (By.CSS_SELECTOR, "h1")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main .price_color")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

