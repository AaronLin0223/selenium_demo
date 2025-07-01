from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class MyServicesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def wait_for_loaded(self):
        """等待 My Services 頁面完全載入"""
        self.log("等待 My Services 頁面載入...")
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//h1[contains(@class, "ant-typography") and contains(text(), "My Services")]')
            )
        )
        self.log("My Services 頁面已載入完成")
        self.screenshot("my_services_loaded")

    def click_service_card(self, card_title):
        """
        點擊指定服務卡片 (如 'DHCP for Wi-Fi') 進入相對應服務頁面
        """
        self.log(f'尋找卡片「{card_title}」...')
        # 根據你的畫面，卡片標題是 div/styledComponent
        xpath = (
            f'//div[contains(@class, "styledComponents__Title") and starts-with(normalize-space(), "{card_title}")]'
            f'/ancestor::div[contains(@class, "ant-card")]'
        )
        card = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: \'center\'});", card)
        card.click()
        self.log(f'已成功點擊「{card_title}」卡片')
        self.screenshot(f'click_{card_title}_card')
