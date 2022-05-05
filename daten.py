from datetime import datetime
import json


def speichern(datei, key, value):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


def anwesenheit_speichern(aktivitaet):
    datei_name = "anwesenheit_2.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, aktivitaet)
    return zeitpunkt, aktivitaet


def aktivitaeten_laden():
    datei_name = "anwesenheit_2.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt
