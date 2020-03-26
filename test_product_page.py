from .pages.product_page import ProductPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    # Открываем страницу товара
    # (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear). Обратите внимание,
    # что в ссылке есть параметр "?promo=newYear". Не теряйте его в авто-тесте, чтобы получить проверочный код.
    product_page = ProductPage(browser, link)
    product_page.open()

    # Нажимаем на кнопку "Добавить в корзину".
    product_page.add_to_basket()

# *Посчитать результат математического выражения и ввести ответ. Используйте для этого метод
# solve_quiz_and_get_code(), который приведен ниже. Например, можете добавить его в класс BasePage, чтобы
# использовать его на любой странице. Этот метод нужен только для проверки того, что вы написали тест на Selenium.
# После этого вы получите код, который нужно ввести в качестве ответа на данное задание. Код будет выведен в консоли
# интерпретатора, в котором вы запускаете тест. Не забудьте в конце теста добавить проверки на ожидаемый результат.
    product_page.solve_quiz_and_get_code()
    product_page.should_be_added_to_cart()
    product_page.should_be_match_price()
# pytest -s -v --tb=line --language=en test_product_page.py