from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    button = browser.find_element(By.ID, 'book')
    button.click()

    x = browser.find_element(By.ID, 'input_value').text
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(x))

    sub = browser.find_element(By.ID, 'solve')
    sub.click()

    alert = browser.switch_to.alert
    alert_text = alert.text

    pyperclip.copy(alert_text.split()[-1])
    '''
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, 'file.txt')
    send_file = browser.find_element(By.ID, 'file')
    send_file.send_keys(file_path)
    '''

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
