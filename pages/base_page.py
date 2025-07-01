import os
import time
from utils.log import logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def log(self, msg, level="info"):
        getattr(logger, level)(msg)  # logger.info(msg) 或 logger.error(msg)

    def screenshot(self, step):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        filename = os.path.join(screenshot_dir, f"{step}_{timestamp}.png")
        self.driver.save_screenshot(filename)
        self.log(f"Screenshot saved: {filename}")
        return filename
