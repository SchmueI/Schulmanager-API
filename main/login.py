from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def insert_data(driver, username, password):

    # Warte, bis das LoginFeld erscheint.
    # Dieser Versuch wird maximal fünf Mal wiederholt.
    for i in range (5) :
        try:
            wait = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, 'emailOrUsername'))
            )
        except:
            continue
        break

    # Finde Input-Feld für die Eingabe des Nutzernamens:
    username_input_elem = driver.find_element(By.ID, "emailOrUsername")

    # Finde Input-Feld für die Eingabe des Passworts:
    password_input_elem = driver.find_element(By.ID, "password")

    # Eingabe der Zugangsdaten
    username_input_elem.send_keys(username)
    password_input_elem.send_keys(password + Keys.RETURN)

    # Erwarte Login
    try:
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "accountDropdown"))
        )
    except:
        return False, driver
    return True, driver


def login(driver, username, password, verbose=False):
    driver.get ("https://login.schulmanager-online.de/#/login")

    # Versuche automatischen Login
    try:
        wait = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "widgets-container"))
        )
    except:
        # Wenn der Versuch scheitert, gebe Daten ein
        success, driver = insert_data(driver, username, password)
        if verbose: return success, driver, False
        else: return success, driver

    if verbose: return True, driver, True
    else: return True, driver


    # Return Value:
    # [Bool: Success], driver, [Bool: useCache]