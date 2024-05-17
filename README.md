# Schulmanager-API

Mit diesem Tool können Daten der Software Schulmanager-Online abgerufen werden.

Dieser Fetcher ermöglicht die Entwicklung von Drittanbieter-Software, welche auf Schulmanager-Online zugreift. Es handelt sich hierbei ausdrücklich um Drittanbieter Software, die Verwendung erfolgt auf eigenes Risiko.

Der Funktionsumfang orientiert sich an den für die Landesschule Pforta zugänglichen Funktionen, sollte allerdings kompatibel mit anderen Schulen sein.

## Installation
Folgende Module müssen installiert sein:
* selenium

Folgende Programme müssen installiert sein:
* Google Chrome oder Chromium

Anschließend kann dieses Projekt mittels
`git clone https://www.github.com/schmuei/Schulmanager-API`
geklont und ausgeführt werden.

## Verwendungshinweis
Die Verwendung dieser Software erfolgt ausschließlich auf eigenes Risiko. Ich empfehle dringend vor der Inbetriebnahme einer eigenen Software auf Grundlage dieser API mit dem Team von Schulmanager-Online abzustimmen.
In persönlicher Korrespondenz zeigten sich die Betreiber stets freundlich und entgegenkommend - einen Umgangston den es seitens der Anwender dieser Software zu erhalten gilt.

Es ist durchaus wahrscheinlich, dass zum Betreib einer Software auf Grundlage dieser API gefordert wird, einen user-agent zu wählen, der eindeutig auf den Verwendungszweck hinweist. Dies kann durch bearbeitung der init.py vorgenommen werden.

> [!WARNING]
> Der Exzessive Aufruf von Schulmanager-Online Daten mithilfe dieser API kann schwerwiegende Folgen haben. Bitte vor der Verwendung Kontakt mit der Schulmanager Online GmbH aufnehmen!


## Beispiele

### Abrufen des Stunden- und Vertretungsplans
```
from main import init
from main import login
from main import schedules

driver = init.init_driver()
login.login(driver, "nutzer@mail.com", "SicheresPa$$w0rt")

# day: int 0-6 (Montag - Sonntag)
schedules.getPlan(day=0, driver=driver)

init.close_driver(driver)
```

### Abrufen der aktuellen Hausaufgaben
```
from main import init
from main import login
from main import homework

driver = init.init_driver()
login.login(driver, "nutzer@mail.com", "SicheresPa$$w0rt")

homework.get(driver)

init.close_driver(driver)
```

### Abrufen aktueller Termine
```
from main import init
from main import login
from main import caldav

driver = init.init_driver()
login.login(driver, "nutzer@mail.com", "SicheresPa$$w0rt")

caldav.collect(driver)

init.close_driver(driver)
```

### Abrufen anstehender Klausuren
```
from main import init
from main import login
from main import exams

driver = init.init_driver()
login.login(driver, "nutzer@mail.com", "SicheresPa$$w0rt")

exams.get(driver)

init.close_driver(driver)
```

## Dokumentation

### init.py
init.py dient dem Initialisieren und schließen eines Browser-Drivers, der zum Abrufen der Daten von Schulmanager-Online erforderlich ist.

#### init_driver(headless, PATH, userID)

Rückgabewert: WebDriver

> [!NOTE]
> PATH ist ein Überbleibsel und findet in der Funktion keine Anwendung.

| Argument      | Typ          | Erforderlich  | Standard | Beschreibung|
| ------------- |------------- | ------------- | -------- | ----------- | 
| headless      | Boolean      | nein          | True     | Bestimmt, ob der Browser im Hintergrund läuft. |
| PATH          | String       | nein          | "/usr/bin/chromedriver" | Veraltet: Dateipfad für Chrome |
| userID        | String       | nein          | "0"      | Gibt eine Nutzerkennung für die Verwendung eines dedizierten Browser-Caches an.|

#### close_driver(driver)
> [!IMPORTANT]
> Driver sollten nach erfolgter Operation geschlossen werden, um unnötige RAM beanspruchung zu vermeiden.

