from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login_to_R1_UI(driver, env, username, password):
    print("Starting login process...")
    
    # open Chrome
    driver.get(f"https://{env}.ruckus.cloud/")

    # maximize window
    # The env here is the environment you want to log in, e.g.., dev、staging etc.
    driver.maximize_window()

    # create a WebDriverWait，wait up to 10 seconds
    wait = WebDriverWait(driver, 10)

    # Wait for the account field to appear, then enter the account
    username_input = wait.until(
        EC.presence_of_element_located((By.NAME, "user[username]"))
    )
    username_input.send_keys(username)


    # Wait for the password field to appear, then enter the password
    password_input = wait.until(
        EC.presence_of_element_located((By.NAME, "user[password]"))
    )
    password_input.send_keys(password)

    # Wait for the login button to be clickable, then click it
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "ruckus-one-submit-button"))
    )
    login_button.click()
    
    
    # Wait for the homepage element to appear (e.g., id="dashboard")
    dashboard_menu = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-label="Dashboard"].active'))
    )
    time.sleep(5)

    # Screenshot
    print("The Dashboard element has appeared and the page has been loaded successfully!")
    driver.save_screenshot("R1_UI_login.png")
    print("Screenshot saved as R1_UI_login.png")


