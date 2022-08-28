from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
        assert empty_basket_message, 'Basket should be empty, but its not'
