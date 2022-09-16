from selenium.common.exceptions import \
    NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

import math

class BasePage():
    """
    Класс для базовых функций, которые могут использоваться на любой странице сайта
    """
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        #Переход на страницу авторизации
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        #Переход на страницу с корзиной
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def is_disappeared(self, how, what, timeout=4):
        #Проверка того, что элемент исчезает со страницы
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        #Проверка присутствия элемента есть на странице
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        #Проверка отсутвия элемента нет на странице
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):
        #Переход по ссылке
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        #Проверка того, что пользователь авторизован
        assert self.is_element_present(*BasePageLocators.USER_ICON), "Иконка пользователя не отображается," \
                                                                    " вероятно, пользователь не авторизован"
    def should_be_login_link(self):
        #Проверка наличия ссылки на страницу авторизации
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Ссылка для авторизации не представлена"

    def solve_quiz_and_get_code(self):
        #Расчет значения для решения задачки и вставка результата в алерт, возникающий при добавлении товара в корзину
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Ваш код: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("Второго алерта не было")

    def text_comparision(self, how, what, text_to_search):
        #Сравнение переданного текста с текстом элемента на странице
        try:
            founded_text = self.browser.find_element(how, what).text
            founded_text = founded_text.strip()

        except NoSuchElementException:
            print('Элемент на странице не обнаружен')
            return False

        return text_to_search == founded_text