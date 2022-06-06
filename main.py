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


@app.route("/teilnahme/")  # Teilnahme
def berechnung():
    with open("aktivitaeten_2.json", "r") as open_file:
        json_as_string = open_file.read()
        datei_inhalt = loads(json_as_string)

    summe_proben_stefanie = 0
    summe_auftritte_stefanie = 0
    summe_proben_philipp = 0
    summe_auftritte_philipp = 0
    summe_proben_rene = 0
    summe_auftritte_rene = 0
    summe_proben_mario = 0
    summe_auftritte_mario = 0
    summe_proben_urs = 0
    summe_auftritte_urs = 0
    summe_proben_cilli = 0
    summe_auftritte_cilli = 0

    for eintrag in datei_inhalt:  # Eintrag Proben
        if eintrag["Vorname"] == "Stefanie":
            try:
                summe_proben_stefanie = summe_proben_stefanie + 1
            except:
                continue

    for eintrag in datei_inhalt:  # Eintrag Auftritte
        if eintrag["Vorname"] == "Stefanie":
            try:
                summe_auftritte_stefanie = summe_auftritte_stefanie + 1
            except:
                continue

    return render_template("teilnahme.html",
                           datei_inhalt=datei_inhalt,
                           summe_proben_stefanie=summe_proben_stefanie,
                           summe_auftritte_stefanie=summe_auftritte_stefanie,
                           )


@app.route("/berechnung/")  # Jahr 2022
def uebersicht():
    with open("aktivitaeten_2.json") as open_file:
        json_as_string = open_file.read()
        datei_inhalt = loads(json_as_string)
    return render_template("/berechnung.html", datei_inhalt=datei_inhalt)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
