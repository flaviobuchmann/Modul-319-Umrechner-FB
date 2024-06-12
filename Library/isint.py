def ist_int(eingabe):
    try:
        # Versuche, die Eingabe in einen Integer umzuwandeln
        int(eingabe)
        return True  # Wenn die Umwandlung erfolgreich ist, ist die Eingabe ein Integer
    except ValueError:
        # Wenn die Umwandlung fehlschlägt, wird eine ValueError-Ausnahme ausgelöst
        return False