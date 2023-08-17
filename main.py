"""Скрипт отбращается к rambler.ru. записывает слово тестирование в поле поиска и сравнивает ссылку"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://comments-school-1.testkontur.ru/comments/preview/1/default/test")
search_fields = driver.find_element(By.XPATH, '//*[@id="commentsRoot"]/div/div/div[2]/div/div/div[2]/div[1]/div/div')
assert search_fields.text == "Войдите"


print(search_fields)
#search_fields.send_keys("Тестирование")
#search_fields.send_keys(Keys.ENTER)

#header = driver.find_element(By.TAG_NAME, "h3")
#assert header.text == 'Тестирование программного обеспечения - Википедия'


sleep(10)
driver.close()
