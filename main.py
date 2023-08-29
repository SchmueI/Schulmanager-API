"""
    "DIES IST NICHT DAS ENDE"
    - Odradek 2022
"""


import init
import login
import caldav
import schedules
import dashboard
import lsp.iwe as iwe

import credentials      # This module is not included in the repo since it contains secret credentials

err = "Kein Zugang möglich.\nDas kann zwei Gründe haben:\n-Deine eingegebenen Daten sind falsch\n-Die API ist überlastet.\nPrüfe die Daten und probiere es erneut!"

driver = init.init_driver(headless=False)

# Die Zugangsdaten werden von der Datenbank geladen.
# Wenn Sie diese API nutzen wollen, verwenden Sie Ihre eigenen Zugangsdaten.
username = credentials.username()
password = credentials.passwort()
#username = "Falsche Daten."

success, driver = login.login(driver, username=username, password=password)
if success:
    success, driver = dashboard.load(driver)
else:
    print ("DRIVER LOGIN\n" + err)

if success:
    iwe.register(driver)
else:
    print ("DRIVER DASHBOARD\n" + err)

init.close_driver(driver)
