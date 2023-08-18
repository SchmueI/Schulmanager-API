"""
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def init_driver(headless=True):
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

    driver = webdriver.Chrome(options=options)

    return driver

def close_driver(driver):
    driver.close()
    driver.quit()
