from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.Locators import *
from urls import Urls

class MainButtons():




#проверка клика по соусам
    def test_click_sauces_scroll_to_sauces(self):
        driver = webdriver.Chrome()
        driver.get(*Urls.get_main)
        driver.find_element(*locators.button_sauces).click()
        WebDriverWait(driver, 5)until(expected_conditions.visibility_of_element_located(*locators.h_sauces)

        assert driver.find_element(*Locators.h_fillings).text == 'Соусы'
    driver.quit()

#проверка клика по начинкам
    def test_click_fillings_scroll_to_fillings(self):
        driver.get(*Urls.get_main)
        driver.find_element(*locators.button_fillings).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*locators.h_fillings)

        assert driver.find_element(*Locators.h_fillings).text == 'Начинки'
    driver.quit()

    # проверка клика по булкам

    def test_click_bans_scroll_to_bans(self):
        driver = webdriver.Chrome()
        driver.get(*Urls.get_main)

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*locators.h_sauces)

        assert driver.find_element(*Locators.h_bans).text == 'Булки'
    driver.quit()