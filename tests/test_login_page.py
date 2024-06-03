import pytest
from pages.login_page import LoginPage

link = "https://race-marketplace.by/login/"


@pytest.mark.critical_test
def test_guest_can_authenticate_tc_id1(browser):
    """User can authenticate and log out from the system."""
    page = LoginPage(browser, link)
    page.open()
    page.fill_login_form_with_valid_data()
    page.click_submit_login_form_btn()
    page.click_user_dropdown_btn()
    page.click_logout_btn()


@pytest.mark.critical_test
def test_guest_cant_authenticate_with_invalid_username_tc_id2(browser):
    """Try to send contact form using invalid username and valid password."""
    page = LoginPage(browser, link)
    page.open()
    page.fill_login_form_with_invalid_username()
    page.click_submit_login_form_btn()
    page.check_error_message()


@pytest.mark.critical_test
def test_guest_cant_authenticate_with_invalid_password_tc_id3(browser):
    """Try to send contact form using valid username and invalid password."""
    page = LoginPage(browser, link)
    page.open()
    page.fill_login_form_with_invalid_password()
    page.click_submit_login_form_btn()
    page.check_error_message()


def test_guest_cant_authenticate_with_invalid_password_tc_id3(browser):
    """Try to send contact form using valid username and invalid password."""
    page = LoginPage(browser, link)
    page.open()
    page.fill_login_form_with_invalid_password()
    page.click_submit_login_form_btn()
    page.check_error_message()


def test_guest_cant_authenticate_without_password_tc_id4(browser):
    """Try to send contact form without password."""
    page = LoginPage(browser, link)
    page.open()
    page.fill_login_form_without_password()
    page.click_submit_login_form_btn()


def test_guest_cant_authenticate_without_username_tc_id5(browser):
    """Try to send contact form without username."""
    page = LoginPage(browser, link)
    page.open()
    page.fill_login_form_without_username()
    page.click_submit_login_form_btn()
