Problembeschreibung/Motivation
Seit der 5. Klasse bin ich Mitglied in einem Verein. Das Anwesenheitsprotokoll wird bei uns noch von Hand gemacht und
ich bin der Meinung, dass die Erfassung der Proben- und Auftrittsbesuche einfacher und schneller erfolgen kann.
In diesem Projekt wurde die Anwesenheitserfassung von 6 Mitglieder realisiert.

Betrieb
Json: import und load (Erstellung und Zugriff der Datenbank)
PIL: Pillow damit das Titelbild eingesetzt werden kann
Plotly: für die grafische Darstellung
Flask: vorgegebene Architektur DOM Tree
Request: Einsatz von Formular
Bootstrap: für die schöne/responsive Darstellung --> CSS

Benutzung
Wie wird das Projekt benutzt
Welche Optionen oder auch Spezialitäten existieren
Die Idee dahinter ist, dass jedes Mitglied die Erfassung selbstständig nachtragen kann.
Auf diese Art und Weise spart man sich die Zeit, dass jemand aus dem Verein die Anwesenheit der Mitglieder zählt und
per Excel die Daten auswerten muss.
Bei der Teilnahme selbst kann das Mitglied zwischen der Kategorie Auftritt und Probe auswählen.
Mit einer Übersicht, auf welchem erkenntlich ist, welches Mitglied die häufigsten Events besucht hat, erleichtert die
Auswertung.

Architektur
Home-Seite: Begrüssung der Mitglieder
Erfassung Anwesenheit-Seite: Eintragung des Stundenaufwands in den Kategorien Proben und Auftritte
Teilnahme-Seite: Auflistung der besuchten Events von allen Mitgliedern
Jahr 2022-Seite: Zusammenfassung Stunden aller Mitglieder. Diagramm Übersicht über die Proben und Auftritte
aller Mitglieder. Mit einer Schlaufe 


Ungelöste/unbearbeitete Probleme
Die HTML.Berechnung wäre sicher einfacher zu lösen als die einzelne Auflistung der Mitglieder.
Der Download des Titelbilds funktioniert nicht. Die Annahme liegt dabei, dass mehr Packages installiert werden müssen,
als nur PIL.

