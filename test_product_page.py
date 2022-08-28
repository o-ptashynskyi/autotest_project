from .pages.product_page import ProductPage
import time
from selenium.webdriver.common.by import By

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    product_name = page.recieve_product_name().text
    product_price = page.recieve_product_value().text
    page.add_product_to_basket()
    time.sleep(5)
    name_in_message = page.recieve_name_from_message().text
    total_in_message = page.recieve_total_from_message().text
    assert product_name in name_in_message, 'Product name is not correct'
    assert product_price == total_in_message, 'Product price is not correct'
    time.sleep(10)
    


