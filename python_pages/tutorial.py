from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Tutorial(BasePage):
    def sending_an_answer(self):
        testing_field = self.browser.find_element(By.XPATH,'//*[@id="ember68239"]/div/div[6]/div[1]/div/div/div/div[5]/div[2]/pre')