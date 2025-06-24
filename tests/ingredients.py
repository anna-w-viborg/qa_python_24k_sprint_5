from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.Locators import *

import locators #

driver = webdriver.Chrome()

#проверка клика по булкам
def test_click_bans_scroll_to_bans(self):
    driver.get(https://stellarburgers.nomoreparties.site/)
    driver.find_element(*locators.button_sauces).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*locators.h_sauces)

    driver.find_element(*locators.button_bans).click()

    assert driver.find_element(*Locators.h_bans) == 'Булки'
    driver.quit()




#проверка клика по соусам
def test_click_sauces_scroll_to_sauces(self):
    driver.get(https://stellarburgers.nomoreparties.site/)
    driver.find_element(*locators.button_sauces).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*locators.h_sauces)

    assert driver.find_element(*Locators.h_sauces) == 'Соусы'
    driver.quit()

#проверка клика по начинкам
def test_click_fillings_scroll_to_fillings(self):
    driver.get(https://stellarburgers.nomoreparties.site/)
    driver.find_element(*locators.button_fillings).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*locators.h_fillings)

    assert driver.find_element(*Locators.h_fillings) == 'Начинки'
    driver.quit()