| Argument      | Typ          | Erforderlich  | Standard | Beschreibung|
| ------------- |------------- | ------------- | -------- | ----------- | 
| driver        | WebDriver    | Ja            | /        | Driver, der geschlossen werden soll |

#### Beispiel
```
from main import init

driver = init.init_driver()

init.close_driver(driver)
```

### login.py
Mithilfe der login.py wird der Zugang zum Dashboard des Schulmanagers ermöglicht

#### login(driver, username, password, verbose)

Rückgabewert: Boolean, driver<br>
Boolean: Anmeldung erfolgreichn<br>
driver: verwendeter WebDrivern<br>
<br>
Rückgabewert (verbose): Boolean, driver, Boolean<br>
Boolean: Anmeldung erfolgreichn<br>
driver: verwendeter WebDrivern<br>
Boolean: Cache verwendetn<br>

| Argument      | Typ          | Erforderlich  | Standard | Beschreibung|
| ------------- |------------- | ------------- | -------- | ----------- | 
| driver        | WebDriver    | ja            | /        | Zu verwendender WebDriver |
| username      | String       | ja            | /        | Nutzername, idR E-Mail Adresse des Nutzers |
| password      | String       | ja            | /        | Passwort des Nutzers |
| verbose       | Boolean      | nein          | False    | True: siehe Rückgabewert |

#### Beispiel
```
from main import init
from main import login

driver = init.init_driver()
login.login(driver, "nutzer@mail.com", "SicheresPa$$w0rt")

init.close_driver(driver)
```

### account.py
> [!Important]
> Für diese und alle weiteren Module ist es erforderlich, einen driver mit angemeldeten User übergeben. Siehe Beispiele!

Zum Abrufen der Stammdaten des Nutzers

#### get_name(driver)

Rückgabewert: String, String<br>
String: Nachname <br>
String: Vorname

| Argument      | Typ          | Erforderlich  | Standard | Beschreibung|
| ------------- |------------- | ------------- | -------- | ----------- | 
| driver        | WebDriver    | ja            | /        | Zu verwendender WebDriver |

#### get_class(driver)

Rückgabewert: String, String<br>
String: Jahrgang <br>
String: Zweig

| Argument      | Typ          | Erforderlich  | Standard | Beschreibung|
| ------------- |------------- | ------------- | -------- | ----------- | 
| driver        | WebDriver    | ja            | /        | Zu verwendender WebDriver |

#### Beispiel
```
from main import init
from main import login
from main import account

driver = init.init_driver()
login.login(driver, "nutzer@mail.com", "SicheresPa$$w0rt")

print (account.get_name(driver))
# Output ("Mustermann", "Max")

print (account.get_class(driver))
# Output ("10", "a")

init.close_driver(driver)
```

### activities.py
Finde Veranstaltungen und Arbeitsgemeinschaften

> [!IMPORTANT]
> Dieses Verfahren lädt die Aktivitäten aus dem Dashboard, nicht aus dem Kalender!
> Zum Laden von Kalendereinträgen siehe caldav.py

#### get(driver, ALL, date, cal)
Rückgabewert: Array <br>
Konstruktion: [["DD.MM.YYYY", "Eintrag 1", "Eintrag 2"], ["DD.MM.YYYY", "Eintrag 1", ....], .....]

| Argument      | Typ          | Erforderlich  | Standard | Beschreibung|
| ------------- |------------- | ------------- | -------- | ----------- | 
| driver        | WebDriver    | ja            | /        | Zu verwendender WebDriver |
| ALL           | Boolean      | nein          | False    | Ignoriere Datum und gebe alle Daten zurück |
| date          | String       | nein          | "2023-01-01"        | Abzufragendes Datum |
| cal           | Boolean      | nein          | False    | True: Rückgabe aller Einträge, außer AGs<br>False: Rückgabe aller AGs ohne Termine |

#### Beispiel
```
from main import init
from main import login
from main import activities

driver = init.init_driver()
login.login(driver, "nutzer@mail.com", "SicheresPa$$w0rt")

activities.get(driver, ALL=True)
# Output aller AGs

init.close_driver(driver)
```

