import time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.login_page
@pytest.mark.main_page
def test_guest_can_go_to_login_page(browser):
   LINK = "http://selenium1py.pythonanywhere.com/"
   page = MainPage(browser, LINK)
   page.open()
   page.go_to_login_page()
   login_page = LoginPage(browser, browser.current_url)
   login_page.should_be_login_page()

@pytest.mark.login_page
@pytest.mark.main_page
def test_guest_should_see_login_link(browser):
   LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
   page = MainPage(browser, LINK)
   page.open()
   page.should_be_login_link()

@pytest.mark.login_page
def test_find_reg_log_form_and_logurl(browser):
   LINK = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
   login_page = LoginPage(browser, LINK)
   login_page.open()
   login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
   LINK = 'http://selenium1py.pythonanywhere.com/'
   page = MainPage(browser, LINK)
   page.open()
   page.go_to_basket_page()
   basket_page = BasketPage(browser, browser.current_url)
   basket_page.should_not_be_product_in_the_basket()
   basket_page.checking_the_text_about_an_empty_basket()