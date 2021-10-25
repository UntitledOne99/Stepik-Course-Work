import pytest
from pages.basket_page import BasketPage

base_link ="http://selenium1py.pythonanywhere.com/en-gb/basket/"

def success_message():
    page = BasketPage(browser,base_link)
    page.open()