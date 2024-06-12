# FB Tool - Benutzerverwaltung und Umrechnungen

## Übersicht

Dieses Projekt bietet ein umfassendes Tool zur Benutzerverwaltung sowie verschiedene mathematische und sprachliche Umrechnungsfunktionen. Es beinhaltet:

- Benutzerverwaltung (Erstellen, Löschen, Anzeigen und Ändern von Benutzerrollen)
- Mathematische Umrechnungen (Grad in Bogenmaß, Bogenmaß in Grad, Fahrenheit in Celsius, Celsius in Fahrenheit)
- Sprachliche Übersetzungen (Deutsch zu Englisch, Englisch zu Deutsch, etc.)
- Fakultätsberechnungen
- Primzahlüberprüfungen

## Installation

1. **Klonen Sie das Repository:**

    ```sh
    git clone <Repository-URL>
    cd <Repository-Verzeichnis>
    ```

2. **Erstellen Sie die Datenbank:**

    Führen Sie die Datei `database.sql` aus, um die erforderlichen Tabellen zu erstellen.

    ```sh
    mysql -u root -p < database.sql
    ```

3. **Erstellen Sie einen Admin-Benutzer:**

    Führen Sie `execute.py` aus, um einen Admin-Benutzer mit dem Passwort `1234` zu erstellen.

    ```sh
    python execute.py
    ```

## Nutzung

1. **Starten Sie das Hauptprogramm:**

    ```sh
    python main.py
    ```

2. **Login:**

    - Benutzername: `admin`
    - Passwort: `1234`

3. **Benutzerverwaltung:**

    - Erstellen Sie neue Benutzer
    - Löschen Sie bestehende Benutzer
    - Anzeigen von Benutzerrollen
    - Ändern von Benutzerrollen

## Dateien

- **database.sql:** SQL-Skript zum Erstellen der Datenbank und Tabellen.
- **execute.py:** Python-Skript zum Erstellen eines Admin-Benutzers.
- **main.py:** Hauptprogramm mit allen Funktionen und Menüs.

## Anforderungen

- Python 3.x
- MySQL
- pymysql
- bcrypt

## Hinweis

Stellen Sie sicher, dass MySQL auf Ihrem System installiert und konfiguriert ist. Ändern Sie bei Bedarf die Verbindungseinstellungen in den Python-Skripten (`localhost`, `root`, `1234`, `login_system_umrechner`).

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei `LICENSE`.
