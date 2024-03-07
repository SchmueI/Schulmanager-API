"""
"""

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def collect(driver):

    output = []
    
    #Lade HTML des Dashboards
    html = driver.page_source

    # Teste, ob Klausurplan vorhanden ist:
    if "<table " in html:
        text = html.split("<table ")[1]
        text = text.split("</table>")[0]
    else:
        return False

    # Identifiziere Unterrichtsstunden
    try:
        lessons = text.split("<strong ")
        i = 0
        for lesson in lessons:
            lessons[i] = lesson.split(">")[1].split("<")[0]
            i = i+1
    except:
        return False

    # Ggf ist der erste Eintrag eine Leerzeile und muss entfernt werden
    if "\n" in lessons[0]:
        lessons.pop(0)
        
    print (lessons)
    print (text)