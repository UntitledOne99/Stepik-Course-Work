from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
   def basket_empty_message(self):
       basketItems = (self.browser.find_element(*BasketPageLocators.BASKET_ITEMS)).text
       assert basketItems == "Your basket is empty. Continue shopping"
