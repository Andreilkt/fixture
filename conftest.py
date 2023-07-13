import pytest
from selenium import webdriver

@pytest.test.fixture()
def driver():
    driver = webdriver.Chrome()  # это будет выполняться до теста
    driver.get("https://comments-school-1.testkontur.ru/comments/preview/1/default/test")
    yield driver  # разграничиваем то, что до и после
    driver.close()  # это будет выполняться после теста
