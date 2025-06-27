import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.Locators import *
from urls import Urls
from data import TestData

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

#авторизация на сайте для дальнейших проверок
@pytest.fixture
def autorization(login):
    driver = webdriver.Chrome()
    driver.get(*Urls.get_main)

    driver.find_element(*Locators.main_button_login).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.login_page))

    driver.login()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.main_button_order))
