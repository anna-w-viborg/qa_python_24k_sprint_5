from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.Locators import *

import locators #

driver = webdriver.Chrome()

#после авторизации клик по кнопке "Выйти" выходит из аккаунта
def test_button_logout_click_logout_happen (self, autorization):
    driver = webdriver.Chrome()
    driver.autorization()

    driver.find_element(*locators.button_logout).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.main_button_login))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    drive.quit()