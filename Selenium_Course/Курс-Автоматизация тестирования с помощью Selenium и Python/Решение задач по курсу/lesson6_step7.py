from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

# Функция для генерации случайной строки заданной длины
def random_string(length):
    letters = string.ascii_lowercase  # Можно добавить заглавные буквы или цифры, если нужно
    return ''.join(random.choice(letters) for _ in range(length))

try:
    # Создаем экземпляр драйвера
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # Находим все текстовые поля по локатору — в данном случае это 'input'
    elements = browser.find_elements(By.TAG_NAME, "input")

    # Заполняем каждое поле случайным текстом
    for element in elements:
        element.send_keys(random_string(8))  # Заполняем 8 случайными символами

    # Нажимаем кнопку отправки формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


