import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.sidebar import Sidebar
from pages.service_catalog_page import ServiceCatalogPage
from pages.dhcp.add_dhcp_for_wifi_page import AddDhcpForWiFiPage
from pages.dhcp.add_dhcp_pool_drawer import AddDhcpPoolDrawer
from pages.dhcp.dhcp_detail_page import DHCPDetailPage

def create_dhcp_profile_and_pool(driver, service_name="AutoTest-DHCP", pool_name="TestPool",
    start_ip="192.168.100.1", end_ip="192.168.100.10"):
    # 1. 登入
    login_page = LoginPage(driver, "dev")
    login_page.login("dog1306@email.com", "password-1")

    # 2. Sidebar > Service Catalog
    sidebar = Sidebar(driver)
    sidebar.go_to_service_catalog()
    service_catalog = ServiceCatalogPage(driver)
    service_catalog.wait_for_loaded()

    # 3. 新增 profile
    service_catalog.click_add_button_on_card("DHCP for Wi-Fi")
    service_catalog.assert_add_page_loaded("DHCP for Wi-Fi")

    add_page = AddDhcpForWiFiPage(driver)
    add_page.wait_for_loaded()
    add_page.set_service_name(service_name)
    add_page.select_dhcp_mode("Multiple AP DHCP")
    add_page.click_add_dhcp_pool()

    # 4. Drawer 操作
    drawer = AddDhcpPoolDrawer(driver)
    drawer.wait_for_loaded()
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
    # 不要驗證 warning，直接新增
    drawer.click_add()  

    # 回到 Add DHCP for Wi-Fi 頁面，點擊最下方 Add 按鈕
    add_page.click_add()

    # 斷言是否成功可省略
    # 返回 detail page 物件，給 test case 用
    detail_page = DHCPDetailPage(driver)
    detail_page.wait_for_loaded()
    return detail_page, pool_name

def test_warning_message_for_small_pool(driver):
    # 新增時不要 click add，直接驗證警告
    login_page = LoginPage(driver, "dev")
    login_page.login("dog1306@email.com", "password-1")
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
    drawer.fill_pool_name("TestPool")
    drawer.fill_start_ip("192.168.100.1")
    drawer.fill_end_ip("192.168.100.10")  # 小於等於 10
    drawer.assert_end_host_address_warning()  # 驗證 wording

def test_number_of_hosts(driver):
    detail_page, pool_name = create_dhcp_profile_and_pool(
        driver,
        service_name="AutoTest-DHCP-Hosts",
        pool_name="TestPool-Hosts",
        start_ip="192.168.100.1",
        end_ip="192.168.100.90"  # 90 hosts
    )

    # 切到 DHCP Pool 分頁（假設 detail_page 已在這個 tab，否則先切換）
    detail_page.go_to_tab("DHCP Pool")

    # 根據 pool_name 抓出 Number of hosts 欄位的數值
    actual_hosts = detail_page.get_number_of_hosts_by_pool_name(pool_name)
    assert actual_hosts == "90", f"Number of hosts 顯示錯誤，實際顯示：{actual_hosts}"
