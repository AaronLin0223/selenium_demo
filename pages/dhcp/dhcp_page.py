from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DhcpPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_number_of_hosts(self, pool_name, expected_value):
        wait = WebDriverWait(self.driver, 10)
        # XPath 根據 pool 名稱找到該 row，再抓 Number of Hosts
        td_elem = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f'//td[text()="{pool_name}"]/following-sibling::td[4]')
            )
        )
        actual_value = td_elem.text.strip()
        assert actual_value == expected_value, f"Number of hosts mismatch: got {actual_value}, expect {expected_value}"
