"""Скрипт отбращается к rambler.ru. записывает слово тестирование в поле поиска и сравнивает ссылку"""

import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from conftest import driver

def test_searchTesting(driver):
    search_ = driver.find_element(By.CLASS_NAME, "data-c71-header")
    assert search_.text == 'Превью комментариев'



def test_comment(driver):
    search_fields = driver.find_element(By.CLASS_NAME, "c71-author__name")
    assert search_fields.text == 'Александр Пушкин'

    print(search_fields.text)
    #search_fields.send_keys("Комментарии")
    #search_fields.send_keys(Keys.ENTER)

    text_ = driver.find_element(By.CLASS_NAME, "c71-author__text")
    assert text_.text == 'Тест!'

    print(text_.text)


