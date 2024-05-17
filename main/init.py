"""
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import os
import shutil



def init_driver(headless=True, PATH="/usr/bin/chromedriver", userID = "0"):

    # Aktuellen Dateipfad ermitteln:
    cwd = os.getcwd()

    # Webdriver Einrichten
    options = Options()
    if headless: options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("start-maximized")
    options.add_argument("user-agent=Schulmanager-Bot-API")
    options.add_argument("user-data-dir=data/"+userID)
    options.add_experimental_option(
        "prefs", {
            "profile.managed_default_content_settings.images": 2,
            "profile.default_content_settings.popups": 0,    
            "download.default_directory":r""+cwd, ### Set the path accordingly
            "download.prompt_for_download": False, ## change the downpath accordingly
            "download.directory_upgrade": True
        }
    )

    driver = webdriver.Chrome(options=options)

    return driver

def close_driver(driver):
    driver.close()
    driver.quit()
