"""
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def load (driver):

    # Lade Account-Seite des Schulmanager und erwarte widgets
    url = "https://login.schulmanager-online.de/#/modules/classbook/homework/"
    driver.get (url)

    try:
        wait = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".tile")
            )
        )
    except:
        return False, driver
    
    if "Hausaufgaben" in driver.page_source:
        return True, driver
    else:
        sleep(7)
        if "Hausaufgaben" in driver.page_source:
            return True, driver
        else:
            return False, driver

def collect (driver):

    output = []
    # output Format [["Datum", "Fach: Aufgabe", "Fach: Aufgabe"], ["Datum", "Fach: Aufgabe"], ..... ]

    # Rufe Hausaufgabenliste auf
    success, driver = load (driver)
    if not success: return success

    html = driver.page_source
        
    

def get (driver, All = True, Date="2023-01-01"):
    if All: return collect (driver)
    else:
        data = collect(driver)
        if not data: return data
        for entity in data:
            if entity[0] == Date:
                entity.pop[0]
                return entity