"""
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

def load(driver):

    # Lade Account-Seite des Schulmanager und erwarte widgets
    url = "https://login.schulmanager-online.de/#/account"
    driver.get (url)

    try:
        wait = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".widget-tile")
            )
        )
    except:
        return False, driver
    
    if "Angemeldet" in driver.page_source:
        return True, driver
    else:
        sleep(7)
        if "Angemeldet" in driver.page_source:
            return True, driver
        else:
            return False, driver

def fetch_details(driver):
    html = driver.page_source
    html = html.split("Angemeldet")[1]
    html = html.split("<br ")[1].split(">")[1]
    html = html.split("</div")[0]
    html = html.replace("\n", "")

    for char in html:
        if char == " ": html = html[1:]
        else:
            break

    return html

def get_name(driver):
    success, driver = load(driver)

    if success: details = fetch_details(driver)
    else: return success

    surname = details.split(",")[0]
    name = details.split(", ")[1].split(" (")[0]

    return surname, name

def get_class(driver):
    success, driver = load(driver)

    if success: details = fetch_details(driver)
    else: return success

    Class = details.split("(")[1][:2]
    Branch = details.split("(")[1][2]

    return Class, Branch