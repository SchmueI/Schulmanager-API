"""
    "DIES IST NICHT DAS ENDE"
    - Odradek 2022
"""


import init
import login
import caldav
import schedules

import credentials      # This module is not included in the repo since it contains secret credentials

driver = init.init_driver()

# Die Zugangsdaten werden von der Datenbank geladen.
# Wenn Sie diese API nutzen wollen, verwenden Sie Ihre eigenen Zugangsdaten.
username = credentials.username()
password = credentials.passwort()
username = "Falsche Daten."

success, driver = login.login(driver, username=username, password=password)

if success:
     #caldav.getDates("2023-09-01", driver)
    schedules.getPlan(3, driver)
else:
    print ("Kein Zugang möglich.\nDas kann zwei Gründe haben:\n-Deine eingegebenen Daten sind falsch\n-Die API ist überlastet.\nPrüfe die Daten und probiere es erneut!")

init.close_driver(driver)