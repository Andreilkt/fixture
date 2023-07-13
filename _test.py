"""Скрипт отбращается к rambler.ru. записывает слово тестирование в поле поиска и сравнивает ссылку"""
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.test.fixture()
def driver():
    driver = webdriver.Chrome() # это будет выполняться до теста
    driver.get("https://comments-school-1.testkontur.ru/comments/preview/1/default/test")
    yield driver # разграничиваем то, что до и после
    driver.close() # это будет выполняться после теста

def test_searchTesting(driver):
    search_fields = driver.find_element(By.NAME, "q")
    search_fields.send_keys("Тестирование")
    search_fields.send_keys(Keys.ENTER)

    header = driver.find_element(By.TAG_NAME, "h3")
    assert header.text == 'Превью комментариев'


    sleep(10)
    driver.close()

def test_comment(driver):
    search_fields = driver.find_element(By.NAME, "q")
    search_fields.send_keys("Комментарии")
    search_fields.send_keys(Keys.ENTER)

    header = driver.find_element(By.TAG_NAME, "h3")
    assert header.text == 'Превью комментариев'

