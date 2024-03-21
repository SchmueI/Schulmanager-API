"""
"""

def formatted(date, menue):

    # Erwartete Eingabewerte:
    # date: DD.MM.YYYY
    # menue: [tag: meal, tag: meal, tag: meal, .....]
    #
    # Ausgabewert: [str(YYYY-MM-DD), str(meal)]

    day = date.split(".")[0]
    month = date.split(".")[1]
    year = date.split(".")[2]
    fDate = year+"-"+month+"-"+day

    entity = ""
    for e in menue:
        entity = entity + e + "\n\n"

    if entity == "": return False
    return [fDate, entity]

def scrape(row):

    # Identifiziere Datum

    try:
        date = row.split("</u>")[0]
        date = date.split(", ")[1]
    except:
        return False

    # Identifiziere Speisen
    try:
        meals = row.split("</u>")[1]
        meals = meals.split("<strong")

        MENUE = []

        # Für jedes Menü
        for meal in meals:

            if ":" in meal:
                menue = meal.split(">")[1].split(":")[0]+": "
                meal = meal.split(": </strong>")[1].split("<")[0]
                MENUE.append(menue + meal)
    except:
        return False 
    
    return formatted(date, MENUE)


def collect (driver):
    # driver sollte im Dashboard sein

    output = []

    # Lade HTML des Dashboards
    html = driver.page_source

    # Sammle einzelne Elemente
    try:
        tiles = html.split("<div class=\"tile-header\">")
    except:
        return False


    # Teste, ob Speiseplan vorhanden ist
    plan = ""
    for tile in tiles:
        tile = tile.replace("  ", "")
        if "<!---->\nSpeiseplan\n</div>" in tile:
            plan = tile
    if plan == "": return False

    # Identifiziere Zeilen
    plan = plan.split("<u>")
    plan.pop(0)

    # Scrape identifizierte Zeilen
    for row in plan:
        scraped = scrape (row)
        if scraped: output.append(scraped)
    
    return output

    
