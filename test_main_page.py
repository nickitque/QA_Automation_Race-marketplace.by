import time
from pages.main_page import MainPage
from pages.login_page import LoginPage




def test_guest_should_see_login_link(browser):
    link = "http://127.0.0.1:8000/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
def test_guest_can_go_to_login_page(browser):
    url = "http://127.0.0.1:8000/"
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()

