"""
"""

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import datetime

def formatted(date, time, lesson):
    # Erwartete Eingabewerte:
    # date: DD.MM.YYYY
    # time: STRING
    # lesson: String
    #
    # Ausgabewert: [str("YYYY-MM-DD"), str(time)+" "+str(lesson)]
    
    day = date.split(".")[0]
    month = date.split(".")[1]
    year = date.split(".")[2]
    fDate = year+"-"+month+"-"+day

    entity = str(time)+" "+str(lesson)

    return [fDate, entity]

def scrape(row):
    # Identifiziere Unterrichtsstunden
    try:
        lesson = row.split("<strong ")[1]
        lesson = lesson.split(">")[1].split("<")[0]
    except:
        return False

    # Identiiziere Datum anhand von Schlüsselattributen
    row = row.split(lesson)[1]
    date = row.split("<td ")[1].split(">")[1].split("\n")[1].split("\n")[0].split(", ")[1].split(",")[0]
    row = row.split(date)[1]

    # Ggf Jahr anfügen
    currentDateTime = datetime.datetime.now()
    year = currentDateTime.date().strftime("%Y")
    if not str(year) in date:
        date = date+year

    # Identifiziere Beginn und Ende der Klausur
    begin = row.split("<br")[1].split(">")[1].split("<")[0].replace(" ", "").replace("\n", "")
    end = " - " + row.split("- ")[1].split("\n")[0]
    time = begin + end

    return formatted(date, time, lesson)

def collect(driver):

    output = []
    
    # Lade HTML des Dashboards
    html = driver.page_source

    # Teste, ob Klausurplan vorhanden ist:
    if "<table " in html:
        text = html.split("<table ")[1]
        text = text.split("</table>")[0]
    else:
        return False

    # Identifiziere Spalten
    rows = text.split("<tr ")
    rows.pop(0)

    # Scrape identifizierte Spalten
    for row in rows:
        scraped = scrape(row)
        if scraped: output.append(scraped)
    
    return output

def get(driver, All = True, Date="2023-01-01"):
    if All: return collect(driver)
    else:
        data = collect(driver)
        for entity in data:
            if entity[0] == Date: return entity[1]
        return False
