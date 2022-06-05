from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask("projektarbeit")


@app.route("/")
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
            with open("aktivitaeten.json", "r") as open_file:
                datei_inhalt = json.load(open_file)
        except FileNotFoundError:
            datei_inhalt = []

        my_dict = {"Vorname": vorname, "Datum": datum, "Event": event}
        datei_inhalt.append(my_dict)

        with open("aktivitaeten.json", "w") as open_file:
            json.dump(datei_inhalt, open_file, indent=4)
            return render_template("ok.html")

    else:
        return render_template("formular.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
