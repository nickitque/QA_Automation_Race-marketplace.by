import pytest
from pages.login_page import LoginPage


link = "http://127.0.0.1:8000/login/"


@pytest.mark.critical_test
def test_guest_can_authenticate_tc_id1(browser):
    """User can authenticate and log out from the system."""
    page = LoginPage(browser, link)
    page.open()
    page.fill_username_field_with_valid_data()
    page.click_user_dropdown_btn()
    page.click_logout_btn()
