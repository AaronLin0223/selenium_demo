from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewFeaturePage(BasePage):
    """新功能頁面 - 演示自動發現功能"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)
    
    def wait_for_loaded(self):
        """等待頁面載入"""
        self.log("等待新功能頁面載入")
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "New Feature")]'))
        )
        self.screenshot("new_feature_page_loaded")
    
    def click_feature_button(self):
        """點擊功能按鈕"""
        self.log("點擊新功能按鈕")
        button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "feature-button"))
        )
        button.click()
        self.screenshot("click_feature_button") 