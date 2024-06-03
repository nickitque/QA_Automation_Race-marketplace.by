from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def check_error_message(self):
        assert self.result_text(*LoginPageLocators.ERROR_MSG_TEXT) == "Пожалуйста, введите правильные имя " \
                                                                      "пользователя и пароль. Оба поля могут быть " \
                                                                      "чувствительны к регистру.", \
            "The error msg is different"

    def click_submit_login_form_btn(self):
        self.click_button(*LoginPageLocators.SUBMIT_BTN)

    def fill_login_form_with_valid_data(self):
        self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys("Race-Marketplace")
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("Hahahalol.")

    def fill_login_form_with_invalid_username(self):
        self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys("Race-Marketplac")
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("Hahahalol.")

    def fill_login_form_with_invalid_password(self):
        self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys("Race-Marketplace")
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("Hahahalol")

    def fill_login_form_without_password(self):
        self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys("Race-Marketplace")

    def fill_login_form_without_username(self):
        self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys("Race-Marketplace")
