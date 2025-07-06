import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import Locators
from urls import Urls
from qa_python_24k_sprint_5.utils.data import TestData

#ввод данных в форму "Вход"
@pytest.fixture
def login():
    driver = webdriver.Chrome()
    driver.get(*Urls.get_login)

    driver.find_element(*Locators.login_field_email).send_keys(*TestData.per_email)
    driver.find_element(*Locators.login_field_password).send_keys(*TestData.td_password)
    driver.find_element(*Locators.login_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located())
    return driver
    yield driver
    driver.quit()

#авторизация на сайте для дальнейших проверок
@pytest.fixture
def autorization():
    driver = webdriver.Chrome()
    driver.get(*Urls.get_main)

    driver.find_element(*Locators.main_button_login).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.login_page))

    driver.find_element(*Locators.login_field_email).send_keys(*TestData.per_email)
    driver.find_element(*Locators.login_field_password).send_keys(*TestData.td_password)
    driver.find_element(*Locators.login_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.main_button_order))
    yield driver
    driver.quit()

#открытие и закрытие браузера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(*Urls.get_main)
    yield driver
    driver.quit()