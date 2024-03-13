from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os
import pyperclip


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window((new_window))

    val = browser.find_element(By.ID, 'input_value').text

    answer = browser.find_element(By.NAME, 'text')
    answer.send_keys(calc(val))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    # Отправляем заполненную форму
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text

    pyperclip.copy(alert_text.split()[-1])
    print(alert_text[-18:])

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
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
