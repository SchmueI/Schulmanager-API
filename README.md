# Schulmanager-API

Automatisierter Zugriff auf Schulmanager durch das Python Selenium Modul.

Diese API ermöglicht die Entwicklung von Drittanbieter-Software, welche auf Schulmanager-Online zugreift. Es handelt sich hierbei ausdrücklich um Drittanbieter Software, die Verwendung erfolgt auf eigenes Risiko.

Der Funktionsumfang orientiert sich an den für die Landesschule Pforta zugänglichen Funktionen, sollte allerdings kompatibel mit anderen Schulen sein.

## Installation
Folgende Module müssen installiert sein:
* selenium

Folgende Programme müssen installiert sein:
* Google Chrome oder Chromium

Anschließend kann dieses Projekt mittels
`git clone https://www.github.com/schmuei/Schulmanager-API`
geklont und ausgeführt werden.

## init.py
### init_driver(headless=True)
<u> Attribut headless (Optional)</u><br>
Das headless Attribut entscheidet darüber ob die Ausführung des Webdrivers ohne grafische Darstellung ausgeführt werden soll. Der Standard ist: Ja.

<u>Funktion</u><br>
Diese Funktion erstellt einen auf chrome basierten Driver und gibt diesen als Rückgabewert aus.

### close_driver(driver)
<u>Attribut driver</u><br>
Dieses Attribut ist erforderlich und bezeichnet den Driver, der geschlossen werden soll.

<u>Funktion</u><br>
Der übergebene Driver wird geschlossen.

## login.py
### login(driver, username, password)<br>
<u>Attribut driver</u><br>
Dieses Attribut ist erforderlich und bezeichnet den Driver, in welchem der Login durchgeführt werden soll

<u>Attribut username</u><br>
Dieses Attribut ist erforderlich und bezeichnet den Nutzernamen oder die E-Mail Adresse des Anmelders.

<u>Attribut password</u><br>
Dieses Attribut ist erforderlich und bezeichnet das Passwort, das zur Anmeldung verwendet werden soll.

<u>Funktion</u><br>
Ermöglicht ein Einloggen mit den bekannten Nutzerdaten. Single-Sign-On wird von dieser API nicht unterstützt<br>
Rückgabewert ist zum einen der Driver mit dem erfolgten Login Versuch sowie ein Boolean, welches den Erfolg des Versuchs angibt.

## schedules.py
### collect (driver)
<u>Attribut driver</u><br>
Dieses Attribut ist erforderlich und bezeichnet den Driver, in welchem der Login durchgeführt werden soll

<u>Funktion</u><br>
Rückgabewert ist ein Array mit den Vertretungsstunden der Woche.

### getPlan (day, driver, ALL=False)
<u>Attribut day</u><br>
Dieses Attribut ist erforderlich und gibt den Tag an, der zurückgegeben werden soll.<br>
0 = Montag<br>
-<br>
6 = Sonntag

<u> Attribut driver</u><br>
Erforderliches Attribut, welches den Driver bezeichnet der für die Operation verwendet werden soll.

<u>Attribut ALL</u><br>
Optionales Attribut. Boolean. Standard = False<br>
Wenn True, wird als Rückgabewert nicht ein Tag sondern eine Woche ausgegeben.

## caldav.py
### collect(driver)
Hinweis: Hier sollte ein Driver verwendet werden, bei welchem bereits eine Anmeldung erfolgreich war.

<u>Attribut driver</u><br>
Dieses Attribut ist erforderlich und bezeichnet den Driver, der verwendet werden soll.

<u>Funktion</u><br>
Als Rückgabewert erhält man ein Array nach folgendem Format: `[YYYY-MM-DD NAME DES EREIGNISSES]`

### getDates(date, driver)
Hinweis: Hier sollte ein Driver verwendet werden, bei welchem bereits eine Anmeldung erfolgreich war.

<u>Attribut date</u><br>
Dieses Attribut ist erforderlich und bezeichnet das Datum, nach welchem gesucht werden soll. Das vorgesehene Format lautet `YYYY-MM-DD`

<u>Attribut driver</u><br>
Dieses Attribut ist erforderlich und bezeichnet den Driver, der verwendet werden soll.

<u>Funktion</u><br>
Rückgabewert dieser Funktion ist ein Array mit Terminen, die an diesem Tag stattfinden.