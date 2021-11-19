from python_pages.tutorial import Tutorial
import time

base_link = "https://stepik.org/lesson/265077/step/6?unit=246025"

def test_sending_answer(browser):
    page = Tutorial(browser, base_link)
    page.open()
    time.sleep(5)
    page.sending_an_answer()