import pytest

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.product_page import BasePage
import time

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # зарегистрировать нового пользователя
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        base_page = BasePage(browser, link)
        base_page.open()
        base_page.go_to_login_page()
        login_page = LoginPage(browser, link)
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, "qwerTy5431")
        base_page.should_be_authorized_user()

    def test_user_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Гость открывает главную страницу
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        # Переходит в корзину по кнопке в шапке сайта
        base_page = BasePage(browser, link)
        base_page.go_to_basket()
        # Ожидаем, что в корзине нет товаров
        basket_page = BasketPage(browser, link)
        basket_page.should_not_be_goods_in_the_basket()
        # Ожидаем, что есть текст о том что корзина пуста
        basket_page.should_be_empty_basket_message()

    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Гость открывает страницу товара
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        # Переходит в корзину по кнопке в шапке
        base_page = BasePage(browser, link)
        # base_page.go_to_login_page()
        # login_page = LoginPage(browser, link)
        # email = str(time.time()) + "@fakemail.org"
        # login_page.register_new_user(self, email, "qwerTy")
        base_page.go_to_basket()
        # Ожидаем, что в корзине нет товаров
        basket_page = BasketPage(browser, link)
        basket_page.should_not_be_goods_in_the_basket()
        # Ожидаем, что есть текст о том что корзина пуста
        basket_page.should_be_empty_basket_message()

# pytest -s -v --tb=line --language=en test_product_page_6.py
