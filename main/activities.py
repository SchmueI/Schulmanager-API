"""
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def collect(driver):
    # Der Driver sollte sich im Dashboard befinden.
    
    output = []
    # output Format: [["Datum", "19:00 Floorball", "20:00 Alpakas"], ["Datum", " Uhrzeit Aktivität"], ["Datum", "Uhrzeit Aktivität"],]

    html = driver.page_source

    if "Kommende Termine" in html:
        html = html.split("Kommende Termine")[1]
        html = html.split("</widgets-container>",1)[0]
        html = html.split("<strong ")

        for day in html:
            # Überprüfe, dass in den Tagesdaten eine AG hinterlegt ist.
            if ("AG " in day):
                results = []
                
                # Erfasse Datum:
                date = day.split("\n")[1][-10:]
                results.append(date)

                # Finde Arbeitsgruppen
                events = day.split ("col-2")
                events.pop(0)
                
                for event in events:
                    # Finde die Uhrzeit der AG
                    time = event.split ("\n")[1][-5:]

                    # Finde den Namen der AG
                    entity = event.split("\n")[6]
                    if "AG " in entity: ag = entity[13:]+" AG"

                    appendance = time + " " + ag
                    results.append(appendance)

                output.append(results)
    return output


def get(driver, ALL = False, date="2023-01-01"):
    # date sollte das Datumsformat YYYY-MM-DD haben.
    # driver im Dashboard
    # ALL  -> Alle anstehenden Termine werden genannt [[DATE, a, b],[DATE, c, d]]
    # !ALL -> das spezifische Datum wird zurückgegeben [a, b]


    # Formatiere Datum, um mit dem Format des Schulmanagers zu passen
    date = date.split("-")
    date = date[2]+"."+date[1]+"."+date[0]

    DATES  = collect(driver)
    output = []

    if not ALL:
        for day in DATES:
            if day[0] == date:
                # Das zutreffende Datum ist zurückzugeben.
                output = day

                # Der Datumsstring wird entfernt
                output.pop(0)
    else:
        output = DATES
    
    if (output == []):
        output.append("• Keine Arbeitsgruppen eingeplant.")

    return output