from .base_page import BasePage
from .locators import LoginPagelocators
from selenium import webdriver
import requests


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        print("\nURL is Correct")
        self.should_be_login_form()
        print("Login form is Correct")
        self.should_be_register_form()
        print("Register form is Correct")

    def should_be_login_url(self):
        self.browser.current_url == ("http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"), "Wrong URL address"
        assert True

    def should_be_login_form(self):
        self.is_element_present(*LoginPagelocators.LOGIN_EMAIL), "No email field"
        assert True
        self.is_element_present(*LoginPagelocators.LOGIN_PASSWORD), "No password field"
        assert True
        self.is_element_present(*LoginPagelocators.BUTTON_LOGIN), "No such button detected"
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPagelocators.REGISTER_EMAIL), "No email field"
        assert True
        self.is_element_present(*LoginPagelocators.REGISTER_PASSWORD), "No password field"
        assert True
        self.is_element_present(*LoginPagelocators.BUTTON_REGISTER), "No such button detected"
        assert True
        self.is_element_present(*LoginPagelocators.CONFIRM_PASSWORD), "No such field detected"
        assert True