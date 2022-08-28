from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGICTR_FORM = (By.CSS_SELECTOR, 'form#register_form')
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    CONFIRM_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    BASKET_TOTAL = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')