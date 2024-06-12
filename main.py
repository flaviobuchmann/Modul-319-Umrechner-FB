import sys
import os
import getpass
import time
import bcrypt

from Library.Math import grad_in_bogenmass, bogenmass_in_grad, fahrenheit_in_celsius, celsius_in_fahrenheit, fakultaet, Primzahlfunktion
from Library.Language import (deutsch_englisch, englisch_deutsch, deutsch_italienisch, 
                      italienisch_deutsch, deutsch_spanisch, spanisch_deutsch, 
                      deutsch_franzoesisch, franzoesisch_deutsch)
from Library.SQL import connect_to_database, verify_login, close_connection, create_user, delete_user, get_all_users, get_user_role, update_user_role as sql_update_user_role
from Library.DataTypes import is_int, is_float, is_string, is_list, is_tuple, is_dict, is_bool

os.system('cls')

# Global connection variable
connection = None

def connect():
    global connection
    if connection is None or not connection.open:
        connection = connect_to_database("localhost", "root", "1234", "login_system_umrechner")
        if not connection:
            print("Verbindung zur Datenbank fehlgeschlagen. Programm wird beendet.")
            sys.exit()

def login():
    username = input("Benutzername: ")
    password = getpass.getpass("Passwort: ")

    os.system('cls')

    user = verify_login(connection, username, password)
    if user:
        print("Login erfolgreich!")
        return user
    else:
        print("Login fehlgeschlagen. Bitte versuchen Sie es erneut.")
        return None

def umrechner():
    while True:
        print("========== Umrechner von FB ==========")
        print('''1: Grad in Bogenmass
2: Bogenmass in Grad
3: Fahrenheit in Celsius
4: Celsius in Fahrenheit
0: Zurück zum Hauptmenü
=======================================''')

        valideauswahl = False
        while not valideauswahl:
            menü_auswahl = input("Bitte wählen Sie eine Option: ")
            os.system('cls')
            if menü_auswahl == "1":
                print("========== Grad in Bogenmass ==========")
                while True:
                    try:
                        gradanzahl = float(input("Geben sie ihre Gradanzahl ein: "))
                        break
                    except ValueError:
                        print("Ungültige Eingabe. Bitte eine gültige Zahl eingeben.")
                bogenmass = grad_in_bogenmass(gradanzahl)
                os.system('cls')
                print(f"{gradanzahl} Grad entsprechen {bogenmass} im Bogenmass.")
                valideauswahl = True
            elif menü_auswahl == "2":
                print("========== Bogenmass in Grad ==========")
                while True:
                    try:
                        bogenmass = float(input("Geben sie ihr Bogenmass ein: "))
                        break
                    except ValueError:
                        print("Ungültige Eingabe. Bitte eine gültige Zahl eingeben.")
                grad = bogenmass_in_grad(bogenmass)
                os.system('cls')
                print(f"{bogenmass} im Bogenmass entsprechen {grad} Grad.")
                valideauswahl = True
            elif menü_auswahl == "3":
                print("========== Fahrenheit in Celsius ==========")
                while True:
                    try:
                        fahrenheit = float(input("Geben sie die Anzahl Fahrenheit ein: "))
                        break
                    except ValueError:
                        print("Ungültige Eingabe. Bitte eine gültige Zahl eingeben.")
                celsius = fahrenheit_in_celsius(fahrenheit)
                os.system('cls')
                print(f"{fahrenheit} Fahrenheit entsprechen {celsius} Celsius.")
                valideauswahl = True
            elif menü_auswahl == "4":
                print("========== Celsius in Fahrenheit ==========")
                while True:
                    try:
                        celsius = float(input("Geben sie die Anzahl Grad Celsius ein: "))
                        break
                    except ValueError:
                        print("Ungültige Eingabe. Bitte eine gültige Zahl eingeben.")
                fahrenheit = celsius_in_fahrenheit(celsius)
                os.system('cls')
                print(f"{celsius} Celsius entsprechen {fahrenheit} Fahrenheit.")
                valideauswahl = True
            elif menü_auswahl == "0":
                return  # Zurück zum Hauptmenü
            else:
                os.system('cls')
                print("Keine valide Auswahl getätigt, bitte erneut versuchen!")

            time.sleep(2)

def übersetzer():
    while True:
        print("========== Übersetzer von FB ==========")
        print('''1: Deutsch -> Englisch
2: Englisch -> Deutsch
3: Deutsch -> Italienisch
4: Italienisch -> Deutsch
5: Deutsch -> Spanisch
6: Spanisch -> Deutsch
7: Deutsch -> Französisch
8: Französisch -> Deutsch
0: Zurück zum Hauptmenü
=======================================''')

        auswahl = input("Bitte wählen Sie eine Option: ")
        os.system('cls')
        if auswahl == "0":
            return  # Zurück zum Hauptmenü
        else:
            print("Diese Funktion wird bald implementiert.")  # Platzhalter für die tatsächlichen Übersetzungsfunktionen

        if auswahl != "0":
            text = input("Bitte geben Sie den zu übersetzenden Text ein: ")
            os.system('cls')
            if auswahl == "1":
                übersetzter_text = deutsch_englisch(text)
            elif auswahl == "2":
                übersetzter_text = englisch_deutsch(text)
            elif auswahl == "3":
                übersetzter_text = deutsch_italienisch(text)
            elif auswahl == "4":
                übersetzter_text = italienisch_deutsch(text)
            elif auswahl == "5":
                übersetzter_text = deutsch_spanisch(text)
            elif auswahl == "6":
                übersetzter_text = spanisch_deutsch(text)
            elif auswahl == "7":
                übersetzter_text = deutsch_franzoesisch(text)
            elif auswahl == "8":
                übersetzter_text = franzoesisch_deutsch(text)

            print(f"Übersetzter Text: {übersetzter_text}")
            time.sleep(3)

