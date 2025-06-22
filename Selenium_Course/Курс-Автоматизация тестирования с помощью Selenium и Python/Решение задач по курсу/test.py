from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Путь к драйверу
driver_path = r'C:\Users\user\.cache\selenium\chromedriver\win64\127.0.6533.119\chromedriver.exe'

# Создаем объект Service для драйвера
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Открываем веб-страницу
    driver.get('https://www.python.org/')  # Замените на нужный URL

    # 1. Поиск элемента по ID
    element_by_id = driver.find_element(By.ID, 'about')  # Убедитесь, что 'about' существует
    print('Элемент найден по ID:', element_by_id.text)

    # 2. Поиск элемента по классу
    element_by_class = driver.find_element(By.CLASS_NAME, 'python-logo')  # Убедитесь, что класс правильный
    print('Элемент найден по классу:', element_by_class.text)

    # 3. Поиск элемента по имени тега
    element_by_tag_name = driver.find_element(By.TAG_NAME, 'h1')  # Убедитесь, что существует
    print('Элемент найден по имени тега:', element_by_tag_name.text)

    # 4. Поиск элемента по CSS селектору
    element_by_css = driver.find_element(By.CSS_SELECTOR, '.icon-jobs')  # Убедитесь, что класс существует
    print('Элемент найден по CSS селектору:', element_by_css.text)

    # 5. Поиск элемента по XPath
    element_by_xpath = driver.find_element(By.XPATH, '//div[@class="small-widget documentation-widget"]/p')  # Проверить XPath
    print('Элемент найден по XPath:', element_by_xpath.text)

    # 6. Демо: Ввод текста в поле ввода
    input_field = driver.find_element(By.NAME, 'q')  # Используйте имя поля ввода
    input_field.send_keys('Текст для ввода')  # Ввод текста
    input_field.send_keys(Keys.RETURN)  # Нажимаем Enter

    time.sleep(3) # Подождите немного, чтобы увидеть изменения на странице

finally:
    # Закрываем браузер
    driver.quit()
