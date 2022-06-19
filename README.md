# 🎷Erfassung der Anwesenheit für Vereine🎺
Das Anwesenheitsprotokoll wird in vielen Vereinen noch von Hand geschrieben.
In diesem Projekt beschränkt sich die Erfassung von Proben und Auftritten von insgesamt 6 Mitgliedern.

## Inhalt
- Betrieb: zusätzliche Packages
- Benutzung der Webapplikation
- Architektur
- Ungelöste Probleme

## Betrieb
Folgende Pakete wurden zusätzlich für dieses Projekt geladen

- Flask - vorgegebene Architektur, welche für Python geschrieben ist (DOM-Tree)
- JSON - für die Erstellung Zugriff für die Datenbank
- Plotly - stellt Grafiken zur Verfügung
- PIL - für Pillow, damit Bilder eingesetzt werden können
- Bootstrap - fürs User Interface (schöne und responsive Darstellung)
- Dillinger - Saubere Darstellung Readme

## Benutzung
Die Erfassung erfolgt von jedem Mitglied selbstständig. Auf diese Art und Weise wird Zeit gespart und die Daten werden
ausgewertet. Bei der Erfassung kann das Mitglied zwischen den Kategorien Probe und Auftritt auswählen

## Architektur
![Flussdiagramm](static/flowchart/Flussdiagramm%20PRO%202.jpg)

### Übersicht Webapplikation
| Name Webpage | Funktion |
| ------------ | -------  |
| Home | Begrüssung der Mitglieder |
| Erfassung Anwesenheit | Eintragung Aufwand der Kategorien in Stunden |
| Teilnahme | Auflistung der besuchten Events von allen Mitgliedern |
| Jahr 2022 | Zusammenfassung aller Stunden der Mitglieder |
|| visuelle Darstellung des Aufwandes in einer Grafik / Diagramm|

## Ungelöste Probleme
Die Berechnung wäre sicher einfacher zu lösen als, jedes einzelne Mitglied aufzulisten. Für eine Erfassung von über
100 und mehr ist der Aufwand zu hoch mit der Berechnung in diesem Projekt.
Der Download des Titelbildes funktioniert nicht richtig. Die Annahme liegt dabei, dass noch ein
anderes Packages installiert werden muss.
