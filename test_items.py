import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestShopItems():

    def test_guest_should_see_basket_link_on_the_item_page(self, browser):
        browser.get(link)
        time.sleep(10)
        button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-baskeut")
        assert len(button) > 0, 'No add to basket button!'