### caldav.py
Öffne Kalender und lade Termine

#### getDates(date, driver)
Rückgabewert: Array <br>
Konstruktion: ["Termin 1", "Termin 2", .....]

| Argument      | Typ          | Erforderlich  | Standard | Beschreibung|
| ------------- |------------- | ------------- | -------- | ----------- | 
| driver        | WebDriver    | ja            | /        | Zu verwendender WebDriver |
| date          | String       | ja            | /        | String des Tages, der geladen werden soll.<br>Format: YYYY-MM-DD |

#### Beispiel
```
from main import init
from main import login
from main import caldav

driver = init.init_driver()
login.login(driver, "nutzer@mail.com", "SicheresPa$$w0rt")

caldav.getDates("2024-05-20", driver)
# Output aller Termine
# ["Pfingstmontag", "Beginn der Ferien"]

init.close_driver(driver)
```

### dashboard.py
Lade das Dashboard

> [!TIP]
> Nach dem Login wird automatisch das Dashboard geladen. Einige Module setzen voraus, dass die Operation im Dashboard gestartet wird. Bei Unklarheit, ob das Dashboard zuvor geladen werden muss, ist es nicht schädlich, diese Funktion aufzurufen.

#### load(driver)
| Argument      | Typ          | Erforderlich  | Standard | Beschreibung|
| ------------- |------------- | ------------- | -------- | ----------- | 
| driver        | WebDriver    | ja            | /        | Zu verwendender WebDriver |

#### Beispiel
```
from main import init
from main import login
from main import caldav
from main import activities
from main import dashboard

driver = init.init_driver()
login.login(driver, "nutzer@mail.com", "SicheresPa$$w0rt")

caldav.getDates("2024-05-20", driver)

dashboard.load(driver)

activities.get(driver, ALL=True)

init.close_driver(driver)
```

### exams.py
Anstehende Klausuren und Klassenarbeiten

#### collect(driver)
Rückgabewert: Array <br>
Konstruktion: [["DD.MM.YYYY", "Eintrag 1", "Eintrag 2"], ["DD.MM.YYYY", "Eintrag 1", ....], .....]

| Argument      | Typ          | Erforderlich  | Standard | Beschreibung|
| ------------- |------------- | ------------- | -------- | ----------- | 
| driver        | WebDriver    | ja            | /        | Zu verwendender WebDriver |

#### get (driver, All, Date)
Rückgabewert: Array <br>
Konstruktion: ["Eintrag 1", "Eintrag 2"]

| Argument      | Typ          | Erforderlich  | Standard | Beschreibung|
| ------------- |------------- | ------------- | -------- | ----------- | 
| driver        | WebDriver    | ja            | /        | Zu verwendender WebDriver |
| All           | Boolean      | nein          | False    | Ignoriere Datum und gebe alle Daten zurück <br>(Format siehe collect(driver)) |
| date          | String       | nein          | "2023-01-01"        | Abzufragendes Datum |

#### Beispiel
```
from main import init
from main import login
from main import exams

driver = init.init_driver()
login.login(driver, "nutzer@mail.com", "SicheresPa$$w0rt")

exams.get(driver, All=False, Date="2024-05-17")
# Output der Arbeiten am Datum

exams.collect(driver)
# Output aller anstehenden Arbeiten

init.close_driver(driver)
```

### homework.py
Anstehende Klausuren und Klassenarbeiten

#### collect(driver)
Rückgabewert: Array <br>
Konstruktion: [["DD.MM.YYYY", "Eintrag 1", "Eintrag 2"], ["DD.MM.YYYY", "Eintrag 1", ....], .....]

| Argument      | Typ          | Erforderlich  | Standard | Beschreibung|
| ------------- |------------- | ------------- | -------- | ----------- | 
| driver        | WebDriver    | ja            | /        | Zu verwendender WebDriver |

#### get (driver, All, Date)
Rückgabewert: Array <br>
Konstruktion: ["Eintrag 1", "Eintrag 2"]

