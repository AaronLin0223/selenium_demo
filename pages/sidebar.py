from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Sidebar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def go_to_service_catalog(self):
        self.log("1️⃣ 先找到 Network Control 主選單...")
        network_control = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//span[contains(@class,"ant-menu-title-content")][contains(text(),"Network Control")]')
            )
        )

        self.log("2️⃣ 滑鼠 hover 到 Network Control...")
        ActionChains(self.driver).move_to_element(network_control).perform()

        self.log("3️⃣ 等待 Service Catalog 子選單出現...")
        service_catalog = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, '//a[contains(text(),"Service Catalog")]')
            )
        )

        self.log("4️⃣ 點擊 Service Catalog 選單...")
        service_catalog.click()

        self.log("5️⃣ 等待頁面 loading 結束 (ant-spin)...")
        self.wait.until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ant-spin'))
        )

        self.log("6️⃣ 等待 Service Catalog 頁面主標題出現...")
        service_catalog_header = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//h1[contains(@class, "ant-typography") and contains(text(), "Service Catalog")]')
            )
        )
        self.log("✅ Service Catalog 頁面主標題已出現，頁面應該已載入完成。")

        self.screenshot("service_catalog_page_loaded")


    def go_to_my_services(self):
        self.log("1️⃣ 先找到 Network Control 主選單...")
        network_control = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//span[contains(@class,"ant-menu-title-content")][contains(text(),"Network Control")]')
            )
        )
        self.log("2️⃣ 滑鼠 hover 到 Network Control...")
        ActionChains(self.driver).move_to_element(network_control).perform()

        self.log("3️⃣ 等待 My Services 子選單出現...")
        my_services = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, '//a[contains(text(),"My Services")]')
            )
        )

        self.log("4️⃣ 點擊 My Services 選單...")
        my_services.click()

        self.log("5️⃣ 等待頁面 loading 結束 (ant-spin)...")
        self.wait.until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ant-spin'))
        )

        self.log("6️⃣ 等待 My Services 頁面主標題出現...")
        my_services_header = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//h1[contains(@class, "ant-typography") and contains(text(), "My Services")]')
            )
        )
        self.log("✅ My Services 頁面主標題已出現，頁面應該已載入完成。")
        self.screenshot("my_services_page_loaded")

    def go_to_wifi_networks_list(self):
        """導航到 Wi-Fi Networks List 頁面"""
        self.log("1️⃣ 先找到 Wi-Fi 主選單...")
        wifi_menu = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//span[contains(@class,"ant-menu-title-content")][contains(text(),"Wi-Fi")]')
            )
        )

        self.log("2️⃣ 滑鼠 hover 到 Wi-Fi...")
        ActionChains(self.driver).move_to_element(wifi_menu).perform()

        self.log("3️⃣ 等待 Wi-Fi Networks List 子選單出現...")
        wifi_networks_list = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, '//a[@data-label="Wi-Fi Networks List"]')
            )
        )

        self.log("4️⃣ 點擊 Wi-Fi Networks List 選單...")
        wifi_networks_list.click()

        self.log("5️⃣ 等待頁面 loading 結束 (ant-spin)...")
        self.wait.until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ant-spin'))
        )

        self.log("6️⃣ 等待 Wi-Fi Networks List 頁面主標題出現...")
        wifi_networks_header = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//h1[contains(@class, "ant-typography") and contains(text(), "Wi-Fi Networks")]')
            )
        )
        self.log("✅ Wi-Fi Networks List 頁面主標題已出現，頁面應該已載入完成。")
        self.screenshot("wifi_networks_list_page_loaded")

    # ==================== Dashboard ====================
    def go_to_dashboard(self):
        """導航到 Dashboard 頁面"""
        self.log("點擊 Dashboard 選單...")
        dashboard = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Dashboard"]'))
        )
        dashboard.click()
        
        self.log("等待頁面 loading 結束...")
        self.wait.until_not(EC.presence_of_element_located((By.CSS_SELECTOR, '.ant-spin')))
        
        self.log("等待 Dashboard 頁面載入...")
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Dashboard")]'))
        )
        self.screenshot("dashboard_page_loaded")

    # ==================== AI Assurance ====================
    def go_to_ai_analytics_incidents(self):
        """導航到 AI Analytics > Incidents 頁面"""
        self.log("1️⃣ 找到 AI Assurance 主選單...")
        ai_assurance = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"AI Assurance")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 AI Assurance...")
        ActionChains(self.driver).move_to_element(ai_assurance).perform()
        
        self.log("3️⃣ 點擊 Incidents...")
        incidents = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Incidents"]'))
        )
        incidents.click()
        
        self._wait_for_page_load("Incidents")
        self.screenshot("ai_analytics_incidents_page_loaded")

    def go_to_ai_analytics_intent_ai(self):
        """導航到 AI Analytics > IntentAI 頁面"""
        self.log("1️⃣ 找到 AI Assurance 主選單...")
        ai_assurance = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"AI Assurance")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 AI Assurance...")
        ActionChains(self.driver).move_to_element(ai_assurance).perform()
        
        self.log("3️⃣ 點擊 IntentAI...")
        intent_ai = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="IntentAI"]'))
        )
        intent_ai.click()
        
        self._wait_for_page_load("IntentAI")
        self.screenshot("ai_analytics_intent_ai_page_loaded")

    def go_to_network_assurance_health(self):
        """導航到 Network Assurance > Health 頁面"""
        self.log("1️⃣ 找到 AI Assurance 主選單...")
        ai_assurance = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"AI Assurance")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 AI Assurance...")
        ActionChains(self.driver).move_to_element(ai_assurance).perform()
        
        self.log("3️⃣ 點擊 Health...")
        health = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Health"]'))
        )
        health.click()
        
        self._wait_for_page_load("Health")
        self.screenshot("network_assurance_health_page_loaded")

    def go_to_network_assurance_service_validation(self):
        """導航到 Network Assurance > Service Validation 頁面"""
        self.log("1️⃣ 找到 AI Assurance 主選單...")
        ai_assurance = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"AI Assurance")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 AI Assurance...")
        ActionChains(self.driver).move_to_element(ai_assurance).perform()
        
        self.log("3️⃣ 點擊 Service Validation...")
        service_validation = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Service Validation"]'))
        )
        service_validation.click()
        
        self._wait_for_page_load("Service Validation")
        self.screenshot("network_assurance_service_validation_page_loaded")

    def go_to_network_assurance_config_change(self):
        """導航到 Network Assurance > Config Change 頁面"""
        self.log("1️⃣ 找到 AI Assurance 主選單...")
        ai_assurance = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"AI Assurance")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 AI Assurance...")
        ActionChains(self.driver).move_to_element(ai_assurance).perform()
        
        self.log("3️⃣ 點擊 Config Change...")
        config_change = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Config Change"]'))
        )
        config_change.click()
        
        self._wait_for_page_load("Config Change")
        self.screenshot("network_assurance_config_change_page_loaded")

    def go_to_network_assurance_video_call_qoe(self):
        """導航到 Network Assurance > Video Call QoE 頁面"""
        self.log("1️⃣ 找到 AI Assurance 主選單...")
        ai_assurance = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"AI Assurance")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 AI Assurance...")
        ActionChains(self.driver).move_to_element(ai_assurance).perform()
        
        self.log("3️⃣ 點擊 Video Call QoE...")
        video_call_qoe = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Video Call QoE"]'))
        )
        video_call_qoe.click()
        
        self._wait_for_page_load("Video Call QoE")
        self.screenshot("network_assurance_video_call_qoe_page_loaded")

    # ==================== Clients ====================
    def go_to_wireless_clients_list(self):
        """導航到 Clients > Wireless > Wireless Clients List 頁面"""
        self.log("1️⃣ 找到 Clients 主選單...")
        clients = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Clients")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Clients...")
        ActionChains(self.driver).move_to_element(clients).perform()
        
        self.log("3️⃣ 點擊 Wireless Clients List...")
        wireless_clients = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Wireless Clients List"]'))
        )
        wireless_clients.click()
        
        self._wait_for_page_load("Wireless Clients")
        self.screenshot("wireless_clients_list_page_loaded")

    def go_to_guest_pass_credentials(self):
        """導航到 Clients > Wireless > Guest Pass Credentials 頁面"""
        self.log("1️⃣ 找到 Clients 主選單...")
        clients = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Clients")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Clients...")
        ActionChains(self.driver).move_to_element(clients).perform()
        
        self.log("3️⃣ 點擊 Guest Pass Credentials...")
        guest_pass = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Guest Pass Credentials"]'))
        )
        guest_pass.click()
        
        self._wait_for_page_load("Guest Pass Credentials")
        self.screenshot("guest_pass_credentials_page_loaded")

    def go_to_wireless_clients_report(self):
        """導航到 Clients > Wireless > Wireless Clients Report 頁面"""
        self.log("1️⃣ 找到 Clients 主選單...")
        clients = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Clients")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Clients...")
        ActionChains(self.driver).move_to_element(clients).perform()
        
        self.log("3️⃣ 點擊 Wireless Clients Report...")
        wireless_report = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Wireless Clients Report"]'))
        )
        wireless_report.click()
        
        self._wait_for_page_load("Wireless Clients Report")
        self.screenshot("wireless_clients_report_page_loaded")

    def go_to_ap_clients_list(self):
        """導航到 Clients > Wired > AP Clients List 頁面"""
        self.log("1️⃣ 找到 Clients 主選單...")
        clients = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Clients")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Clients...")
        ActionChains(self.driver).move_to_element(clients).perform()
        
        self.log("3️⃣ 點擊 AP Clients List...")
        ap_clients = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="AP Clients List"]'))
        )
        ap_clients.click()
        
        self._wait_for_page_load("AP Clients")
        self.screenshot("ap_clients_list_page_loaded")

    def go_to_switch_clients_list(self):
        """導航到 Clients > Wired > Switch Clients List 頁面"""
        self.log("1️⃣ 找到 Clients 主選單...")
        clients = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Clients")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Clients...")
        ActionChains(self.driver).move_to_element(clients).perform()
        
        self.log("3️⃣ 點擊 Switch Clients List...")
        switch_clients = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Switch Clients List"]'))
        )
        switch_clients.click()
        
        self._wait_for_page_load("Switch Clients")
        self.screenshot("switch_clients_list_page_loaded")

    def go_to_identity_groups(self):
        """導航到 Clients > Identity Management > Identity Groups 頁面"""
        self.log("1️⃣ 找到 Clients 主選單...")
        clients = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Clients")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Clients...")
        ActionChains(self.driver).move_to_element(clients).perform()
        
        self.log("3️⃣ 點擊 Identity Groups...")
        identity_groups = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Identity Groups"]'))
        )
        identity_groups.click()
        
        self._wait_for_page_load("Identity Groups")
        self.screenshot("identity_groups_page_loaded")

    def go_to_identities_list(self):
        """導航到 Clients > Identity Management > Identities List 頁面"""
        self.log("1️⃣ 找到 Clients 主選單...")
        clients = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Clients")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Clients...")
        ActionChains(self.driver).move_to_element(clients).perform()
        
        self.log("3️⃣ 點擊 Identities List...")
        identities = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Identities List"]'))
        )
        identities.click()
        
        self._wait_for_page_load("Identities")
        self.screenshot("identities_list_page_loaded")

    # ==================== Venues ====================
    def go_to_venues(self):
        """導航到 Venues 頁面"""
        self.log("點擊 Venues 選單...")
        venues = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Venues"]'))
        )
        venues.click()
        
        self._wait_for_page_load("Venues")
        self.screenshot("venues_page_loaded")

    # ==================== Wi-Fi ====================
    def go_to_ap_list(self):
        """導航到 Wi-Fi > Access Points > AP List 頁面"""
        self.log("1️⃣ 找到 Wi-Fi 主選單...")
        wifi = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Wi-Fi")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Wi-Fi...")
        ActionChains(self.driver).move_to_element(wifi).perform()
        
        self.log("3️⃣ 點擊 AP List...")
        ap_list = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="AP List"]'))
        )
        ap_list.click()
        
        self._wait_for_page_load("AP List")
        self.screenshot("ap_list_page_loaded")

    def go_to_ap_group_list(self):
        """導航到 Wi-Fi > Access Points > AP Group List 頁面"""
        self.log("1️⃣ 找到 Wi-Fi 主選單...")
        wifi = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Wi-Fi")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Wi-Fi...")
        ActionChains(self.driver).move_to_element(wifi).perform()
        
        self.log("3️⃣ 點擊 AP Group List...")
        ap_group_list = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="AP Group List"]'))
        )
        ap_group_list.click()
        
        self._wait_for_page_load("AP Group List")
        self.screenshot("ap_group_list_page_loaded")

    def go_to_ap_report(self):
        """導航到 Wi-Fi > Access Points > AP Report 頁面"""
        self.log("1️⃣ 找到 Wi-Fi 主選單...")
        wifi = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Wi-Fi")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Wi-Fi...")
        ActionChains(self.driver).move_to_element(wifi).perform()
        
        self.log("3️⃣ 點擊 AP Report...")
        ap_report = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="AP Report"]'))
        )
        ap_report.click()
        
        self._wait_for_page_load("AP Report")
        self.screenshot("ap_report_page_loaded")

    def go_to_airtime_utilization_report(self):
        """導航到 Wi-Fi > Access Points > Airtime Utilization Report 頁面"""
        self.log("1️⃣ 找到 Wi-Fi 主選單...")
        wifi = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Wi-Fi")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Wi-Fi...")
        ActionChains(self.driver).move_to_element(wifi).perform()
        
        self.log("3️⃣ 點擊 Airtime Utilization Report...")
        airtime_report = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Airtime Utilization Report"]'))
        )
        airtime_report.click()
        
        self._wait_for_page_load("Airtime Utilization Report")
        self.screenshot("airtime_utilization_report_page_loaded")

    def go_to_wlans_report(self):
        """導航到 Wi-Fi > Wi-Fi Networks > WLANs Report 頁面"""
        self.log("1️⃣ 找到 Wi-Fi 主選單...")
        wifi = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Wi-Fi")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Wi-Fi...")
        ActionChains(self.driver).move_to_element(wifi).perform()
        
        self.log("3️⃣ 點擊 WLANs Report...")
        wlans_report = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="WLANs Report"]'))
        )
        wlans_report.click()
        
        self._wait_for_page_load("WLANs Report")
        self.screenshot("wlans_report_page_loaded")

    def go_to_applications_report(self):
        """導航到 Wi-Fi > Wi-Fi Networks > Applications Report 頁面"""
        self.log("1️⃣ 找到 Wi-Fi 主選單...")
        wifi = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Wi-Fi")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Wi-Fi...")
        ActionChains(self.driver).move_to_element(wifi).perform()
        
        self.log("3️⃣ 點擊 Applications Report...")
        applications_report = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Applications Report"]'))
        )
        applications_report.click()
        
        self._wait_for_page_load("Applications Report")
        self.screenshot("applications_report_page_loaded")

    def go_to_wireless_report(self):
        """導航到 Wi-Fi > Wi-Fi Networks > Wireless Report 頁面"""
        self.log("1️⃣ 找到 Wi-Fi 主選單...")
        wifi = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Wi-Fi")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Wi-Fi...")
        ActionChains(self.driver).move_to_element(wifi).perform()
        
        self.log("3️⃣ 點擊 Wireless Report...")
        wireless_report = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Wireless Report"]'))
        )
        wireless_report.click()
        
        self._wait_for_page_load("Wireless Report")
        self.screenshot("wireless_report_page_loaded")

    # ==================== Wired ====================
    def go_to_switch_list(self):
        """導航到 Wired > Switches > Switch List 頁面"""
        self.log("1️⃣ 找到 Wired 主選單...")
        wired = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Wired")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Wired...")
        ActionChains(self.driver).move_to_element(wired).perform()
        
        self.log("3️⃣ 點擊 Switch List...")
        switch_list = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Switch List"]'))
        )
        switch_list.click()
        
        self._wait_for_page_load("Switch List")
        self.screenshot("switch_list_page_loaded")

    def go_to_wired_report(self):
        """導航到 Wired > Switches > Wired Report 頁面"""
        self.log("1️⃣ 找到 Wired 主選單...")
        wired = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Wired")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Wired...")
        ActionChains(self.driver).move_to_element(wired).perform()
        
        self.log("3️⃣ 點擊 Wired Report...")
        wired_report = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Wired Report"]'))
        )
        wired_report.click()
        
        self._wait_for_page_load("Wired Report")
        self.screenshot("wired_report_page_loaded")

    def go_to_configuration_profiles(self):
        """導航到 Wired > Wired Network Profiles > Configuration Profiles 頁面"""
        self.log("1️⃣ 找到 Wired 主選單...")
        wired = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Wired")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Wired...")
        ActionChains(self.driver).move_to_element(wired).perform()
        
        self.log("3️⃣ 點擊 Configuration Profiles...")
        config_profiles = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Configuration Profiles"]'))
        )
        config_profiles.click()
        
        self._wait_for_page_load("Configuration Profiles")
        self.screenshot("configuration_profiles_page_loaded")

    def go_to_on_demand_cli_configuration(self):
        """導航到 Wired > Wired Network Profiles > On-Demand CLI Configuration 頁面"""
        self.log("1️⃣ 找到 Wired 主選單...")
        wired = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Wired")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Wired...")
        ActionChains(self.driver).move_to_element(wired).perform()
        
        self.log("3️⃣ 點擊 On-Demand CLI Configuration...")
        cli_config = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="On-Demand CLI Configuration"]'))
        )
        cli_config.click()
        
        self._wait_for_page_load("On-Demand CLI Configuration")
        self.screenshot("on_demand_cli_configuration_page_loaded")

    # ==================== Gateway ====================
    def go_to_ruckus_edge(self):
        """導航到 Gateway > RUCKUS Edge 頁面"""
        self.log("1️⃣ 找到 Gateway 主選單...")
        gateway = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Gateway")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Gateway...")
        ActionChains(self.driver).move_to_element(gateway).perform()
        
        self.log("3️⃣ 點擊 RUCKUS Edge...")
        ruckus_edge = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="RUCKUS Edge"]'))
        )
        ruckus_edge.click()
        
        self._wait_for_page_load("RUCKUS Edge")
        self.screenshot("ruckus_edge_page_loaded")

    def go_to_ruckus_wan_gateway(self):
        """導航到 Gateway > RUCKUS WAN Gateway 頁面"""
        self.log("1️⃣ 找到 Gateway 主選單...")
        gateway = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Gateway")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Gateway...")
        ActionChains(self.driver).move_to_element(gateway).perform()
        
        self.log("3️⃣ 點擊 RUCKUS WAN Gateway...")
        wan_gateway = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="RUCKUS WAN Gateway"]'))
        )
        wan_gateway.click()
        
        self._wait_for_page_load("RUCKUS WAN Gateway")
        self.screenshot("ruckus_wan_gateway_page_loaded")

    # ==================== Business Insights ====================
    def go_to_data_studio(self):
        """導航到 Business Insights > Data Studio 頁面"""
        self.log("1️⃣ 找到 Business Insights 主選單...")
        business_insights = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Business Insights")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Business Insights...")
        ActionChains(self.driver).move_to_element(business_insights).perform()
        
        self.log("3️⃣ 點擊 Data Studio...")
        data_studio = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Data Studio"]'))
        )
        data_studio.click()
        
        self._wait_for_page_load("Data Studio")
        self.screenshot("data_studio_page_loaded")

    def go_to_reports(self):
        """導航到 Business Insights > Reports 頁面"""
        self.log("1️⃣ 找到 Business Insights 主選單...")
        business_insights = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Business Insights")]'))
        )
        
        self.log("2️⃣ 滑鼠 hover 到 Business Insights...")
        ActionChains(self.driver).move_to_element(business_insights).perform()
        
        self.log("3️⃣ 點擊 Reports...")
        reports = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-label="Reports"]'))
        )
        reports.click()
        
        self._wait_for_page_load("Reports")
        self.screenshot("reports_page_loaded")

    # ==================== Helper Methods ====================
    def _wait_for_page_load(self, page_title):
        """通用的頁面載入等待方法"""
        self.log(f"5️⃣ 等待頁面 loading 結束 (ant-spin)...")
        self.wait.until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ant-spin'))
        )
        
        self.log(f"6️⃣ 等待 {page_title} 頁面主標題出現...")
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f'//h1[contains(@class, "ant-typography") and contains(text(), "{page_title}")]')
            )
        )
        self.log(f"✅ {page_title} 頁面主標題已出現，頁面應該已載入完成。")