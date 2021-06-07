import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def change_browser():
    return webdriver.Chrome(ChromeDriverManager().install())

@pytest.fixture(scope='session')
def browser():
    browser = change_browser()
    yield browser
    browser.quit()

