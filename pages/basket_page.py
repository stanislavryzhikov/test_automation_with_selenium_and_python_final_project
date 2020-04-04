from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Ожидаем, что в корзине нет товаров
    def should_not_be_goods_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Success message is presented, but should not be"

    # Ожидаем, что есть текст о том что корзина пуста
    def should_be_empty_basket_message(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE)
        basket_message_text = basket_message.text
        assert basket_message_text == "Your basket is empty. Continue shopping"
