# skUnify via csv-Import/Export

Hey,

skUnify ist mein erstes kleines Projekt, das ich in Python3 schreibe und mir meinen Arbeitsalltag erleichtern soll. Es geht um die Pflege eines Online-Shops, 
bei dem mittlerweile über 600 Produkte aktiviert sind und stetig wächst. Jedes Produkt erhält beim Anlegen eine von uns überlegte, für das 
Produkt spezifische und nummerierte Stock Keeping Unit (SKU). Dabei erkennt man auf einen Blick, um welche Art Produkt es sich handelt und wieviele der 
selben Art schon im Umlauf sind. Das System funktioniert gut. Allerdings sind über die letzten Monate etliche neue Produkte dazugekommen, und die SKU-Vergabe 
gestaltet sich zunehmend schwieriger, so dass ich mir nun ein Programm wünsche, bei dem diese Vergabe automatisch passiert.

Hier nur einige Beispiele:

- 196s-0214 (FORTLAUFENDE SONGNUMMER + s für "Song" + FORTLAUFENDE ARTIKELNUMMER)
- 196pb-0215 (FORTLAUFENDE SONGNUMMER + pb für "Playback" + FORTLAUFENDE ARTIKELNUMMER)
- cd2-0023 (cd + FORTLAUFENDE CD-ANZAHL + cd + FORTLAUFENDE ARTIKELNUMMER) usw.
- cd2digi-0026 (CD-Inhalt als digitalen Download)
- rhy11-0588 (Rhythmical - Noten und Video)
- lug3-0029 (Heft mit CD - vom Lugert-Verlag)

Weitere Produkte sind
- eigene Bücher
- Tonies-Auftragsarbeiten
- eigene Tonies
- interaktive Lerninhalte (Videos+)
- Materialpakete (Unterrichtsmaterial)
- Bücher vom Coppenrath-Verlag
- Hörspiele
- Songpakete
- kreative Liedersammlungen
- Klanggeschichten
- Noten
- kostenlose Texte
- Poster

skUnify kann bereits: 
- einen csv-Export lesen 
- kategorisieren 
- über eine User-Abfrage ein neues Produkt anlegen 
- eine individuelle SKU vergeben
- eine individuelle Kurzbeschreibung hinzufügen
- neu Angelegtes mit rotem Fähnchen ("NEU!!!") versehen
- den Preis festlegen (teilweise fest vergeben, Manches über User-Abfrage möglich)
- für den Verkauf aktivieren, bzw. deaktivieren °°°
- individuelle Produkt-Beschreibung in HTML
- individueller SEO-Titel
- individuelle SEO-Beschreibung
- alle vorhandenen und neu angelegten Produkte für einen Import in einer neuen csv-Datei schreiben

°°° alle neu angelegten Produkte bleiben zu Anfang erstmal deaktiviert, da noch Produktbeschreibungen, Audiovorschauen, SEO-Titel und -Beschreibung, Fotos und Thumbnails hinzugefügt werden müssen, bevor die im Shop zu sehen sind. Die Funktion ließ sich aber schnell umsetzen, daher habe ich die Funktion für "den einen besonderen Fall" mal mit reingepackt.

Der csv-Import der neuen Datei im Online-Shop funktioniert. So habe ich zu Testzwecken den Import gewagt und erfolgreich 4 neue Produkte angelegt.
Riesiger Motivationsschub....
Dabei soll es aber nicht bleiben. Im folgenden schreibe ich mir hier eine Checkliste für weitere Funktionen, die sicherlich hilfreich wären. Auch
im Hinblick darauf, dass irgendwann auch ein:e Arbeitskollege:in ein neues Produkt anlegen könnte, ohne das SKU-System verstehen zu müssen.

skUnifys Nice-To-Haves (sortiert von hoffentlich leicht nach "Ich-hab-keine-Ahnung-wie-das-gehen-soll"):
- Code teilweise in Funktionen und neue py-Datei auslagern (angefangen - Optimierungsbedarf)
- 7% und 19% Umsatzsteuer
- Suchfunktion (nach Produktnamen, SKUs, Kategorien, Kurzbeschreibungen, etc.)
- Zugriff oder Einblick auf / Suche nach schon angelegte und reservierte Produkte
    - csv-Datei (reservierte Produkte read & write?)
    - Neuvergabe von reservierten Produkten
- von Listen zu Dictionaries ?
- in jedem Moment der User-Abfrage einen Abbruch erlauben
- den User per Abfrage um csv-Import bitten -> REST api ??
- eine Rückgängig-Funktion
- Image und Thumbnail-Upload

Ein paar Abschließende Sätze:
Ich bin Neuling in der Welt des Programmierens, daher bitte ich um Verzeihung für jegliche Fehlerchen und No-Gos, die sich in den Untiefen des Scripts verbergen. 
Ich bin seit ein paar Monaten dabei und absolut motiviert. Das Projekt ist eine ordentliche Herausvorderung, aber ich glaube, ich kann dabei Einiges lernen. 
In der Hoffnung, dass sich skUnify als echtes Tool in meinem Büro-Alltag durchsetzt.

Danke fürs Zuhören!
Hendrik

edit:
Ich bin gerade dabei das Projekt auf einen json-Down- und Upload via Rest-Api umzuschreiben. Glücklicherweise kann ich den schwierigsten Teil mit der SKU-Vergabe fast komplett übernehmen. Die Umsatzsteuer-Angaben und eine Suchfunktion sind durch die Arbeit mit json um ein Vielfaches einfacher. Listen und Dictionaries und der csv-Import und Export ist dadurch hinfällig geworden. Durch den automatischen Down- und Upload der json habe ich noch mehr zeitersparnis.
<!---
hms-challenger/hms-challenger is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

