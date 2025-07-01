from selenium import webdriver
from login_page import LoginPage
from sidebar import Sidebar
#from dashboard_page import DashboardPage
#from dhcp_page import DhcpPage

driver = webdriver.Chrome()
driver.maximize_window()
username = "dog1306@email.com"  # 替換為實際的使用者名稱
password = "password-1"  # 替換為實際的密碼
env = "dev"  # 這裡可以根據需要修改為 dev、staging 等環境
#driver.get(f"https://{env}.ruckus.cloud/")  # 開啟 R1 UI 登入頁面

# 步驟1: 登入
login_page = LoginPage(driver, env)
login_page.login(username, password)
sidebar = Sidebar(driver)
sidebar.go_to_service_catalog()

"""請將 "your_user" 和 "your_password" 替換為實際的使用者名稱和密碼。
如果你有環境變數或其他方式存儲這些資訊，可以在這裡讀取。
# 步驟2: 進到 Dashboard，再點到 DHCP
dashboard_page = DashboardPage(driver)
dashboard_page.go_to_dhcp()

# 步驟3: 在 DHCP 頁驗證資料
dhcp_page = DhcpPage(driver)
dhcp_page.verify_number_of_hosts("pool-multiple", "90")
"""
print("所有步驟都順利完成！")
driver.quit()
