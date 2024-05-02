import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser_chrome = webdriver.Chrome()
    yield browser_chrome
    print("\nquit browser..")
    browser_chrome.quit()