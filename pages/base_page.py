from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
import requests


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_displayed(self, how, what):
        return self.browser.find_element(how, what).is_displayed()

    def click_button(self, how, what):
        self.browser.find_element(how, what).click()

    def result_text(self, how, what):
        return self.browser.find_element(how, what).text

    def result_href(self, how, what):
        return self.browser.find_element(how, what).get_attribute("href")

    def assert_status_code_200(self):
        assert requests.head(self.url).status_code == 200, "The status code is not 200"

    def assert_page_title(self, title):
        assert self.browser.title == title, "The page title is different"

    def click_login_btn_header(self):
        self.click_button(*BasePageLocators.LOGIN_BTN_HEADER)
        assert self.browser.current_url == "https://race-marketplace.by/login/"

    def click_register_btn_header(self):
        self.click_button(*BasePageLocators.REGISTER_BTN_HEADER)
        assert self.browser.current_url == "https://race-marketplace.by/signup/"

    def click_user_dropdown_btn(self):
        self.click_button(*BasePageLocators.AUTH_USERNAME_DROPDOWN_HEADER)

    def click_logout_btn(self):
        self.click_button(*BasePageLocators.AUTH_LOGOUT_BTN_HEADER)

    def click_marketplace_btn_header(self):
        self.click_button(*BasePageLocators.MARKETPLACE_BTN_HEADER)
        assert self.browser.current_url == "https://race-marketplace.by/items/"

    def click_blog_btn_header(self):
        self.click_button(*BasePageLocators.BLOG_BTN_HEADER)
        assert self.browser.current_url == "https://race-marketplace.by/blog/"

    def click_blog_dropdown_btn_header(self):
        self.click_button(*BasePageLocators.BLOG_DROPDOWN_BTN_HEADER)

    def click_blog_drift_dropdown_btn_header(self):
        self.click_button(*BasePageLocators.BLOG_DROPDOWN_DRIFT_BTN_HEADER)
        assert self.browser.current_url == "https://race-marketplace.by/blog/category/drift/"

    def click_blog_drag_dropdown_btn_header(self):
        self.click_button(*BasePageLocators.BLOG_DROPDOWN_DRAG_BTN_HEADER)
        assert self.browser.current_url == "https://race-marketplace.by/blog/category/drag/"

    def click_blog_timeattack_dropdown_btn_header(self):
        self.click_button(*BasePageLocators.BLOG_DROPDOWN_TA_BTN_HEADER)
        assert self.browser.current_url == "https://race-marketplace.by/blog/category/Time-attack/"


    def click_calendar_btn_header(self):
        self.click_button(*BasePageLocators.CALENDAR_BTN_HEADER)
        assert self.browser.current_url == "https://race-marketplace.by/events/"