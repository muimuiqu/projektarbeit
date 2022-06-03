from flask import Flask
from flask import render_template
from flask import request
import json
from json import loads


app = Flask("projektarbeit")


@app.route("/")  # Verlinkung Hauptseite
def index():
    return render_template("index.html")


@app.route("/formular/", methods=["GET", "POST"])
def formular():
    if request.method == "POST":
        data = request.form
        vorname = data["vorname"]
        datum = data["datum"]
        event = data["event"]
        try:
            with open("aktivitaeten_2.json", "r") as open_file:
                datei_inhalt = json.load(open_file)
        except FileNotFoundError:
            datei_inhalt = []

        my_dict = {"Vorname": vorname, "Datum": datum, "Event": event, }
        datei_inhalt.append(my_dict)

        with open("aktivitaeten_2.json", "w") as open_file:
            json.dump(datei_inhalt, open_file, indent=4)
        return render_template("ok.html")
    else:
        return render_template("formular.html")


@app.route("/ok/", methods=["GET", "POST"])
def ok():
    return render_template("formular.html")


@app.route("/teilnahme/")
def teilnahme():
    with open("aktivitaeten_2.json") as open_file:
        json_as_string = open_file.read()
        daten_inhalt = loads(json_as_string)
    return render_template("teilnahme.html", daten_inhalt=daten_inhalt)


@app.route("/berechnung/")
def berechnung():

    with open("aktivitaeten_2.json", "r") as open_file:
        json_as_string = open_file.read()
        daten_inhalt = loads(json_as_string)

    summe_proben = 0
    #summe_auftritte = 0

    for value in daten_inhalt:
        if value["Vorname"] == "Stefanie":
            try:
                summe_proben += summe_proben + 1
            except:
                continue

    return render_template("berechnung.html", summe_proben=summe_proben)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

"""
r für read = lesen
indent 4 zeigt die JSON Datei schöner an 
"""
