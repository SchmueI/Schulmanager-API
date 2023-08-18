"""
    "DIES IST NICHT DAS ENDE"
    - Odradek 2022
"""


import init
import login
import caldav

import credentials      # This module is not included in the repo since it contains secret credentials

driver = init.init_driver()

# Die Zugangsdaten werden von der Datenbank geladen.
# Wenn Sie diese API nutzen wollen, verwenden Sie Ihre eigenen Zugangsdaten.
username = credentials.username()
password = credentials.passwort()

driver = login.login(driver, username=username, password=password)

caldav.collect(driver)

init.close_driver(driver)