def primzahlen_menu():
    """Funktion zum Aufrufen des Primzahlen-Menüs."""
    print("===== Primzahlen-Tool von FB =====")
    while True:
        try:
            Primzahlfunktion()
            break
        except ValueError:
            print("Ungültige Eingabe. Bitte eine gültige Zahl eingeben.")
        choice = input("Drücken Sie Enter, um zum Hauptmenü zurückzukehren oder geben Sie 'exit' ein, um das Programm zu beenden: ")
        if choice.lower() == 'exit':
            sys.exit()

def fakultät_menu():
    """Funktion zum Aufrufen des Fakultät-Menüs."""
    print("===== Fakultät Rechner von FB =====")
    while True:
        eingabe = input("Geben Sie die Obergrenze für die Fakultätsberechnung ein: ")

        if is_int(eingabe):
            obergrenze = int(eingabe)
            ergebnis = fakultaet(obergrenze)  # Speichere das Ergebnis der Fakultätsberechnung
            print(f"Die Fakultät von {obergrenze} ist {ergebnis}.")  # Zeige das Ergebnis an
            break
        else:
            print("Fehler: Die Eingabe war keine gültige Zahl. Bitte versuchen Sie es erneut.")
    input("Drücken Sie Enter, um zum Hauptmenü zurückzukehren.")

def create_new_user():
    while True:
        username = input("Geben Sie den neuen Benutzernamen ein: ")
        password = getpass.getpass("Geben Sie das Passwort ein: ")
        role = input("Geben Sie die Rolle ein (admin/user): ")

        if role not in ['admin', 'user']:
            print("Ungültige Rolle. Bitte 'admin' oder 'user' eingeben.")
            continue

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Create the user
        if create_user(connection, username, hashed_password, role):
            print(f"Benutzer {username} erfolgreich erstellt.")
            break
        else:
            print(f"Fehler beim Erstellen des Benutzers {username}. Bitte versuchen Sie es erneut.")

def delete_existing_user():
    while True:
        users = get_all_users(connection)
        print("Vorhandene Benutzer:")
        for user in users:
            print(f" - {user['username']} (Rolle: {user['role']})")

        username = input("Geben Sie den Benutzernamen ein, den Sie löschen möchten: ")

        if delete_user(connection, username):
            print(f"Benutzer {username} erfolgreich gelöscht.")
            break
        else:
            print(f"Fehler beim Löschen des Benutzers {username}. Bitte versuchen Sie es erneut.")

def display_user_roles():
    users = get_all_users(connection)
    print("Benutzerrollen:")
    for user in users:
        print(f" - {user['username']} (Rolle: {user['role']})")
    input("Drücken Sie Enter, um zum Benutzerverwaltungsmenü zurückzukehren.")

def update_user_role_menu():
    while True:
        users = get_all_users(connection)
        print("Vorhandene Benutzer:")
        for user in users:
            print(f" - {user['username']} (Rolle: {user['role']})")

        username = input("Geben Sie den Benutzernamen ein, dessen Rolle Sie ändern möchten: ")
        new_role = input("Geben Sie die neue Rolle ein (admin/user): ")

        if new_role not in ['admin', 'user']:
            print("Ungültige Rolle. Bitte 'admin' oder 'user' eingeben.")
            continue

        if sql_update_user_role(connection, username, new_role):
            print(f"Rolle von {username} erfolgreich zu {new_role} geändert.")
            break
        else:
            print(f"Fehler beim Ändern der Rolle von {username}. Bitte versuchen Sie es erneut.")

def user_management():
    while True:
        print("========== Benutzerverwaltung ==========")
        print('''1: Neuen Benutzer erstellen
2: Bestehenden Benutzer löschen
3: Benutzerrollen anzeigen
4: Benutzerrolle ändern
0: Zurück zum Hauptmenü
=======================================''')

        auswahl = input("Bitte wählen Sie eine Option: ")
        os.system('cls')
        if auswahl == "1":
            create_new_user()
        elif auswahl == "2":
            delete_existing_user()
        elif auswahl == "3":
            display_user_roles()
        elif auswahl == "4":
            update_user_role_menu()
        elif auswahl == "0":
            return  # Zurück zum Hauptmenü
        else:
            print("Keine valide Auswahl getätigt, bitte erneut versuchen!")

if __name__ == "__main__":
    logged_in_user = None
    connect()  # Verbindung beim Start herstellen
    while not logged_in_user:
        print("======== Willkommen zum FB Tool, bitte loggen Sie sich ein. ========")
        logged_in_user = login()

    while True:
        print("===================")
        print("1: Umrechner")
        print("2: Übersetzer")
        print("3: Primzahlen-Tool")
        print("4: Fakultät Rechner")
        if logged_in_user['role'] == 'admin':
            print("5: Benutzerverwaltung")
        print("0: Programm beenden")
        print("===================")
        modus_auswahl = input("Wählen Sie den Modus: ")
        os.system('cls' if os.name == 'nt' else 'clear')

        if modus_auswahl == "1":
            umrechner()
        elif modus_auswahl == "2":
            übersetzer()
        elif modus_auswahl == "3":
            primzahlen_menu()
        elif modus_auswahl == "4":
            fakultät_menu()
        elif modus_auswahl == "5" and logged_in_user['role'] == 'admin':
            user_management()
        elif modus_auswahl == "0":
            print("Danke für die Nutzung des FB Tools. Auf Wiedersehen!")
            close_connection(connection)
            sys.exit()
        else:
            print("Ungültige Eingabe, bitte erneut versuchen.")