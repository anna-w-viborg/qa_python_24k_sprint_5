import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import Locators
from urls import Urls

class TestMainButtons:

#проверка клика по соусам
    def test_click_sauces_scroll_to_sauces(self,driver):

        driver.find_element(*locators.button_sauces).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*locators.h_sauces))

        WebDriverWait(driver, 5).until(expected_conditions).presence_of_element_located(*Locators.h_active).is_displayed()
        active_tab = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.h_active))

        assert "Соусы" in active_tab.text

#проверка клика по начинкам
    def test_click_fillings_scroll_to_fillings(self, driver):

        driver.find_element(*locators.button_fillings).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*locators.h_fillings))

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.h_active)).is_displayed()
        active_tab = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.h_active))

        assert "Начинки" in active_tab.text

# проверка клика по булкам
    def test_click_bans_scroll_to_bans(self, driver):

        driver.find_element(*locators.button_bans).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*locators.h_bans))

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.h_active)).is_displayed()
        active_tab = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.h_active))

        assert "Булки" in active_tab.text


