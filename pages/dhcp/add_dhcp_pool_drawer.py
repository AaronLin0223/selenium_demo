from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class AddDhcpPoolDrawer(BasePage):  # 假設你有 BasePage，含 log/screenshot
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def wait_for_loaded(self):
        self.log("等待 Add DHCP Pool drawer 載入")
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"ant-drawer-title")]//*[text()="Add DHCP Pool"]'))
        )
        self.screenshot("add_dhcp_pool_drawer_loaded")

    def fill_pool_name(self, pool_name):
        self.log(f"輸入 Pool Name: {pool_name}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "name")))
        el.clear()
        el.send_keys(pool_name)
        self.screenshot("fill_pool_name")

    def fill_description(self, desc):
        self.log(f"輸入 Description: {desc}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "description")))
        el.clear()
        el.send_keys(desc)
        self.screenshot("fill_description")

    def toggle_allow_ap_wired_clients(self, turn_on=True):
        self.log("切換 Allow AP wired clients")
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "allowWired")))
        checked = btn.get_attribute("aria-checked") == "true"
        if turn_on != checked:
            btn.click()
            self.screenshot("toggle_allow_ap_wired_clients")

    def fill_subnet_address(self, value):
        self.log(f"輸入 Subnet Address: {value}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "subnetAddress")))
        el.clear()
        el.send_keys(value)
        self.screenshot("fill_subnet_address")

    def fill_subnet_mask(self, value):
        self.log(f"輸入 Subnet Mask: {value}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "subnetMask")))
        el.clear()
        el.send_keys(value)
        self.screenshot("fill_subnet_mask")

    def fill_start_ip(self, value):
        self.log(f"輸入 Start Host Address: {value}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "startIpAddress")))
        el.clear()
        el.send_keys(value)
        self.screenshot("fill_start_ip")

    def fill_end_ip(self, value):
        self.log(f"輸入 End Host Address: {value}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "endIpAddress")))
        el.clear()
        el.send_keys(value)
        self.screenshot("fill_end_ip")

    def fill_primary_dns(self, value):
        self.log(f"輸入 Primary DNS IP: {value}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "primaryDnsIp")))
        el.clear()
        el.send_keys(value)
        self.screenshot("fill_primary_dns")

    def fill_secondary_dns(self, value):
        self.log(f"輸入 Secondary DNS IP: {value}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "secondaryDnsIp")))
        el.clear()
        el.send_keys(value)
        self.screenshot("fill_secondary_dns")

    def fill_lease_time(self, lease_time=24, lease_unit="Hours"):
        self.log(f"設定 Lease Time: {lease_time} {lease_unit}")
        lease_input = self.wait.until(EC.presence_of_element_located((By.ID, "leaseTime")))
        lease_input.click()
        lease_input.send_keys(Keys.CONTROL, 'a')
        lease_input.send_keys(Keys.BACKSPACE)
        lease_input.clear()
        lease_input.send_keys(str(lease_time))
        # Lease unit 是個下拉選單，可考慮進階點選，但若預設 "Hours" 則可略過
        self.screenshot("fill_lease_time")

    def fill_vlan(self, vlan_id):
        self.log(f"設定 VLAN: {vlan_id}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "vlanId")))
        el.click()
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(Keys.BACKSPACE)
        el.clear()
        el.send_keys(str(vlan_id))
        self.screenshot("fill_vlan")

    def click_add(self):
        self.log("點擊 Drawer 底部 Add 按鈕")
        btn = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                '//div[contains(@class, "ant-drawer-footer")]//button[contains(@class, "ant-btn-primary")]//span[text()="Add"]/..'
            ))
        )
        # 防止被遮蔽
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        self.screenshot("before_click_drawer_add")
        btn.click()
        self.screenshot("after_click_drawer_add")
        # 等 Drawer 消失
        self.wait.until_not(
            EC.presence_of_element_located((By.CLASS_NAME, "ant-drawer-content-wrapper"))
        )
        self.log("Drawer 已經關閉，已回到 Add DHCP for Wi-Fi 畫面")

    def get_end_host_address_warning(self):
        self.log("準備等待 End Host Address 警告訊息出現…")
        warning_elem = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'ant-form-item-explain-error') and contains(text(), 'additional 10 IPs')]")
            )
        )
        warning_text = warning_elem.text
        self.log(f"取得 End Host Address 警告訊息：{warning_text}")
        return warning_elem.text
    
    def assert_end_host_address_warning(self):
        expected_wording = (
            "An additional 10 IPs on top of the number of clients desired are needed for the DHCP servers and gateways used in multiple mode"
        )
        self.log(f"預期警告訊息: {expected_wording}")
        actual_wording = self.get_end_host_address_warning()
        self.log(f"實際警告訊息: {actual_wording}")
        assert actual_wording == expected_wording, f"警告訊息不正確: {actual_wording}"
        self.log("End Host Address 警告訊息斷言通過 ✅")