from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.Locators import * #

# вход по кнопке «Войти в аккаунт» на главной
class LoginVarious():
    def test_login_button_main_page_login_happen(self.login):
        driver = webdriver.Chrome()
        driver.get(*Urls.get_main)

        driver.find_element(*Locators.main_button_login).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.login_page))

        driver.login()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.main_button_order))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    drive.quit()

#вход по кнопке "Личный кабинет" на главной
    def test_personal_button_main_page_login_happen(self.login):
        driver = webdriver.Chrome()
        driver.get(*Urls.get_main)

        driver.find_element(*Locators.main_button_personal).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.login_page))

        driver.login()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.main_button_order))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    drive.quit()

#вход через кнопку "Войти" в форме регистрации
    def test_login_in_registration_form_login_happen (self, login):
        driver = webdriver.Chrome()
        driver.get(*Urls.get_main)

        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.login_page))

        driver.login()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.main_button_order))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    drive.quit()

#вход через  кнопку "Войти" в форме восстановления пароля
    def test_login_in_forgot_password_form_login_happen (self,login):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.login_page))

        driver.login()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.main_button_order))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    drive.quit()


