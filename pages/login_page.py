from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def fill_username_field_with_valid_data(self):
        self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys("Race-Marketplace")
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("Hahahalol.")
        self.click_button(*LoginPageLocators.SUBMIT_BTN)
