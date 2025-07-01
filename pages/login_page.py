from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver, env):
        super().__init__(driver)
        self.env = env

    def login(self, username, password):
        self.log("Navigating to login page...")
        self.driver.get(f"https://{self.env}.ruckus.cloud/")
        self.driver.maximize_window()
        self.screenshot("open_login_page")

        wait = WebDriverWait(self.driver, 15)
        self.log("Waiting for username input...")
        username_input = wait.until(
            EC.presence_of_element_located((By.NAME, "user[username]"))
        )
        username_input.send_keys(username)
        self.screenshot("entered_username")

        self.log("Waiting for password input...")
        password_input = wait.until(
            EC.presence_of_element_located((By.NAME, "user[password]"))
        )
        password_input.send_keys(password)
        self.screenshot("entered_password")

        self.log("Clicking login button...")
        login_button = wait.until(
            EC.element_to_be_clickable((By.ID, "ruckus-one-submit-button"))
        )
        login_button.click()
        self.screenshot("clicked_login")

        self.log("Waiting for Dashboard to appear...")
        dashboard_menu = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-label="Dashboard"].active'))
        )
        self.screenshot("dashboard_loaded")
        self.log("Login successful! Dashboard loaded.")
