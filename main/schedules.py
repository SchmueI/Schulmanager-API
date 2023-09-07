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
    try:
        wait = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "class-hour-calendar"))
        )
    except:
        return []

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

    i = 0
    for day in week:
        inp = []
        for entity in day:
            if not "span" in entity:
                inp.append("")
            else:
                if not ("<span style=\"color" in entity and not "Inter" in entity):
                    # Wenn keine Information eingeklammert ist, handelt es sich um eine Regelstunde
                    """
                    elems = entity.split("<span>")
                    lesson = elems[1].split("<",1)[0].replace(" ", "").replace("\n", "")
                    teacher = elems[3].split("<",1)[0].replace(" ", "").replace("\n", "")
                    room = elems[4].split("<",1)[0].replace(" ", "").replace("\n", "")
                    """


                    lesson = entity.split("timetable-left\">",1)[1].split("timetable-right",1)[0]
                    lesson = lesson.split(">")[2].split("<",1)[0].replace(" ", "").replace("\ņ", "")
                    lesson = lesson.replace("\n", "")

                    teacher = entity.split("timetable-right\">",1)[1].split("timetable-bottom",1)[0]
                    teacher = teacher.split(">")[5].split("<",1)[0].replace(" ", "").replace("\ņ", "")
                    teacher = teacher.replace("\n", "")

                    room = entity.split("timetable-bottom\">",1)[1]
                    room = room.split(">")[3].split("<",1)[0].replace(" ", "").replace("\n", "")
                    room = room.replace("\n", "")

                    if ("fa-info-circle" in entity):
                        # Wenn eine Information ohne Änderung verfügbar ist, handelt es sich um einen Ausfall
                        teacher = "("+teacher+")"
                        lesson = lesson + " → selbst."
                        room = "("+room+")"
                else:
                    # Wenn eine Farbkodierung in der Tabelle vorhanden ist, handelt es sich um eine Änderung
                    lesson = entity.split("timetable-left\">",1)[1].split("timetable-right",1)[0]
                    if not "<span style=\"color:" in lesson:
                        lesson = lesson.split(">")[2].split("<",1)[0].replace(" ", "").replace("\ņ", "")
                    else:
                        old = lesson.split("red;\">")[2].split("<",1)[0]
                        old = old.replace(" ", "")
                        old = old.replace("\n", "")

                        new = lesson.split("green;\">")[1].split("<",1)[0]
                        new = new.replace(" ", "")
                        new = new.replace("\n", "")

                        lesson = old + " → " + new

                    teacher = entity.split("timetable-right\">",1)[1].split("timetable-bottom",1)[0]
                    if not "<span style=\"color:" in teacher:    
                        teacher = teacher.split(">")[5].split("<",1)[0].replace(" ", "").replace("\ņ", "")
                        teacher = teacher.replace("\n", "")
                    else:
                        old = teacher.split("red;\">")[1].split("<",1)[0]
                        old = old.replace(" ", "")
                        old = old.replace("\n", "")

                        new = teacher.split("green;\">")[1].split("<",1)[0]
                        new = new.replace(" ", "")
                        new = new.replace("\n", "")

                        teacher = old + " → " + new

                    room = entity.split("timetable-bottom\">",1)[1]
                    if not "<span style=\"color:" in room:
                        room = room.split(">")[3].split("<",1)[0].replace(" ", "").replace("\n", "")
                    else:
                        old = room.split("red;\">")[2].split("<",1)[0]
                        old = old.replace(" ", "")
                        old = old.replace("\n", "")

                        new = room.split("green;\">")[1].split("<",1)[0]
                        new = new.replace(" ", "")
                        new = new.replace("\n", "")

                        room = old + " → " + new
                
                inp.append(lesson+" "+teacher+" "+room)
        
        week[i] = inp
        i = i+1
    
    return week

def getPlan(day, driver, ALL=False):
    # day sollte ein Integer von 0 (Montag) bis 6 (Sonntag)
    # bzw ein Integer von 0 bis 4 sein.

    DATA = collect(driver)
    if ALL: return DATA
    else: return DATA[day]