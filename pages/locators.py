from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '[id="login_link"]')

class LoginPagelocators():
    REGISTER_EMAIL =(By.CSS_SELECTOR, "id_registration-email")
    REGISTER_PASSWORD =(By.CSS_SELECTOR, "id_registration-password1")
    CONFIRM_PASSWORD =(By.CSS_SELECTOR, "id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "registration_submit")
    LOGIN_EMAIL =(By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD =(By.CSS_SELECTOR, "#id_login-password")
    BUTTON_LOGIN =(By.CSS_SELECTOR, "login_submit")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '[value="Add to basket"]')
    NAME_OF_THE_BOOK_UP = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    NAME_OF_THE_BOOK = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRICE_OF_THE_BOOK = (By.CSS_SELECTOR, '[class="price_color"]')
    BASKET_TOTAL = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')