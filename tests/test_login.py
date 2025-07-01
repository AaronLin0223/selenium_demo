import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.log import logger

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_success(driver):
    env = "dev"
    username = "dog1306@email.com"
    password = "password-1"
    login_page = LoginPage(driver, env)

    try:
        logger.info("=== Start login test ===")
        login_page.login(username, password)
        dashboard = driver.find_element("css selector", 'a[data-label="Dashboard"].active')
        assert dashboard is not None
        logger.info("=== Login Test Passed ===")
    except Exception as e:
        logger.error(f"Exception caught: {e}")
        login_page.screenshot("test_fail")
        raise
