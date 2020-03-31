from .pages.product_page import ProductPage
import time

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    product_page = ProductPage(browser, link)
    product_page.open()
    # Добавляем товар в корзину
    product_page.add_to_basket()
    #  Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара
    product_page = ProductPage(browser, link)
    product_page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    product_page = ProductPage(browser, link)
    product_page.open()
    # Добавляем товар в корзину
    product_page.add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    product_page.should_disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# pytest -s -v --tb=line --language=en test_product_page_3.py