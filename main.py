from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask("projektarbeit")


@app.route("/formular/", methods=["GET", "POST"])
def formular():
    if request.method == "POST":

        data = request.form
        vorname = data["vorname"]
        nachname = data["nachname"]
        datum = data["datum"]
        anwesenheit_auftritte = data["anwesenheit_auftritte"]
        anwesenheit_proben = data["anwesenheit_probe"]
        try:
            with open("aktivitaeten_2.json", "r") as open_file:
                datei_inhalt = json.load(open_file)
        except FileNotFoundError:
            datei_inhalt = []

        my_dict = {"Vorname": vorname, "Nachname": nachname, "Datum": datum, "Auftritte": anwesenheit_auftritte, "Probe": anwesenheit_proben}
        datei_inhalt.append(my_dict)

        with open("aktivitaeten_2.json", "w") as open_file:
            json.dump(datei_inhalt, open_file, indent=4)
        return str("Besten Dank, deine Daten wurden gesichert")
    else:
        return render_template("formular.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

"""
r für read = lesen
indent 4 zeigt die JSON Datei schöner an 
"""
