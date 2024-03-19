import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture()
def browser():
    print('\nStart new browser for test')
    driver = webdriver.Chrome()
    yield driver
    print('\n Quit browser')
    driver.quit()


@pytest.fixture(autouse=True)
def auto_fixture():
    print()
    print('asdfasgfskasodsgds')


class TestMainPage1():
    def test_guest_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.bascket-mini .btn-group > a')
