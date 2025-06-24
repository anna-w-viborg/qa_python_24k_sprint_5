import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.Locators import *

driver = webdriver.Chrome() #

#ввод данных в форму "Вход"
@pytest.fixture
def login():

    driver.get(https://stellarburgers.nomoreparties.site/login)

    driver.find_element(*Locators.login_field_email).send_keys('gribova_anna_24_123@ya.ru')
    driver.find_element(*Locators.login_field_password).send_keys('123456')
    driver.find_element(*Locators.login_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located())
    return driver

#авторизация на сайте для дальнейших проверок
@pytest.fixture
def autorization(login):
    driver.get(https: // stellarburgers.nomoreparties.site /)

    driver.find_element(*Locators.main_button_login).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.login_page))

    driver.login()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.main_button_order))
