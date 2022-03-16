
def song_description():
    song_des = """<p>Beschreibungstext</p>
        <ul>
            <li><em>Tonart: </em></li>
            <li><em>Stimmumfang: </em></li>
            <li><em>Level: </em></li>
            <li><em>Geeignet für: </em></li>
        </ul>
        <h5>Hörprobe</h5>
        <p>
            <audio controls="" preload="metadata" rel="width:100%;" style="width: 100%;">
            <source src="https://www.hoerthin.de/audiovorschau/...mp3" type="audio/mpeg">
            </audio>
        </p>
        <h5>Stichworte</h5><p></p>"""
    return song_des

def playback_description():
    pb_des = """<p>Beschreibungstext</p>
        <ul>
            <li><em>Tonart: </em></li>
            <li><em>Stimmumfang: </em></li>
            <li><em>Level: </em></li>
            <li><em>Geeignet für: </em></li>
        </ul>
        <h5>Stichworte</h5><p></p>"""
    return pb_des

def cd_description():
    cd_des = """<p>Beschreibungstext</p>
        <h5>Hörprobe</h5>
        <p>
            <audio controls="" preload="metadata" style=" width:100%;" rel=" width:100%;"><br>
            <source src="http://www.hoerthin.de/audiovorschau/....mp3" type="audio/mpeg"></audio>
            </p>
        <h5>Liederliste</h5>
        <p>...</p>"""
    return cd_des

def book_description():
    book_des = """<p>Beschreibungstext</p>
        <h5>Umfang</h5>
        <p>z.B. Heft (71 Seiten) inkl. CD</p>
        <h5>Lieder in diesem Heft</h5>
        <ul>
            <li>...</li>
        </ul>
        <h5>Hörprobe</h5>
        <p>
            <audio controls="" preload="metadata" rel="width:100%;" style="width: 100%;">
            <source src="https://www.hoerthin.de/audiovorschau/...mp3" type="audio/mpeg">
            </audio>
        </p>"""
    return book_des

def cop_description():
    cop_des = """<p>Beschreibungstext</p>
        <h5>Musikpädagogen empfehlen dieses Buch, denn es fördert</h5>
        <ul>
            <li>...</li>
        </ul>
        <h6>STICHWORTE</h6>
        <p>Coppenrath, Spiegelburg, Mini Musiker, U3, Kinderbuch, Liederbuch, Musik für die Kleinsten</p>"""
    return cop_des

def kl_description():
    kl_des = """<p>
        Kleiner Tipp: Lade sie z. B. auf einen <strong>Kreativ-Tonie</strong> für deine Toniebox. 
        So hast du neue <strong>Musik fürs Kinderzimmer</strong> parat!
        </p>
        <ol>
            <li>Ich lieb den Frühling</li>
            <li>Hey kleiner Osterhase</li>
            <li>Immer wieder kommt ein neuer Frühling</li>
            <li>Die Vogelhochzeit</li>
            <li>Un poquito cantas</li>
        </ol>"""
    return kl_des

def mat_description():
    mat_des = """<p>Beschreibungstext</p>
        <h5>Themen im Unterrichtmaterial</h5>
        <ul>
            <li>...</li>
        </ul>
        <h5>Arbeitsblätter und mehr downloaden</h5>
        <ul>
            <li>Materialpaket (Gesamtumfang: ??? Seiten)</li>
            <li>Karteikarten mit Kurzinfos zu beiden Songs</li>
            <li>Coronabedingte Umsetzungsalternativen</li>
            <li>Noten+ und Songtexte </li>
            <li>Mitspielsätze für ...</li>
            <li>Song & Playback zu "..."</li>
            <li>Song & Playback zu "..."</li>
        </ul>"""
    return mat_des

def rhy_description():
    rhy_des = """<h3>Thema ...</h3>
        <p>Beschreibungstext</p>
        <p>
            <iframe width="500" height="281" src="YOUTUBELINK" frameborder="0" allowfullscreen="">
            </iframe>
        </p>
        <h5>Stichworte</h5>
        <p>...</p>"""
    return rhy_des

def vid_description():
    vid_des = """<h5>Lernvideo: THEMA</h5>
        <p>Beschreibungstext</p>
        <p>Das Material wurde für Grundschüler*innen konzipiert und eignet sich für den <strong>Distanzunterricht</strong> oder als <strong>Hausaufgabe</strong>. 
        Die interaktive pdf-Datei lässt sich auf allen gängigen Endgeräten (Laptop, Smartphone, Tablet etc.), mit einem pdf-Reader (z.B. Acrobat Reader) öffnen.</p>
        <p>Du erhältst</p>
        <ul>
            <li><strong>Lernvideo</strong> - Thema: Die Gitarre (1:30 min)</li>
            <li><strong>interaktive PDF-Datei mit Quiz</strong></li>
        </ul>
        <h6>STICHWORTE</h6>
        <p>Grundschule, Unterrichtsmaterial, Lernvideo, interaktive PDF, Quiz, Material, Arbeitsblatt, Instrumentenkunde</p>"""
    return vid_des