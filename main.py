from flask import Flask
from flask import render_template
from flask import request
import json
from json import loads


app = Flask("projektarbeit")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/formular/", methods=['GET', 'POST'])  # Verlinkung Formular
def formular():
    if request.method == 'POST':
        data = request.form
        vorname = data["vorname"]
        datum = data["datum"]
        event = data["event"]
        try:
            with open("aktivitaeten_2.json", "r") as open_file:  # r für read = lesen
                datei_inhalt = json.load(open_file)
        except FileNotFoundError:
            datei_inhalt = []
        my_dict = {"Vorname": vorname, "Datum": datum, "Event": event}
        datei_inhalt.append(my_dict)
        with open("aktivitaeten_2.json", "w") as open_file:
            json.dump(datei_inhalt, open_file, indent=4)  # indent=4 sieht schöner aussieht
        return render_template("ok.html")
    else:
        return render_template("formular.html")


@app.route("/ok/", methods=["GET", "POST"])
def ok():
    return render_template("ok.html")


@app.route("/teilnahme/", methods=["GET", "POST"])  # ist die Berechnung
def berechnung():
    with open("aktivitaeten_2.json", "r") as open_file:  # Datenbank (JSON datei) abrufen
        json_as_string = open_file.read()
        datei_inhalt = loads(json_as_string)

#  Definition Event-Aufteilung und Summen Mitglieder
    if request.method.lower() == "post":
        event_proben = request.form['Probe']
        event_auftritte = request.form['Auftritte']

#  Daten filtern und zusammenrechnen
        datei_filtern = datei_inhalt.eingabe_laden()
        gefilterte_elemente = []
        summe_proben_stefanie = 0
        summe_auftritte_stefanie = 0
        for liste_elemente in datei_filtern:
            if liste_elemente['Stefanie'] == event_proben and liste_elemente['Event: Probe'].split('-')[2] == event_auftritte:
                gefilterte_elemente.append(liste_elemente)
                summe_proben_stefanie = liste_elemente["Probe"]
                summe_auftritte_stefanie = liste_elemente["Auftritte"]
        return render_template("teilnahme.html", liste_elemente=gefilterte_elemente, summe_proben_stefanie=summe_proben_stefanie, summe_auftritte_stefanie=summe_auftritte_stefanie, Probe=event_proben, Auftritte=event_auftritte,)
    return render_template("teilnahme.html")


@app.route("/berechnung/")  # Übersicht fürs Jahr 2022 und Diagramm
def uebersicht():
    with open("aktivitaeten_2.json") as open_file:
        json_as_string = open_file.read()
        datei_inhalt = loads(json_as_string)
    return render_template("/berechnung.html", datei_inhalt=datei_inhalt)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
