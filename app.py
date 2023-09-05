"""
    "DIES IST NICHT DAS ENDE"
    - Odradek 2022
"""


from main import init
from main import login
from main import caldav
from main import schedules
from main import dashboard
from main import activities
import lsp.iwe as iwe

import credentials      # This module is not included in the repo since it contains secret credentials

err = "Kein Zugang möglich.\nDas kann zwei Gründe haben:\n-Deine eingegebenen Daten sind falsch\n-Die API ist überlastet.\nPrüfe die Daten und probiere es erneut!"

driver = init.init_driver(headless=True)

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
    print(activities.get(driver, ALL = False, date="2023-09-06"))
else:
    print ("DRIVER DASHBOARD\n" + err)

init.close_driver(driver)
