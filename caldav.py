"""
"""

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def collect(driver):
    
    output = []

    # Rufe Kalender auf
    url = "https://login.schulmanager-online.de/#/modules/calendar/overview"
    driver.get (url)

    # Warte bis Kalender geladen ist
    wait = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "calendar"))
    )

    html = driver.page_source

    # Alle Daten aufsuchen
    entities = html.split("data-date=\"")
    del entities[0]
    del entities[-1]

    # Daten durchsuchen
    for entity in entities:
        if ("<!--" in entity): 
            # Jedes Datum mit Eintrag ausfindig machen
            date = entity.split("\"", 1)[0]
            
            # Titel des entsprechenden Datums extrahieren
            title = entity.split("class=\"fc-event-title fc-sticky\">",1)[1]
            title = title.split("<", 1)[0]
            title = title.split("\n")[1]
            title = title[6:]
            
            outp = date+" "+title

            output.append(outp)
    
    return output
    