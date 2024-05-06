import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart chrome for test..")
    browser_chrome = webdriver.Chrome()
    yield browser_chrome
    print("\nquit chrome..")
    browser_chrome.quit()


@pytest.fixture(scope="session")
def browser_for_session():
    print("\nstart chrome for test..")
    browser_chrome = webdriver.Chrome()
    yield browser_chrome
    print("\nquit chrome..")
    browser_chrome.quit()
