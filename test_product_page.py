import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time

@pytest.mark.authorized_users
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        LINK = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        email = f'{time.time()}@fakemail.ru'
        password = 'Test_PaS7w0RD'
        login_page = LoginPage(browser, LINK)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        LINK = f'http://selenium1py.pythonanywhere.com' \
               f'/catalogue/coders-at-work_207/?promo=offer1'
        product_page = ProductPage(browser, LINK)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    @pytest.mark.parametrize(
        'promo',
        [
            pytest.param(x, marks=pytest.mark.xfail) if x == 7 else x for x in range(5, 8)
        ]
    )
    def test_user_can_add_product_to_basket(self, browser, promo):
        LINK = f'http://selenium1py.pythonanywhere.com' \
               f'/catalogue/coders-at-work_207/?promo=offer{promo}'
        product_page = ProductPage(browser, LINK)
        product_page.open()
        product_page.add_product_in_cart()
        product_page.solve_quiz_and_get_code()
        product_page.does_the_element_match()

@pytest.mark.need_review
@pytest.mark.parametrize(
    'promo',
    [
        pytest.param(x, marks=pytest.mark.xfail) if x == 7 else x for x in range(5,8)
    ]
)
def test_guest_can_add_product_to_basket(browser,promo):
    LINK = f'http://selenium1py.pythonanywhere.com' \
           f'/catalogue/coders-at-work_207/?promo=offer{promo}'
    product_page = ProductPage(browser, LINK)
    product_page.open()
    product_page.add_product_in_cart()
    product_page.solve_quiz_and_get_code()
    product_page.does_the_element_match()

@pytest.mark.xfail(reason="Известная ошибка. Скоро все починим")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    LINK = f'http://selenium1py.pythonanywhere.com' \
           f'/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, LINK)
    product_page.open()
    product_page.add_product_in_cart()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    LINK = f'http://selenium1py.pythonanywhere.com' \
           f'/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, LINK)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail(reason="Известная ошибка. Скоро все починим")
def test_message_disappeared_after_adding_product_to_basket(browser):
    LINK = f'http://selenium1py.pythonanywhere.com' \
           f'/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, LINK)
    product_page.open()
    product_page.add_product_in_cart()
    product_page.dissappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_the_basket()
    basket_page.checking_the_text_about_an_empty_basket()