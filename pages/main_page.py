from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    """
    Класс главной страницы
    """
    
    def __init__(self, *args, **kwargs):
        #Наследует все функции из базовой страницы - BasePage
        super(MainPage, self).__init__(*args, **kwargs)