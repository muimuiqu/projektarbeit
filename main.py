from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask("projektarbeit")


@app.route("/")  # Verlinkung Hauptseite
def index():
    return render_template("index.html")


@app.route("/formular/", methods=["GET", "POST"])
def formular():
    if request.method == "POST":
        data = request.form
        vorname = data["vorname"]
        nachname = data["nachname"]
        datum = data["datum"]
        event = data["event"]
        try:
            with open("aktivitaeten_2.json", "r") as open_file:
                datei_inhalt = json.load(open_file)
        except FileNotFoundError:
            datei_inhalt = []

        my_dict = {"Vorname": vorname, "Nachname": nachname, "Datum": datum, "Event": event, }
        datei_inhalt.append(my_dict)

        with open("aktivitaeten_2.json", "w") as open_file:
            json.dump(datei_inhalt, open_file, indent=4)
        return str("Besten Dank, deine Daten wurden gesichert")
    else:
        return render_template("formular.html")


@app.route("/teilnahme/", methods=['GET', 'POST'])
def teilnahme():

    event = event.aktivitaeten_2_laden()

    aktivitaeten_2 = "event"
    for key, value in event.items():
        zeile = str(key) + "event" + value + "<br>"
        aktivitaeten_2 += zeile

    return aktivitaeten_2


@app.route("/jahresprogramm/", methods=['GET', 'POST'])
def jahresprogramm():
    return render_template("jahresprogramm.html")


@app.route("/about/", methods=['GET', 'POST'])
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

"""
r für read = lesen
indent 4 zeigt die JSON Datei schöner an 
"""
