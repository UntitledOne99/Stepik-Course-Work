import pytest
from pages.product_page import ProductPage

base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


#def test_guest_can_buy_a_book(browser):
    #page = ProductPage(browser, link)
    #page.open()
    # page.product_function()
urls = [f"{base_link}/?promo=offer{i}" for i in range(10)]
@pytest.mark.parametrize('link',urls)
@pytest.mark.xfail
def test_guest_can_buy_a_book(browser,link):
    page = ProductPage(browser,link)
    page.open()
    page.product_function()

