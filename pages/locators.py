from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    # реализуйте проверку, что есть форма логина
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    # реализуйте проверку, что есть форма регистрации на странице
    REGISTERED_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.XPATH, "//button[@value=\"Add to basket\"]")
    MESSAGE_ADDED_TO_CART_PRODUCT_NAME = (By.XPATH, "//*[@id=\"messages\"]/div[1]/div/strong")
    PRODUCT_NAME = (By.XPATH, "//*[@id=\"content_inner\"]/article/div[1]/div[2]/h1")
    PRODUCT_PRICE = (By.XPATH, "//*[@id=\"content_inner\"]/article/div[1]/div[2]/p[1]")
    PRODUCT_PRICE_FROM_MESSAGE = (By.XPATH, "//*[@id=\"messages\"]/div[3]/div/p[1]/strong")
