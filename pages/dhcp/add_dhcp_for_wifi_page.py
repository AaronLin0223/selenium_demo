from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class AddDhcpForWiFiPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def wait_for_loaded(self):
        self.log("等待 Add DHCP for Wi-Fi 頁面載入")
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//h1[contains(@class,"ant-typography") and contains(text(),"Add DHCP for Wi-Fi")]')
            )
        )
        self.screenshot("add_dhcp_for_wifi_loaded")

    def set_service_name(self, name):
        self.log(f"輸入 Service Name: {name}")
        field = self.wait.until(EC.presence_of_element_located((By.ID, "settings_serviceName")))
        field.clear()
        field.send_keys(name)
        self.screenshot("set_service_name")

    def select_dhcp_mode(self, mode="Simple DHCP"):
        self.log(f"選擇 DHCP Mode: {mode}")
        radio = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                f'//label[contains(@class,"ant-radio-wrapper")]/span[2][contains(.,"{mode}")]'
            ))
        )
        radio.click()
        self.screenshot("select_dhcp_mode")

    def click_add_dhcp_pool(self):
        self.log("點擊 Add DHCP Pool")
        # 等 loading 結束
        self.wait.until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-spin"))
        )
        add_pool_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Add DHCP Pool"]]'))
        )
        # 強制滾到可見
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_pool_btn)
        time.sleep(0.2)
        add_pool_btn.click()
        self.screenshot("click_add_dhcp_pool")

    def click_add(self):
        self.log("點擊頁面下方 Add 確認按鈕")
        add_btn = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                '//div[contains(@class, "action-footer")]//button[contains(@class, "ant-btn-primary")]//span[text()="Add"]/..'
            ))
        )
        add_btn.click()
        self.screenshot("click_add_confirm")

    def assert_add_success(self):
        self.log("驗證是否已新增成功，請根據實際情境判斷")
        # 例如驗證 toast、回到列表頁等等
        pass  # 依需求補上斷言內容
