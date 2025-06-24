from selenium import webdriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.Locators import *

driver = webdriver.Chrome() #
driver.get('https://stellarburgers.nomoreparties.site/register')

class TestRegistration:
# регистрация с валидными данными
def test_registration_valid_data_sucsessful_registration(self,driver)

    driver.find_element(*Locators.reg_field_name).send_keys('Doodle')
    driver.find_element(*Locators.reg_field_email).send_keys('gribova_anna_24_123@ya.ru')
    driver.find_element(*Locators.reg_field_password).send_keys('123456')

    driver.find_element(*Locators.reg_button_register).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.login_page))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login' and login_page.text == 'Вход'
    driver.quit()

    #регистрация с неверным паролем
def test_registration_valid_data_show_error_message (self, driver)

    driver.find_element(*Locators.reg_field_name).send_keys('Doodle')
    driver.find_element(*Locators.reg_field_email).send_keys('gribova_anna_24_123@ya.ru')
    driver.find_element(*Locators.reg_field_password).send_keys('12345')

    driver.find_element(*Locators.reg_button_register).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(*Locators.reg_message_of_error)) #ждем появления сообщения об ошибке

    assert driver.find_element(*Locators.reg_message_of_error).text == 'Некорректный пароль'   #проверяем, что текст ошибки "Некорректный пароль"

    driver.quit()