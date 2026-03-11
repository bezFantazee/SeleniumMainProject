from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        # комплексная проверка страницы логина
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        # регистрация нового пользователя с заполнением всех полей
        self.should_be_login_url()
        self.should_be_login_form()
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_INPUT), \
            "Форма для имейла не найдена"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_INPUT), \
            "Форма для заполнения пароля не найдена"
        assert self.is_element_present(*LoginPageLocators.REGISTER_REPEAT_PASSWORD_INPUT), \
            "Форма для повтора пароля не найдена"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BTN), \
            "Кнопка подтверждения регистрации не найдена"

        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        password_input.send_keys(password)

        password_repeat_input = self.browser.find_element(*LoginPageLocators.REGISTER_REPEAT_PASSWORD_INPUT)
        password_repeat_input.send_keys(password)

        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()


    def should_be_login_url(self):
        # проверка на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, \
            f"Подстрока 'login' не найдена в URL. Текущий URL: {current_url}"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Форма авторизации отсутствует"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Форма регистрации отсутствует"

