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
        dauer = data["dauer"]
        try:
            with open("aktivitaeten_2.json", "r") as open_file:  # r für read = lesen
                datei_inhalt = json.load(open_file)
        except FileNotFoundError:
            datei_inhalt = []
        my_dict = {"Vorname": vorname, "Datum": datum, "Event": event, "Dauer": dauer}
        datei_inhalt.append(my_dict)
        with open("aktivitaeten_2.json", "w") as open_file:
            json.dump(datei_inhalt, open_file, indent=4)  # indent=4 sieht schöner aussieht
        return render_template("ok.html")
    else:
        return render_template("formular.html")


@app.route("/ok/", methods=["GET", "POST"])
def ok():
    return render_template("ok.html")


@app.route("/teilnahme/")  # ist die Datenausgabe
def uebersicht():
    with open("aktivitaeten_2.json") as open_file:
        json_as_string = open_file.read()
        datei_inhalt = loads(json_as_string)
    return render_template("teilnahme.html", datei_inhalt=datei_inhalt)


@app.route("/berechnung/")  # Übersicht fürs Jahr 2022 und Diagramm
def berechnung():
    with open("aktivitaeten_2.json", "r") as open_file:  # Datenbank (JSON datei) abrufen
        json_as_string = open_file.read()
        datei_inhalt = loads(json_as_string)

#  Daten filtern und zusammenrechnen
        summe_dauer_proben_stefanie = 0
        summe_dauer_auftritte_stefanie = 0
        summe_dauer_proben_rene = 0
        summe_dauer_auftritte_rene = 0

        for element in datei_inhalt:
            if element["Vorname"] == "Stefanie":
                if element["Event"] == "Probe":
                    try:
                        summe_dauer_proben_stefanie += int(element["dauer"])
                    except:
                        continue
                else:
                    try:
                        summe_dauer_auftritte_stefanie += int(element["dauer"])
                    except:
                        continue
            else:
                if element["Event"] == "Probe":
                    try:
                        summe_dauer_proben_rene += int(element["dauer"])
                    except:
                        continue
                else:
                    try:
                        summe_dauer_auftritte_rene += int(element["dauer"])
                    except:
                        continue

        return render_template("berechnung.html",
                               summe_dauer_proben_stefanie=summe_dauer_proben_stefanie,
                               summe_dauer_auftritte_stefanie=summe_dauer_auftritte_stefanie,
                               summe_dauer_proben_rene=summe_dauer_proben_rene,
                               summe_dauer_auftritte_rene=summe_dauer_auftritte_rene
                               )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
