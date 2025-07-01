import pytest
from pages.sidebar import Sidebar
from pages.service_catalog_page import ServiceCatalogPage
from pages.dhcp.add_dhcp_for_wifi_page import AddDhcpForWiFiPage
from pages.dhcp.add_dhcp_pool_drawer import AddDhcpPoolDrawer
from pages.my_services_page import MyServicesPage
from pages.dhcp.dhcp_list_page import DHCPListPage
from pages.dhcp.dhcp_detail_page import DHCPDetailPage
from utils.log import logger
import ipaddress




# helper: 完成到 Add DHCP Pool Drawer 的共用前置
def prepare_add_dhcp_pool_drawer(driver):
    env = "dev"
    username = "dog1306@email.com"
    password = "password-1"
    from pages.login_page import LoginPage
    login_page = LoginPage(driver, env)
    login_page.login(username, password)

    sidebar = Sidebar(driver)
    sidebar.go_to_service_catalog()

    service_catalog = ServiceCatalogPage(driver)
    service_catalog.wait_for_loaded()
    service_catalog.click_add_button_on_card("DHCP for Wi-Fi")
    service_catalog.assert_add_page_loaded("DHCP for Wi-Fi")

    add_page = AddDhcpForWiFiPage(driver)
    add_page.wait_for_loaded()
    add_page.set_service_name("AutoTest-DHCP")
    add_page.select_dhcp_mode("Multiple AP DHCP")
    add_page.click_add_dhcp_pool()

    drawer = AddDhcpPoolDrawer(driver)
    drawer.wait_for_loaded()
    return add_page, drawer

def ip_pool_size(start_ip, end_ip):
    """計算 IP pool 的大小"""
    start = ipaddress.ip_address(start_ip)
    end = ipaddress.ip_address(end_ip)
    return int(end) - int(start) + 1

# 測試警告訊息 wording
def test_dhcp_end_ip_warning_message(driver):
    logger.info("========== [TEST] test_dhcp_end_ip_warning_message ==========")
    add_page, drawer = prepare_add_dhcp_pool_drawer(driver)
    drawer.fill_pool_name("TestPool")
    drawer.fill_description("自動測試")
    drawer.fill_subnet_address("192.168.100.0")
    drawer.fill_subnet_mask("255.255.255.0")
    drawer.fill_start_ip("192.168.100.1")
    drawer.fill_end_ip("192.168.100.10")
    drawer.fill_primary_dns("8.8.8.8")
    drawer.fill_secondary_dns("8.8.4.4")
    drawer.fill_lease_time(24)
    drawer.fill_vlan(300)
    # 驗證警告 wording
    drawer.assert_end_host_address_warning()

# 測試 Number of Hosts 值
def test_dhcp_number_of_hosts(driver, start_ip="192.168.100.1", end_ip="192.168.100.20"):  # 測試20個ip
    logger.info("========== [TEST] test_number_of_hosts ==========")
    add_page, drawer = prepare_add_dhcp_pool_drawer(driver)
    pool_name = "TestPool2"
    drawer.fill_pool_name(pool_name)
    drawer.fill_description("自動測試")
    drawer.fill_subnet_address("192.168.100.0")
    drawer.fill_subnet_mask("255.255.255.0")
    drawer.fill_start_ip(start_ip)
    drawer.fill_end_ip(end_ip) 
    drawer.fill_primary_dns("8.8.8.8")
    drawer.fill_secondary_dns("8.8.4.4")
    drawer.fill_lease_time(24)
    drawer.fill_vlan(300)
    # 新增 pool
    drawer.click_add()

    # 回到 Add DHCP for Wi-Fi 頁，下方再按 Add
    add_page.click_add()
    
    # 進到 my services page
    sidebar = Sidebar(driver)
    sidebar.go_to_my_services()
    
    # 點擊 DHCP for Wi-Fi 卡片
    my_services = MyServicesPage(driver)
    my_services.wait_for_loaded()
    my_services.click_service_card("DHCP for Wi-Fi")
    
    #進到DHCP list page
    dhcp_list = DHCPListPage(driver)
    dhcp_list.wait_for_loaded()
    # 點擊剛剛新增的 DHCP Profile
    dhcp_list.click_dhcp_name("AutoTest-DHCP")
    # 驗證是否進入 detail page

    # 進到 detail page
    detail = DHCPDetailPage(driver)
    detail.wait_for_loaded("AutoTest-DHCP")
    detail.go_to_tab("DHCP Pool")
    # 驗證 Number of hosts 欄位
    num_hosts = detail.get_number_of_hosts_by_pool_name(pool_name)
    expected_hosts = ip_pool_size(start_ip, end_ip) - 10 # 減去 10 個保留位址
    logger.info(f"Number of hosts: {num_hosts}, Expected: {expected_hosts}")
    assert num_hosts == str(expected_hosts), f"Number of hosts 錯誤，取得值: {num_hosts}, 預期值: {expected_hosts}"
#    assert num_hosts == "10", f"Number of hosts 錯誤，取得值: {num_hosts}"

