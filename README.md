Problembeschreibung/Motivation
Seit der 5. Klasse bin ich Mitglied in einem Verein. Das Anwesenheitsprotokoll wird bei uns noch von Hand gemacht und
ich bin der Meinung, dass die Erfassung der Proben- und Auftrittsbesuche einfacher und schneller erfolgen kann.
In diesem Projekt wurde die Anwesenheitserfassung von 6 Mitglieder realisiert.

Betrieb
Welche zusätzliche Pakete müssen bei Bedarf installiert werden. (Muss im Normalfall nicht beachtet werden. Python muss nicht erwähnt werden, da das bei einem Python Projekt impliziert ist.)
Was muss man bei der Ausführung beachten. Was muss eventuell davor noch gemacht werden.
Welch Datei muss ausgeführt werden
Json: import und load (Erstellung und Zugriff der Datenbank)
PIL: Pillow damit das Titelbild eingesetzt werden kann

Benutzung
Wie wird das Projekt benutzt
Welche Optionen oder auch Spezialitäten existieren
Die Idee dahinter ist, dass jedes Mitglied die Erfassung selbstständig nachtragen kann.
Bei der Übersicht-Seite 2022 ist auf einem Blick erkenntlich, welches Mitglied die häufigsten Events besucht hat.
Auf diese Art und Weise spart man sich die Zeit, dass jemand aus dem Verein die Mitglieder zählt und per Excel Daten die Events auswerten muss.
Zusätzlich bekommt man mit einer schönen visuellen Darstellung eine angenehme Sicht.

Architektur
Home-Seite: Begrüssung der Mitglieder
Erfassung Anwesenheit-Seite: Proben und Auftritte eintragen
Teilnahme-Seite: Auflistung der besuchten Events, hier kann jedes Mitglied auf seine eigenen erfassten Daten zugreifen
Anwesenheit 2022-Seite: Diagramm Übersicht über die Proben und Auftritte aller Mitglieder
Hier bei Bedarf eine kurze Beschreibung des Ablaufs des Programms auf Code Ebene z.B. als Ablaufdiagramm.

Ungelöste/unbearbeitete Probleme
Die HTML.Berechnung wäre sicher einfacher zu lösen als die einzelne Auflistung der Mitglieder.
Der Download des Titelbilds funktioniert nicht. Die Annahme liegt dabei, dass mehr Packages installiert werden müssen,
als nur PIL.

