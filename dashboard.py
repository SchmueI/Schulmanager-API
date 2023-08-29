"""
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def load(driver):
    # Lade Dashboard des Schulmanagers und erwarte widgets
    url = "https://login.schulmanager-online.de/#/dashboard"
    driver.get (url)
    
    try:
        wait = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "widgets-container"))
        )
    except:
        return False, driver
    return True, driver