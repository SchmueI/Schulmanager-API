from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    driver.get ("https://login.schulmanager-online.de/#/login")

    # Warte, bis das LoginFeld erscheint.
    wait = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'emailOrUsername'))
    )

    # Finde Input-Feld für die Eingabe des Nutzernamens:
    username_input_elem = driver.find_element(By.ID, "emailOrUsername")

    # Finde Input-Feld für die Eingabe des Passworts:
    password_input_elem = driver.find_element(By.ID, "password")

    # Eingabe der Zugangsdaten
    username_input_elem.send_keys(username)
    password_input_elem.send_keys(password + Keys.RETURN)

    # Erwarte Login
    try:
        wait = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "accountDropdown"))
        )
    except:
        return False, driver

    return True, driver