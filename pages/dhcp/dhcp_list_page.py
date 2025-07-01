from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class DHCPListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def wait_for_loaded(self):
        self.log("等待 DHCP List 頁面載入...")
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//h1[contains(@class, "ant-typography") and contains(text(), "DHCP")]')
            )
        )
        self.log("DHCP List 頁面已載入完成")
        self.screenshot("dhcp_list_loaded")

    def click_dhcp_name(self, name):
        """
        點擊表格中指定名稱（例如 AutoTest-DHCP）的 DHCP Name，進入 detail 頁面
        """
        self.log(f'尋找 DHCP 名稱 "{name}" ...')
        # 依照你畫面，Name 欄位是個 link，通常是 <a>
        xpath = f'//a[text()="{name}"]'
        name_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        self.screenshot(f'before_click_{name}_in_list')
        name_link.click()
        self.log(f'已點擊 DHCP 名稱 "{name}" 進入 Detail')
