from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.product_page import BasePage
import time

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
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

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке
    base_page = BasePage(browser, link)
    base_page.go_to_basket()
    # Ожидаем, что в корзине нет товаров
    basket_page = BasketPage(browser, link)
    basket_page.should_not_be_goods_in_the_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_empty_basket_message()

# pytest -s -v --tb=line --language=en test_product_page_5.py