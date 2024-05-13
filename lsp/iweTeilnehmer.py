"""

Dieses Modul ist spezifisch für den Awnwendungsfall der Landesschule Pforta geschrieben.
Verwendet für die IWE-Teilnehmerliste wird das schulmanager-online Modul der Dokumente.
Eventuell lässt sich dieses Verfahren analog auf andere Dokumente anderer Schulen anwenden.

"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import camelot
import json

from time import sleep


def download(driver):

    # Lösche ggf vorhandene Teilnehmerliste
    for item in os.listdir(os.getcwd()):
        if item.endswith(".pdf"): os.remove(item)
    
    # Rufe Dokumente URL auf
    url = "https://login.schulmanager-online.de/#/modules/documents/browse?folders=93389%2C109804%2C109857%2C109858"
    driver.get(url)

    # Warte bis Dokumentenauswahl geladen ist:
    try:
        wait = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.CLASS_NAME, "document"))
        )
    except:
        return False, driver
    
    # Klicke auf erstes Dokument
    selector = driver.find_elements(By.CLASS_NAME, 'document')

    AC(driver)\
        .click(selector[0])\
        .perform()

    
    # Warte bis Seite erscheint
    try:
        wait = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.CLASS_NAME, "fa-download"))
        )
    except:
        print ("Seite nicht gefunden")
        return False, driver

    # Lade PDF herunter
    selector = driver.find_elements(By.CLASS_NAME, 'fa-download')
    
    AC(driver)\
        .click(selector[0])\
        .perform()
    

    return True, driver

def read():
    pdfFile = ""
    text = ""

    # Lokalisiere PDF Datei
    for item in os.listdir(os.getcwd()):
        if item.endswith(".pdf"): pdfFile = item
    
    if not pdfFile == "":
        # Lese Datei
        tables = camelot.read_pdf(pdfFile, pages="all")
    else:
        print ("Datei konnte nicht gefunden werden.") 
        return "Datei konnte nicht gefunden werden."

    contents = []
    for i in range (len(tables)):
        contents.append(json.loads(tables[i].df.to_json()))
    
    outp = ""
    for table in contents:

        try:
            head = [*table["0"].values()]
            names = [*table["1"].values()] 
            Class = [*table["2"].values()]

            if "IWE" in head[0] or "Sa." in head[0]:
                outp = outp + "\n<b>"+head[0]+"</b>\n" 


            if (len(names) == len(Class)):
                for i in range (len(names)):
                    if not str(names[i]) == "":
                        outp = outp  + (str(names[i]) + " : " + str(Class[i])) + "\n"
        except:
            # Manchmal liest Camelot den gesamten Tabelleninhalt in eine einzelne Zeile ein.
            inner = [*table["0"].values()]
            
            for item in inner:
                if "Sa." in item:
                    outp = outp + "\n<b>"+item+"</b>\n"
                else:
                    if "\n" in item:
                        item = item.split("\n")
                        try:
                            if not (item[1] == ""):
                                outp = outp + item[1] + " : " + item[2] + "\n"
                        except:
                            continue
        finally:
            continue
    
    return outp



def getParti(driver):
    success, driver = download(driver)
    
    if not success:
        return False, driver
    
    sleep(2)
    read()
