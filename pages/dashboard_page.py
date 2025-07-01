from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_dhcp(self):
        wait = WebDriverWait(self.driver, 10)
        # 點擊 Network Control
        network_control_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//span[contains(@class,"ant-menu-title-content")][contains(text(),"Network Control")]')
            )
        )
        network_control_btn.click()
        # 點擊 DHCP 子選單
        dhcp_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[contains(@href, "/dhcp")]')
            )
        )
        dhcp_btn.click()
