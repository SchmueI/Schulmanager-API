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
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-domain-reliability")
    options.add_experimental_option(
        "prefs", {
            "profile.managed_default_content_settings.images": 2,
            "profile.default_content_settings.popups": 0,    
            "download.default_directory":r""+cwd, ### Set the path accordingly
            "download.prompt_for_download": False, ## change the downpath accordingly
            "download.directory_upgrade": True
        }
    )

    try:
        driver = webdriver.Chrome(options=options)
    except:
        try:
            shutil.rmtree("data/"+userID)
            driver = webdriver.Chrome(options=options)
        except:
            driver = webdriver.Chrome(options=options)

    return driver

def close_driver(driver):
    driver.close()
    driver.quit()
