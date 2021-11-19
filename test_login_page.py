from pages.login_page import LoginPage
import allure

link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
@allure.title('Allure testing')
@allure.severity('Blocker')
def test_should_be_login_page(browser):
    page = LoginPage(browser, link)
    with allure.step('Step 1'):
        page.open()
    with allure.step('Step 2'):
        page.should_be_login_page()
