"""
"""

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def collect(driver, url = "https://login.schulmanager-online.de/#/modules/calendar/overview"):
    
    output = []

    # Rufe Kalender auf
    driver.get (url)

    # Warte bis Kalender geladen ist
    try: 
        wait = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "calendar"))
        )
    except:
        return []

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

            time = "00:00"

            if "fc-event-time" in entity:
                time = entity.split("class=\"fc-event-time\">",1)[1]
                time = time.split("<", 1)[0]
                time = time.replace(" " , "")
                time = time.replace("\n", "")
            
            # Titel des entsprechenden Datums extrahieren
            title = entity.split("class=\"fc-event-title fc-sticky\">",1)[1]
            title = title.split("<", 1)[0]
            title = title.split("\n")[1]
            title = title[6:]
            
            outp = date+ " " + time + " "+title

            output.append(outp)
    
    return output

def getDates(date, driver):
    # date sollte das Datumsformat YYYY-MM-DD haben.
    
    DATES = collect(driver)
    output = []
    
    for entity in DATES:
        DATE = entity.split(" ",1)[0]
        if date == DATE:
            output.append(entity.split(" ",1)[1])
    
    return output
    
