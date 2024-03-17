import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Test(unittest.TestCase):
    def case(self, link):
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(1)

        # Ваш код, который заполняет обязательные поля
        fname_element = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first')
        fname_element.send_keys('FooBar')
        lname_element = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.second')
        lname_element.send_keys('FooBar')
        email_element = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.third')
        email_element.send_keys('FooBar')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.case(link)

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.case(link)


if __name__ == "__main__":
    unittest.main()
