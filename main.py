from flask import Flask  # Architektur für DOM-Tree (Document Object Model)
from flask import render_template  # Ausgabe
from flask import request  # Datenübergabe für methods GET und POST
import json  # JavaScript Object Notation -- JavaScript Nutzung
from json import loads
import plotly.express as px  # visuelle Darstellung für Grafik
from plotly.offline import plot  # Funktionalität für Offline Modus
from PIL import Image  # Bilder PIL für Pillow

app = Flask("projektarbeit")


@app.route("/")
def index():
    im = Image.open("static/pictures/Titelbild_Klein.jpg")
    im.load()
    return render_template("index.html", Image=Image)


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

#  Daten zusammenrechnen
        summe_dauer_proben_stefanie = 0
        summe_dauer_auftritte_stefanie = 0
        summe_dauer_proben_philipp = 0
        summe_dauer_auftritte_philipp = 0
        summe_dauer_proben_rene = 0
        summe_dauer_auftritte_rene = 0
        summe_dauer_proben_mario = 0
        summe_dauer_auftritte_mario = 0
        summe_dauer_proben_urs = 0
        summe_dauer_auftritte_urs = 0
        summe_dauer_proben_cilli = 0
        summe_dauer_auftritte_cilli = 0

    for eintrag in datei_inhalt:  # Schlaufe in Schlaufe. Es wird als 1. auf Dictionary zugegriffen
        # danach Kategorie Event
        if eintrag["Vorname"] == "Stefanie":  # Erste Schlaufe für Dictionary
            if eintrag["Event"] == "Probe":  # Zweite Schlaufe für im Dictionary in der Kategorie Event
                try:
                    summe_dauer_proben_stefanie += float(eintrag["Dauer"])  # float wegen 1.5 Stunden
                except:
                    continue
            else:
                try:
                    summe_dauer_auftritte_stefanie += float(eintrag["Dauer"])
                except:
                    continue
        elif eintrag["Vorname"] == "Philipp":
            if eintrag["Event"] == "Probe":
                try:
                    summe_dauer_proben_philipp += float(eintrag["Dauer"])
                except:
                    continue
            else:
                try:
                    summe_dauer_auftritte_philipp += float(eintrag["Dauer"])
                except:
                    continue
        elif eintrag["Vorname"] == "Rene":
            if eintrag["Event"] == "Probe":
                try:
                    summe_dauer_proben_rene += float(eintrag["Dauer"])
                except:
                    continue
            else:
                try:
                    summe_dauer_auftritte_rene += float(eintrag["Dauer"])
                except:
                    continue
        elif eintrag["Vorname"] == "Mario":
            if eintrag["Event"] == "Probe":
                try:
                    summe_dauer_proben_mario += float(eintrag["Dauer"])
                except:
                    continue
            else:
                try:
                    summe_dauer_auftritte_mario += float(eintrag["Dauer"])
                except:
                    continue
        elif eintrag["Vorname"] == "Urs":
            if eintrag["Event"] == "Probe":
                try:
                    summe_dauer_proben_urs += float(eintrag["Dauer"])
                except:
                    continue
            else:
                try:
                    summe_dauer_auftritte_urs += float(eintrag["Dauer"])
                except:
                    continue
        elif eintrag["Vorname"] == "Cilli":
            if eintrag["Event"] == "Probe":
                try:
                    summe_dauer_proben_cilli += float(eintrag["Dauer"])
                except:
                    continue
            else:
                try:
                    summe_dauer_auftritte_cilli += float(eintrag["Dauer"])
                except:
                    continue

    diagramm_proben = px.bar(
        x=["Stefanie", "Philipp", "Rene", "Mario", "Urs", "Cilli"],
        y=[summe_dauer_proben_stefanie, summe_dauer_proben_philipp, summe_dauer_proben_rene,
           summe_dauer_proben_mario, summe_dauer_proben_urs, summe_dauer_proben_cilli],
        labels={"x": "Mitglieder", "y": "Anzahl Proben"}  # Beschriftung der Grafik
    )

    div_diagramm_proben = plot(diagramm_proben, output_type="div")

    diagramm_auftritte = px.bar(  # bar für das Balkendiagramm
        x=["Stefanie", "Philipp", "Rene", "Mario", "Urs", "Cilli"],
        y=[summe_dauer_auftritte_stefanie, summe_dauer_auftritte_philipp, summe_dauer_auftritte_rene,
           summe_dauer_auftritte_mario, summe_dauer_auftritte_urs, summe_dauer_auftritte_cilli],
        labels={"x": "Mitglieder", "y": "Anzahl Auftritte"}
    )

    div_diagramm_auftritte = plot(diagramm_auftritte, output_type="div")

    return render_template("berechnung.html",
                           summe_dauer_proben_stefanie=summe_dauer_proben_stefanie,
                           summe_dauer_auftritte_stefanie=summe_dauer_auftritte_stefanie,
                           summe_dauer_proben_philipp=summe_dauer_proben_philipp,
                           summe_dauer_auftritte_philipp=summe_dauer_auftritte_philipp,
                           summe_dauer_proben_rene=summe_dauer_proben_rene,
                           summe_dauer_auftritte_rene=summe_dauer_auftritte_rene,
                           summe_dauer_proben_mario=summe_dauer_proben_mario,
                           summe_dauer_auftritte_mario=summe_dauer_auftritte_mario,
                           summe_dauer_proben_urs=summe_dauer_proben_urs,
                           summe_dauer_auftritte_urs=summe_dauer_auftritte_urs,
                           summe_dauer_proben_cilli=summe_dauer_proben_cilli,
                           summe_dauer_auftritte_cilli=summe_dauer_auftritte_cilli,
                           diagramm_proben=div_diagramm_proben,
                           diagramm_auftritte=div_diagramm_auftritte
                           )


if __name__ == "__main__":  # wird zwingend für die Webapplikation benötigt
    app.run(debug=True, port=5000)
