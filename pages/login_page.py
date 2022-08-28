from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert 'login' in url, 'URL is not correct'

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form, 'Login form is not exsist'

    def should_be_register_form(self):
        registr_form = self.browser.find_element(*LoginPageLocators.REGICTR_FORM)
        assert registr_form, 'Registration form is not exsist'