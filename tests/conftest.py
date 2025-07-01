import pytest
from selenium import webdriver
from utils.log import logger


@pytest.fixture(scope="function")
def driver():
    # 你可以根據需求自訂 driver 參數，例如 headless 模式
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # 如果要無頭模式
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_setup(item):
    print(f"\n========= [RUN] {item.name} =========")
    logger.info(f"========= [RUN] {item.name} =========")
    yield

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_teardown(item, nextitem):
    print(f"========= [END] {item.name} =========")
    logger.info(f"========= [END] {item.name} =========")
    yield