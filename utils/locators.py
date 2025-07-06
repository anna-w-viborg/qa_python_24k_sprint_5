import pytest
from selenium.webdriver.common.by import By

class Locators:

    # для окна авторизации #

    reg_field_name = (By.XPATH, './/label[text()="Имя"]//parent*/input[@type="text" and @name="name"]')   #поле ввода имени
    reg_field_email = (By.XPATH, './/label[text()="Email"]//parent::*/input[@type="text" and @name="name"]')   #поле ввода почты
    reg_field_password = (By.XPATH, './/label[text()="Пароль"]//parent::*/input[@type="password" and @name="Пароль"')   #поле ввода пароля
    reg_button_register = (By.XPATH, './/button[text()="Зарегистрироваться"]') #кнопка "Зарегистрироваться"
    reg_message_of_error = (By.XPATH, './/p[contains(@class, "input__error")]') #сообщение о неверном пароле

    #для окна входа
    login_page = (By.XPATH, './/*[(@class = "Auth_login_3hAey")]') #вся страница с надписью "Вход"
    login_field_email = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")   #поле ввода почты
    login_field_password =(By.XPATH, ".//label[text()='Пароль']//parent::*/input[@type='password' and @name='Пароль']")
    login_button = (By.XPATH, ".//button[text()='Войти']")

    #кнопки входа на главной странице
    main_button_login = (By.XPATH, './/button[text()="Войти в аккаунт"]') #кнопка "Войти в аккаунт"
    main_button_personal = (By.XPATH, './/p[text()="Личный кабинет"]') #кнопка "Личный кабинет"

    #появлется после авторизации
    main_button_order = (By.XPATH, './/button[text()="Оформить заказ"') #кнопка "Оформить заказ"

    #проверка кнопок-переключателей
    button_profile = (By.XPATH, './/a[text()="Профиль"]') #кнопка в профиле, появляется только после авторизации
    logo = (By.XPATH, './/a[@class = "active"]') #элемент логотипа
    button_constructor = (By.XPATH, '//p[text()="Конструктор"') #кнопка "Конструктор"

    #для выхода из аккаунта
    button_logout = (By.XPATH, './/button[text()="Выход"]')

    #кнопки ингредиентов
    button_bans = (By.XPATH, './/span[text()="Булки"]')
    button_sauces = (By.XPATH, './/span[text()="Соусы"]')
    button_fillings = (By.XPATH, './/span[text()="Начинки"]')

    #заголовки разделов
    h_bans = (By.XPATH, ".//div[text()='Булки' and contains (@class = 'current')]")
    h_sauces = (By.XPATH, ".//div[text()='Соусы' and contains (@class = 'current')]")
    h_fillings = (By.XPATH, ".//div[text()='Начинки' and  contains (@class = 'current')]")

    #активный раздел
    h_active = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]')

