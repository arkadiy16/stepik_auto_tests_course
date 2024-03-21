import pytest
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


answer = math.log(int(time.time()))


def test_autorization(browser):
    link = f" https://stepik.org/lesson/236895/step/1"
    browser.get(link)

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#ember416")))
    btn_login = browser.find_element(By.CSS_SELECTOR, "#ember416")
    btn_login.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="login"]')))
    inp_email = browser.find_element(By.CSS_SELECTOR, 'input[name="login"]')
    inp_email.send_keys('Arkadiy160702@gmail.com')

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="password"]')))
    inp_passw = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    inp_passw.send_keys('Microlab160702SO')

    btn_signup = browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn.button_with-loader')
    btn_signup.click()

    WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.modal-dialog-inner')))
    print(1)

