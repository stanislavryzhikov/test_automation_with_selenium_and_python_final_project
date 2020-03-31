from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_added_to_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name.text
        product_name_from_message = self.browser.find_element(*ProductPageLocators.MESSAGE_ADDED_TO_CART_PRODUCT_NAME)
        product_name_from_message_text = product_name_from_message.text
        assert product_name_text == product_name_from_message_text

    def should_be_match_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_name_value = product_price.text
        product_price_from_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_FROM_MESSAGE)
        product_price_from_message_text = product_price_from_message.text
        assert product_name_value == product_price_from_message_text

    def should_not_be_success_message(self):
        # assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        # assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"