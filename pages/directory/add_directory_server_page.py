from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class AddDirectoryServerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def wait_for_loaded(self):
        """等待 Add Directory Server 頁面載入"""
        self.log("等待 Add Directory Server 頁面載入")
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//form[@step="0"]'))
        )
        self.screenshot("add_directory_server_page_loaded")

    def fill_name(self, name):
        """填寫 Directory Server 名稱"""
        self.log(f"輸入 Directory Server 名稱: {name}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "name")))
        el.clear()
        el.send_keys(name)
        self.screenshot("fill_directory_server_name")

    def select_type(self, server_type):
        """選擇 Directory Server 類型 (LDAP 或 RADIUS)"""
        self.log(f"選擇 Directory Server 類型: {server_type}")
        if server_type.lower() == "ldap":
            radio = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="ldap"]'))
            )
        elif server_type.lower() == "radius":
            radio = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="radius"]'))
            )
        else:
            raise ValueError(f"不支援的 Directory Server 類型: {server_type}")
        
        radio.click()
        self.screenshot(f"select_type_{server_type.lower()}")

    def toggle_tls_enabled(self, enable=True):
        """切換 TLS 啟用狀態"""
        self.log(f"切換 TLS 啟用狀態: {enable}")
        tls_switch = self.wait.until(EC.element_to_be_clickable((By.ID, "tlsEnabled")))
        current_state = tls_switch.get_attribute("aria-checked") == "true"
        
        if enable != current_state:
            tls_switch.click()
            self.screenshot(f"toggle_tls_{'enabled' if enable else 'disabled'}")

    def fill_host(self, host):
        """填寫主機地址"""
        self.log(f"輸入主機地址: {host}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "host")))
        el.clear()
        el.send_keys(host)
        self.screenshot("fill_host")

    def fill_port(self, port):
        """填寫端口號"""
        self.log(f"輸入端口號: {port}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "port")))
        el.clear()
        el.send_keys(str(port))
        self.screenshot("fill_port")

    def fill_domain_name(self, domain_name):
        """填寫域名"""
        self.log(f"輸入域名: {domain_name}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "domainName")))
        el.clear()
        el.send_keys(domain_name)
        self.screenshot("fill_domain_name")

    def fill_admin_domain_name(self, admin_domain):
        """填寫管理員域名"""
        self.log(f"輸入管理員域名: {admin_domain}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "adminDomainName")))
        el.clear()
        el.send_keys(admin_domain)
        self.screenshot("fill_admin_domain_name")

    def fill_admin_password(self, password):
        """填寫管理員密碼"""
        self.log("輸入管理員密碼")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "adminPassword")))
        el.clear()
        el.send_keys(password)
        self.screenshot("fill_admin_password")

    def fill_identity_name(self, identity_name):
        """填寫身份名稱"""
        self.log(f"輸入身份名稱: {identity_name}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "identityName")))
        el.clear()
        el.send_keys(identity_name)
        self.screenshot("fill_identity_name")

    def fill_identity_email(self, email):
        """填寫身份郵箱"""
        self.log(f"輸入身份郵箱: {email}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "identityEmail")))
        el.clear()
        el.send_keys(email)
        self.screenshot("fill_identity_email")

    def fill_identity_phone(self, phone):
        """填寫身份電話"""
        self.log(f"輸入身份電話: {phone}")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "identityPhone")))
        el.clear()
        el.send_keys(phone)
        self.screenshot("fill_identity_phone")

    def add_attribute_mapping(self, attribute_name, mapped_name):
        """新增屬性映射"""
        self.log(f"新增屬性映射: {attribute_name} -> {mapped_name}")
        
        # 點擊新增按鈕 (假設有新增按鈕)
        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Add") or contains(@class, "add")]'))
        )
        add_btn.click()
        
        # 填寫屬性名稱
        name_input = self.wait.until(EC.presence_of_element_located((By.ID, "attributeMappings_0_name")))
        name_input.clear()
        name_input.send_keys(attribute_name)
        
        # 填寫映射名稱
        mapped_input = self.wait.until(EC.presence_of_element_located((By.ID, "attributeMappings_0_mappedByName")))
        mapped_input.clear()
        mapped_input.send_keys(mapped_name)
        
        self.screenshot("add_attribute_mapping")

    def click_add(self):
        """點擊新增按鈕"""
        self.log("點擊新增 Directory Server 按鈕")
        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "ant-btn-primary") and contains(text(), "Add")]'))
        )
        self.screenshot("before_click_add_directory_server")
        add_btn.click()
        self.screenshot("after_click_add_directory_server")

    def click_cancel(self):
        """點擊取消按鈕"""
        self.log("點擊取消按鈕")
        cancel_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Cancel")]'))
        )
        cancel_btn.click()
        self.screenshot("click_cancel")

    def get_validation_error(self, field_id):
        """獲取指定欄位的驗證錯誤訊息"""
        self.log(f"獲取欄位 {field_id} 的驗證錯誤訊息")
        error_elem = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, f'//div[@id="{field_id}"]/following-sibling::div[contains(@class, "ant-form-item-explain-error")]'))
        )
        error_text = error_elem.text
        self.log(f"驗證錯誤訊息: {error_text}")
        return error_text

    def assert_validation_error(self, field_id, expected_error):
        """斷言指定欄位的驗證錯誤訊息"""
        actual_error = self.get_validation_error(field_id)
        assert actual_error == expected_error, f"驗證錯誤訊息不正確: 預期 '{expected_error}', 實際 '{actual_error}'"
        self.log(f"欄位 {field_id} 驗證錯誤斷言通過 ✅")

    def is_form_valid(self):
        """檢查表單是否有效 (沒有驗證錯誤)"""
        try:
            error_elements = self.driver.find_elements(By.CLASS_NAME, "ant-form-item-explain-error")
            return len(error_elements) == 0
        except:
            return True

    def fill_ldap_configuration(self, name, host, port=636, domain_name="", admin_domain="", admin_password="", tls_enabled=True):
        """快速填寫 LDAP 配置"""
        self.log("開始填寫 LDAP 配置")
        self.fill_name(name)
        self.select_type("LDAP")
        self.toggle_tls_enabled(tls_enabled)
        self.fill_host(host)
        self.fill_port(port)
        if domain_name:
            self.fill_domain_name(domain_name)
        if admin_domain:
            self.fill_admin_domain_name(admin_domain)
        if admin_password:
            self.fill_admin_password(admin_password)
        self.screenshot("ldap_configuration_filled")

    def fill_radius_configuration(self, name, host, port=1812, admin_domain="", admin_password=""):
        """快速填寫 RADIUS 配置"""
        self.log("開始填寫 RADIUS 配置")
        self.fill_name(name)
        self.select_type("RADIUS")
        self.fill_host(host)
        self.fill_port(port)
        if admin_domain:
            self.fill_admin_domain_name(admin_domain)
        if admin_password:
            self.fill_admin_password(admin_password)
        self.screenshot("radius_configuration_filled")
