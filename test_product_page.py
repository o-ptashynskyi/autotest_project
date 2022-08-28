from .pages.product_page import ProductPage
import time
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest


@pytest.mark.new
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(self.browser, link)
        page.open()
        mail = str(time.time()) + "@fakemail.org"
        passw = str(time.time() + 20)
        page.register_new_user(mail, passw)
        time.sleep(6)
        page.should_be_authorized_user()


    def test_user_can_add_product_to_basket(self, browser):
        self.browser = browser
        link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/?promo=newYear'
        page = ProductPage(self.browser, link)
        page.open()
        product_name = page.recieve_product_name().text
        product_price = page.recieve_product_value().text
        page.add_product_to_basket()
        time.sleep(2)
        name_in_message = page.recieve_name_from_message().text
        total_in_message = page.recieve_total_from_message().text
        assert product_name == name_in_message, 'Product name is not correct'
        assert product_price == total_in_message, 'Product price is not correct'
        time.sleep(2)

    def test_user_cant_see_success_message(self, browser):
        self.browser = browser
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_success_message()


def test_guest_can_add_product_to_basket(browser, link):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = ProductPage(browser, link)
        page.open()
        product_name = page.recieve_product_name().text
        product_price = page.recieve_product_value().text
        page.add_product_to_basket()
        time.sleep(3)
        name_in_message = page.recieve_name_from_message().text
        total_in_message = page.recieve_total_from_message().text
        assert product_name == name_in_message, 'Product name is not correct'
        assert product_price == total_in_message, 'Product price is not correct'
        time.sleep(3)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    time.sleep(5)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket
    
