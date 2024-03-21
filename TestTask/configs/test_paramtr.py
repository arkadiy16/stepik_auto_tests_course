import pytest
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


answer = math.log(int(time.time()))


@pytest.fixture(autouse=True)
def autorization(browser):
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


urls = ['https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1']


@pytest.mark.parametrize('url', urls)
def test_output_alien(browser, url):

    browser.get(url)

    try:
        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.quiz-component.ember-view textarea')))
        inp_answer = browser.find_element(By.CSS_SELECTOR, '.quiz-component.ember-view textarea')

        inp_answer.send_keys(math.log(int(time.time())))

        btn_submit = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
        btn_submit.click()
    except TimeoutException:
        pass

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))

    result_text = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text

    assert result_text == 'Correct!'




