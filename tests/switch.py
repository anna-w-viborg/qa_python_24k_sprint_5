from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.Locators import *

class Switchers():
#после авторизации клик по кнопке "Личный кабинет" открывает личный кабинет
    def test_button_personal_go_to_personal (self, autorization):

        autorization()

        driver.find_element(*Locators.main_button_personal).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.button_profile)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
    deiver.quit()

#после авторизации из Личного кабинета клик по кнопке "Конструктор" перебрасывает на главную страницу со сборкой бургера
    def test_button_constructor_switch_to_main (self, autorization):
        autorization()
        driver.find_element(*Locators.main_button_personal).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.button_profile))

        driver.find_element(*Locators.button_constructor).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.main_button_order))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

#после авторизации из Личного кабинета клик по логотипу "Stellar Burgers" перебрасывает на главную страницу со сборкой бургера
    def test_button_logo_switch_to_main (self, autorization):
        autorization()
        driver.find_element(*Locators.main_button_personal).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.button_profile))

        driver.find_element(*Locators.logo).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.main_button_order))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit())

