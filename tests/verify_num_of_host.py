from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://dev.ruckus.cloud/")  # 你應該已經登入、切換到 DHCP 頁面

wait = WebDriverWait(driver, 10)

# 等 table 載入（假設一定會有 pool-multiple 這個名字的欄位）
number_of_hosts_elem = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, '//td[text()="pool-multiple"]/following-sibling::td[4]')
    )
)
# 這裡的 4 是因為 pool-multiple 之後第4個 <td> 就是 Number of hosts

number_of_hosts_value = number_of_hosts_elem.text.strip()
print(f'Number of hosts: {number_of_hosts_value}')

# 假設你要比對正確性（例如要驗證是 90）
expected_value = "90"
assert number_of_hosts_value == expected_value, f"值不符，預期: {expected_value}, 實際: {number_of_hosts_value}"

print("Number of hosts 值正確！")
driver.quit()
