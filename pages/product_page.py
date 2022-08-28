from .base_page import BasePage
from .locators import ProductPageLocators
from . locators import BasketPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def recieve_product_value(self):
        product_value = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_value

    def recieve_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name

    def recieve_name_from_message(self):
        name_in_massage = self.browser.find_element(*ProductPageLocators.CONFIRM_MESSAGE)
        return name_in_massage

    def recieve_total_from_message(self):
        total_in_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        return total_in_message

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def success_message_is_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is not disappeared'

    def product_name_is_correct(self, page_name, message_name):
        assert page_name == message_name, 'Product name is not correct'

    def product_price_is_correct(self, page_price, message_price):
        assert page_price == message_price, 'Product price is not correct'

    