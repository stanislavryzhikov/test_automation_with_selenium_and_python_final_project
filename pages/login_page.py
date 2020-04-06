from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN_FORM is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTERED_FORM), "REGISTRED_FORM is not presented"

    def register_new_user(self, email, password):
        # заполнить Email address
        email_address_input = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_INPUT)
        email_address_input.send_keys(email)
        # заполнить Password
        password1_input = self.browser.find_element(*LoginPageLocators.PASSWORD1_INPUT)
        password1_input.send_keys(password)
        # заполнить Confirm password
        password2_input = self.browser.find_element(*LoginPageLocators.PASSWORD2_INPUT)
        password2_input.send_keys(password)
        # нажать Register
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()