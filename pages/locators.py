from selenium.webdriver.common.by import By

class BasePageLocators():
    """
    Универсальные базовые локаторы
    """
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class BasketPageLocators():
    """
    Локаторы страницы корзины с товарами
    """
    BASKET_PRODUCTS = (By.CSS_SELECTOR, '.basket-title.hidden-xs')
    BASKET_PRODUCTS_TEXT = (By.CSS_SELECTOR, '#content_inner > p')

class LoginPageLocators():
    """
    Локаторы для страницы Регистрации\Авторизации
    """
    BUTTON_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTION_EMAIL_STRING = (By.ID, 'id_registration-email')
    REGISTION_PASSWORD_STRING = (By.ID, 'id_registration-password1')
    REGISTION_REPEATED_PASSWORD_STRING = (By.ID, 'id_registration-password2')


class MainPageLocators():
    """
    Локаторы для главной страницы
    """
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class ProductPageLocators():
    """
    Локаторы для страницы товара
    """
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    CONFIRMATION_NAME_PRODUCT = (By.CSS_SELECTOR, "#messages :nth-child(1) strong")
    CONFIRMATION_PRICE_PRODUCT = (By.CSS_SELECTOR, "#messages :nth-child(2) strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main>h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alert-success')

