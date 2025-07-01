from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class ServiceCatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def wait_for_loaded(self):
        """等待 Service Catalog 頁面完全載入"""
        self.log("等待 Service Catalog 頁面載入...")
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//h1[contains(@class, "ant-typography") and contains(text(), "Service Catalog")]')
            )
        )
        self.log("Service Catalog 頁面已載入完成")
        self.screenshot("service_catalog_loaded")

    def click_add_button_on_card(self, card_title):
        """
        點擊指定卡片標題(card_title)的 Add 按鈕
        """
        self.log(f'尋找卡片「{card_title}」的 Add 按鈕...')
        xpath = (
            f'//div[contains(@class,"styledComponents__Title-sc-2p6olq-7") and text()="{card_title}"]'
            f'/ancestor::div[contains(@class,"ant-card")]'
            f'//button[.//span[text()="Add"]]'
        )
        add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        add_button.click()
        self.log(f'已成功點擊「{card_title}」的 Add 按鈕')
        self.screenshot(f"add_{card_title}_clicked")

    # 如果有多種操作，也都可以這樣 log + screenshot 實作

    # 補充：有需要可以加「驗證進入 Add 頁面」的 method
    def assert_add_page_loaded(self, card_title):
        """
        驗證已經進入 Add Service 頁面（以 H1 標題為依據）
        """
        add_title = f"Add {card_title}"
        self.log(f"等待 Add 頁面標題「{add_title}」...")
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f'//h1[contains(text(), "{add_title}")]')
            )
        )
        self.log(f"已成功進入 {add_title} 頁面")
        self.screenshot(f"add_{card_title}_page_loaded")
