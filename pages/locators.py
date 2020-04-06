from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    YOUR_BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    # реализуйте проверку, что есть форма логина
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    # реализуйте проверку, что есть форма регистрации на странице
    REGISTERED_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDRESS_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.XPATH, "//button[@value=\"Add to basket\"]")
    MESSAGE_ADDED_TO_CART_PRODUCT_NAME = (By.XPATH, "//*[@id=\"messages\"]/div[1]/div/strong")
    PRODUCT_NAME = (By.XPATH, "//*[@id=\"content_inner\"]/article/div[1]/div[2]/h1")
    PRODUCT_PRICE = (By.XPATH, "//*[@id=\"content_inner\"]/article/div[1]/div[2]/p[1]")
    PRODUCT_PRICE_FROM_MESSAGE = (By.XPATH, "//*[@id=\"messages\"]/div[3]/div/p[1]/strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

class BasketPageLocators():
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset > div")
