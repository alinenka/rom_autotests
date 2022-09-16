from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    """
    Класс страницы товара
    """

    def add_product_in_cart(self):
        #Добавление товара в корзину
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def does_the_element_match(self):
        #Проверка совпадения цены и названия товара на странице продукта и в корзине
        self.does_the_name_matсh()
        self.does_the_price_match()

    def does_the_name_matсh(self):
        #Проверка совпадения названия товара на странице продукта и в корзине
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        conf_product_name = self.browser.find_element\
            (*ProductPageLocators.CONFIRMATION_NAME_PRODUCT).text
        assert product_name.lower() == conf_product_name.lower(), 'Наименования товара не совпадают или не обнаружены'

    def does_the_price_match(self):
        #Проверка совпадения цены товара на странице продукта и в корзине
        product_price = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        conf_product_price = self.browser.find_element\
            (*ProductPageLocators.CONFIRMATION_NAME_PRODUCT).text
        assert product_price.lower() == conf_product_price.lower(), 'Цены товара не совпадают или не обнаружены'

    def should_not_be_success_message(self):
        #Проверка отсутствия сообщения об удачном добавлении товара
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Ошибочно отображается сообщение об успешном добавлении товара в корзину"

    def dissappeared_success_message(self):
        #Проверка исчезнования сообщения об успешном добавлении в корзину
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Сообщение об успешном добавлении товара в корзину не пропало"