from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class DHCPDetailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)  # 可用 super().__init__ 產生 self.wait，或這樣處理

    def wait_for_loaded(self, service_name=None):
        """等待 detail 頁主標題 (H1) 出現。可選擇驗證 service_name。"""
        self.log("等待 DHCP Detail 頁面載入")
        if service_name:
            xpath = f'//h1[contains(text(), "{service_name}")]'
        else:
            xpath = '//h1[contains(@class, "ant-typography")]'
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        self.screenshot("dhcp_detail_page_loaded")

    def go_to_tab(self, tab_name):
        """切換到指定分頁，例如 'Overview' 或 'DHCP Pool'"""
        self.log(f"切換到 {tab_name} 分頁")
        tab_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f'//div[@role="tab" and contains(@class,"ant-tabs-tab-btn") and text()="{tab_name}"]')
            )
        )
        tab_btn.click()
        self.screenshot(f"switch_tab_{tab_name}")

    def get_pool_row_by_name(self, pool_name):
        """從 DHCP Pool 分頁的表格尋找 Pool Name 為指定值的 row"""
        self.log(f"查找 Pool Name: {pool_name} 的 row")
        xpath = (
            f'//table//tr[td[contains(@class,"ant-table-cell") and normalize-space()="{pool_name}"]]'
        )
        return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def get_number_of_hosts_by_pool_name(self, pool_name):
        """取指定 pool 的 Number of hosts 欄位值"""
        row = self.get_pool_row_by_name(pool_name)
        # 根據 column index (最後一欄 Number of hosts，根據你的 html 是第7個td)
        hosts_cell = row.find_elements(By.TAG_NAME, "td")[6]
        value = hosts_cell.text
        self.log(f"Pool: {pool_name} Number of hosts: {value}")
        return value
