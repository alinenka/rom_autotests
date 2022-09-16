from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    """
    Класс страницы Регистрации/Авторизации
    """
    def should_be_login_page(self):
        #Ряд проверок: url страницы, формы авторизации, формы регистрации
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        # Проверка наличия формы авторизации
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert True, 'На странице отсутствует форма авторизации'

    def should_be_login_url(self):
        #Проверка url страницы на наличие "login"
        url = self.browser.current_url
        assert 'login' in url, 'В url страницы нет "login"'

    def should_be_register_form(self):
        #Проверка наличия формы регистрации
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert True, 'На странице отсутствует форма регистрации'

    def register_new_user(self, email, password):
        #Регистрация нового пользователя

        email_string = self.browser.find_element(*LoginPageLocators.REGISTION_EMAIL_STRING)
        email_string.send_keys(email)

        password_string = self.browser.find_element(*LoginPageLocators.REGISTION_PASSWORD_STRING)
        password_string.send_keys(password)

        repeated_password_string = self.browser.find_element(*LoginPageLocators.REGISTION_REPEATED_PASSWORD_STRING)
        repeated_password_string.send_keys(password)

        button = self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT)
        button.click()