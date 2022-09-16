from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    """
    Класс страницы с корзиной
    """

    def should_not_be_product_in_the_basket(self):
        #Проверка отсутствия товаров в корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), \
            "Ошибочно отображается сообщение о товаре в корзине"

    def checking_the_text_about_an_empty_basket(self):
        #Сверка текста об отсутствии товаров в корзине с положенным
       assert self.text_comparision(*BasketPageLocators.BASKET_PRODUCTS_TEXT,
                                    'Your basket is empty. Continue shopping'), \
           'Сообщение на сатйе не совпадает с "Your basket is empty. Continue shopping"'