| Argument      | Typ          | Erforderlich  | Standard | Beschreibung|
| ------------- |------------- | ------------- | -------- | ----------- | 
| driver        | WebDriver    | ja            | /        | Zu verwendender WebDriver |
| All           | Boolean      | nein          | False    | Ignoriere Datum und gebe alle Daten zurück <br>(Format siehe collect(driver)) |
| date          | String       | nein          | "2023-01-01"        | Abzufragendes Datum |

#### Beispiel
```
from main import init
from main import login
from main import homework

driver = init.init_driver()
login.login(driver, "nutzer@mail.com", "SicheresPa$$w0rt")

homework.get(driver, All=False, Date="2024-05-17")
# Output der Hausaufgaben zum Datum

homework.collect(driver)
# Output aller anstehenden Hausaufgaben

init.close_driver(driver)
```

### meal.py
Lade den Speiseplan, sofern er im Dashboard vorhanden ist.
> [!IMPORTANT]
> Diese Funktion setzt voraus, dass der Speiseplan im Dashboard hinterlegt wurde.

#### collect(driver)

Rückgabewert: Array oder False <br>
Konstruktion: Konstruktion: [["YYYY-MM-DD", "Eintrag 1", "Eintrag 2"], ["YYYY-MM-DD", "Eintrag 1", ....], .....]

> [!TIP]
> Wenn kein Speiseplan gefunden wurde, ist der Rückgabewert False. In Python ist bei Boolischen Abfragen auf Strings der Rückgabewert immer dann True, wenn der Wert nicht "" ist. Somit kann man beispielsweise vor der Ausgabe in einem Drittanbieterprogramm das Vorhandensein des Speiseplans mit einer if-Abfrage prüfen.

| Argument      | Typ          | Erforderlich  | Standard | Beschreibung|
| ------------- |------------- | ------------- | -------- | ----------- | 
| driver        | WebDriver    | ja            | /        | Zu verwendender WebDriver |

#### Beispiel
```
from main import init
from main import login
from main import meal

driver = init.init_driver()
login.login(driver, "nutzer@mail.com", "SicheresPa$$w0rt")

meal.collect(driver)
# Output aller Speisen

init.close_driver(driver)
```

### schedules.py
Lade den aktuellen Stunden- und Vertretungsplan

#### getPlan(day, driver, ALL, startDate)
Rückgabewert: Array <br>
Konstruktion: ["Eintrag 1", "Eintrag 2"]
<br><br>
Wenn ALL:<br>
Rückgabewert: Array oder False <br>
Konstruktion: Konstruktion: [["YYYY-MM-DD", "Eintrag 1", "Eintrag 2"], ["YYYY-MM-DD", "Eintrag 1", ....], .....]

| Argument      | Typ          | Erforderlich  | Standard | Beschreibung|
| ------------- |------------- | ------------- | -------- | ----------- | 
| driver        | WebDriver    | ja            | /        | Zu verwendender WebDriver |
| All           | Boolean      | nein          | False    | Ignoriere Datum und gebe alle Daten zurück <br>(Format siehe Beschreibung) |
| day           | Int          | ja            | /        | Abzurufender Tag (0-6)<br>0: Montag<br>6: Sonntag |
| startDate     | String       | nein          | ""       | Startdatum der Woche inkl URL-Erweiterung. |

#### Beispiel
```
from main import init
from main import login
from main import schedules

driver = init.init_driver()
login.login(driver, "nutzer@mail.com", "SicheresPa$$w0rt")

schedules.getPlan(3, driver)
# Gibt den Stundenplan des dieswöchigen Mittwoch aus

schedules.getPlan(0, driver, ALL=True)
# Gibt den Stundenplan der gesamten Woche aus

schedules.getPlan(3, driver, startDate="?start=2024-05-27")
# Gibt den Stundenplan des Mittwochs der Kalenderwoche vom 27.05.2024 aus.

schedules.getPlan(3, driver, startDate="?start=2024-05-27", ALL=True)
# Gibt den Stundenplan der gesamten Woche vom 27.05.2024 aus.

init.close_driver(driver)
```