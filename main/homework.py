"""
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

def load (driver):

    # Lade Account-Seite des Schulmanager und erwarte widgets
    url = "https://login.schulmanager-online.de/#/modules/classbook/homework/"
    driver.get (url)

    try:
        wait = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".tile")
            )
        )
    except:
        return False, driver
    
    if "Hausaufgaben" in driver.page_source:
        return True, driver
    else:
        sleep(7)
        if "Hausaufgaben" in driver.page_source:
            return True, driver
        else:
            return False, driver

def formatted (date, lessons, tasks):
    # Erwartete Eingabewerte:
    # date: DD.MM.YYYY
    # lesson: STRING
    # task: String
    #
    # Ausgabewert: [str("YYYY-MM-DD"), str(lesson)+": "+str(task)]

    outp = []

    try:
        day = date.split(".")[0]
        month = date.split(".")[1]
        year = date.split(".")[2]
        
        fDate = year+"-"+month+"-"+day
        outp.append(fDate)

        iterations = len(lessons)
    except: return False

    entity = ""
    for i in range (iterations):
        entity = lessons[i] + ": " + tasks[i]
        outp.append(entity)

    return outp

def scrape (block):
    
    # Identifiziere Datum
    try:    
        date = block.split(", ",1)[1].split("\n")[0]
    except:
        return False

    # Identifiziere Fach
    try:
        lessons = block.split("<h4 ")
        lessons.pop(0)
        i = 0
        for lesson in lessons:
            lesson = lesson.split(">")[1].split("<")[0]
            lessons[i] = lesson
            i = i+1
    except:
        return False

    # Identifiziere Aufgabe
    try:
        tasks = block.split("<span ")
        tasks.pop(0)
        i = 0
        for task in tasks:
            task = task.split(">")[1].split("<")[0]
            tasks[i] = task
            i = i+1
    except:
        return False

    return formatted (date, lessons, tasks)


def collect (driver):

    output = []
    # output Format [["Datum", "Fach: Aufgabe", "Fach: Aufgabe"], ["Datum", "Fach: Aufgabe"], ..... ]

    # Rufe Hausaufgabenliste auf
    success, driver = load (driver)
    if not success: return success

    html = driver.page_source

    # Identifiziere Blöcke
    blocks = html.split("tile\">")
    blocks.pop(0)
    try:
        blocks.pop(len(blocks)-1)
    except:
        # Wenn keine Hausaufgaben vergeben wurden, scheitert diese Operation.
        # In dem Fall gebe False zurück.
        return False

    # Scrape identifizierte Blöcke
    for block in blocks:
        scraped = scrape(block)
        if scraped: output.append(scraped)

    return output
    

def get (driver, All = True, Date="2023-01-01"):
    if All: return collect (driver)
    else:
        data = collect(driver)
        if not data: return data
        for entity in data:
            if entity[0] == Date:
                entity.pop(0)
                return entity
