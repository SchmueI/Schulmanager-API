"""
"""

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def collect(driver):
    output = []

    # Rufe Stundenplan auf
    url = "https://login.schulmanager-online.de/#/modules/schedules/view//"
    driver.get (url)

    # Warte bis der Stundenplan geladen ist
    wait = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "class-hour-calendar"))
    )

    # Mache Stundenplan ausfindig
    html = driver.page_source
    html = html.split("<table",1)[1]
    html = html.split("</table>",1)[0]

    # Finde Zeilen und entferne überflüssige
    rows = html.split ("<tr>")
    del rows [0]
    del rows [0]
    
    # Finde Spalten der Zeile und Ordne zu
    mon = []
    tue = []
    wed = []
    thu = []
    fri = []
    sat = []
    sun = []

    for row in rows:
        td = row.split ("<td>")
        i = 0
        for d in td:
            d = d.split("</td>",1)[0]
            
            if i == 1: mon.append(d)
            if i == 2: tue.append(d)
            if i == 3: wed.append(d)
            if i == 4: thu.append(d)
            if i == 5: fri.append(d)
            if i == 6: sat.append(d)
            if i == 7: sun.append(d)
            
            i = i+1
    
    week = [mon, tue, wed, thu, fri, sat, sun]

    inp = []
    for entity in fri:
        if not "span" in entity:
            inp.append("")
            print ("\n\n\n")
            print ("-----------------------------------------------------")
        else:
            if not ("(" in entity):
                # Wenn keine Information eingeklammert ist, handelt es sich um eine Regelstunde
                elems = entity.split("<span>")
                lesson = elems[1].split("<",1)[0].replace(" ", "").replace("\n", "")
                teacher = elems[3].split("<",1)[0].replace(" ", "").replace("\n", "")
                room = elems[4].split("<",1)[0].replace(" ", "").replace("\n", "")
                print (lesson)
                print (teacher)
                print (room)
                print ("-----------------------------------------------------")
            else:
                print ("\nÄNDERUNG\n")
                print ("-----------------------------------------------------")
