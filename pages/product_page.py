from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class ProductPage(BasePage):
    def product_function(self):
        #self.should_be_right_url()
        self.additing_into_cart()
        self.solve_quiz_and_get_code()
        self.price_of_the_book()
        self.name_of_the_book()

    def should_be_right_url(self):
        self.browser.current_url == ("http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"), "Wrong URL address"
        assert True
    def additing_into_cart(self):
        addIt = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        addIt.click()

    def name_of_the_book(self):
        bookName = (self.browser.find_element(*ProductPageLocators.NAME_OF_THE_BOOK)).text
        nameUp =(self.browser.find_element(*ProductPageLocators.NAME_OF_THE_BOOK_UP)).text
        assert bookName == nameUp

    def price_of_the_book(self):
        price = (self.browser.find_element(*ProductPageLocators.PRICE_OF_THE_BOOK)).text
        basket = (self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)).text
        assert price == basket


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            #time.sleep(1)
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")