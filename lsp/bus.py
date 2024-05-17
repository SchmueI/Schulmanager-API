"""

Dieses Modul ist spezifisch für den Awnwendungsfall der Landesschule Pforta geschrieben.
Verwendet für die Bus-Anmeldung wird das schulmanager-online Modul der Wahlpflicht-Kurswahl.
Eventuell lässt sich dieses Verfahren analog auf andere Kurse anderer Schulen anwenden.

"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def callRegistration(driver):
    # Der Driver sollte sich im Dashboard befinden.


    html = driver.page_source
    # Suche Link zur Bus Anmeldung
    if "Busanmeldung" in html:
        html = html.split("Busanmeldung", 1)[1]
        html = html.split("</div>", 2)[1]
        html = html.split("href=\"")[1].split("\"",1)[0]

        # Rufe Anmeldung auf
        url = "https://login.schulmanager-online.de/"+html
        driver.get(url)

        # Warte, bis Auswahlfeld erscheint
        try:
            wait = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, "instance-select"))
            )
        except:
            return False, driver

        # Klicke auf Auswahlfeld
        selector = driver.find_element(By.TAG_NAME, "instance-select")

        AC(driver)\
            .click(selector)\
            .perform()
    
        try:
            wait = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, "ng-dropdown-panel"))
            )
        except:
            return False, driver
        

        return True, driver
    else:
        return False, driver

def sendData(driver, mode):
    # Finde das Suchfeld zur Eingabe des Modus

    try:
        wait = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ng-option"))
        )
    except:
        print ("kann Optionen nicht finden")
        return False, driver 

    search = driver.find_elements(By.TAG_NAME, "input")[1]
    

    if mode == 1: search.send_keys("12:11"    + Keys.DOWN + Keys.RETURN + Keys.TAB + Keys.RETURN)
    if mode == 2: search.send_keys("12:50" + Keys.DOWN + Keys.RETURN + Keys.TAB + Keys.RETURN)
    if mode == 3: search.send_keys("13:02" + Keys.DOWN + Keys.RETURN + Keys.TAB + Keys.RETURN)
    
    if mode == 0:
        #Finde den Knopf zum Löschen der Anmeldung
        cancel = driver.find_elements(By.CLASS_NAME, "btn-danger")
        
        # Klicke Löschen
        AC(driver)\
            .click(cancel[0])\
            .click(cancel[0])\
            .perform()
            
        # Warte auf Bestätigungsfeld
        try:
            wait = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "modal-body"))
            )
        except:
            print ("kann Bus Anmeldung nicht löschen")
            return False, driver 
        
        # Finde Bestätigungs Knopf
        cancel = driver.find_elements(By.CLASS_NAME, "btn-danger")
        
        # Klicke Bestätigung
        AC(driver)\
            .click(cancel[1])\
            .click(cancel[1])\
            .perform()
        

    return True, driver

def getState(driver):
    # Warte bis Bus-Auswahl geladen ist.
    try:
        wait = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ng-option"))
        )
    except:
        print ("kann Optionen nicht finden")
        return False, driver 
    
    # Lade Seitenquelltext
    html = driver.page_source
    state = ""

    # Suche ausgewählte Bus-Einwahl
    if ("ng-value-label" in html):
        state = html.split("ng-value-label\">")[1].split("<",1)[0]
    elif ("ng-placeholder" in html):
        state = "Nicht angemeldet"
    else:
        return True, "keine Angabe", driver

    return True, state, driver

def register (driver, mode=1):
    # driver sollte im Dashboard sein.
    # mode = 1 - Bus 12:11 (Linie) Bushaltestelle
    # mode = 2 - Bus 12:50 (Zusatz) Stiftung
    # mode = 3 - Bus 13:02 (Linie) Abfahrort nach Schülerzahl
    # mode = 0 - Abmelden

    success, driver = callRegistration(driver)
    if not success:
        return False, driver
    
    success, driver = sendData(driver, mode)
    return success, driver

def status (driver):
    # Driver sollte im Dashboard sein.

    success, driver = callRegistration(driver)
    if not success:
        return False, "Keine Busanmeldung gefunden.", driver
    
    success, state, driver = getState(driver)
    return success, state, driver