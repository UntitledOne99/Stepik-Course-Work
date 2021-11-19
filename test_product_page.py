import time
import pytest
import allure
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
basket_link = "http://selenium1py.pythonanywhere.com/en-gb/basket/"


def test_guest_can_buy_a_book(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.product_function()

urls = [f"{base_link}/?promo=offer{i}" for i in range(10)]
@pytest.mark.parametrize('link',urls)
@pytest.mark.xfail
def test_guest_can_buy_a_book(browser,link):
    page = ProductPage(browser,base_link)
    page.open()
    page.product_function()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser,base_link)
    page.open()
    page.product_function()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser,base_link)
    basket_page = BasketPage(browser,basket_link)
    page.open()
    page.basket_function()
    basket_page.basket_empty_message()