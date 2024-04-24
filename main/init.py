"""
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



def init_driver(headless=True, PATH="/usr/bin/chromedriver", userID = "0"):
    # Chrome einrichten
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        "prefs", {"profile.managed_default_content_settings.images": 2}
    )

    # Webdriver Einrichten
    options = Options()
    options.headless = headless
    options.add_argument("--window-size=1920,1080")
    options.add_argument("start-maximized")
    options.add_argument("user-agent=Schulmanager-Bot-API")
    options.add_argument("user-data-dir=data/"+userID)

    driver = webdriver.Chrome(options=options)

    return driver

def close_driver(driver):
    driver.close()
    driver.quit()
