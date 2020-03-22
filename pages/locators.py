from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    # реализуйте проверку, что есть форма логина
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    # реализуйте проверку, что есть форма регистрации на странице
    REGISTERED_FORM = (By.CSS_SELECTOR, "#register_form")
