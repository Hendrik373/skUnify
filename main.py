import csv
import json
from functions_constants import *
from descriptions import *

products = {}

with open('products_2022-03-14_18-13.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=";")

    header = next(reader) # skips the first element/first row

    for row in reader:
        column = {
            header[0]: row[0],
            header[1]: row[1],
            header[2]: row[2],
            header[3]: row[3],
            header[4]: row[4],
            header[5]: row[5],
            header[6]: row[6],
            header[7]: row[7],
            header[8]: row[8],
            header[9]: row[9],
            header[10]: row[10],
            header[11]: row[11],
            header[12]: row[12],
            header[13]: row[13],
            header[14]: row[14],
            header[15]: row[15],
            header[16]: row[16],
            header[17]: row[17],
            header[18]: row[18],
            header[19]: row[19],
            header[20]: row[20],
            header[21]: row[21],
            header[22]: row[22],
            header[23]: row[23],
            header[24]: row[24],
            header[25]: row[25],
            header[26]: row[26],
            header[27]: row[27],
            header[28]: row[28]
        }
        name = f"{row[0]} {row[1]}" # adds first row as name[0], everything else as name[1]
        products[name] = column

json.dumps(products, indent=4, ensure_ascii=False)

with open("products_new.csv", "w", encoding="utf-8", newline="") as productfile:
    writer = csv.writer(productfile, delimiter=";")
    writer.writerow(header)

    names = []
    subtitles = []
    categories = []
    categories_2 = []
    my_lugert_books = []
    my_mini_books = []
    my_coppenrath_books = []
    my_poster = []
    my_hörgeschichten = []
    my_cds = []
    my_digitals = []
    my_tonies = []
    my_fanarticles = []
    my_klanggeschichten = []
    my_liedersammlungen = []
    my_materialpakete = []
    my_songpakete = []
    my_nachbestellungen = []
    my_noten = []
    my_playbacks = []
    my_rhythmicals = []
    my_songs = []
    my_texte = []
    my_fuer_viertis = []
    my_videos = []

    counter = []
    rows = []

    for column in products.values():
        row = []
        row.append(column[header[0]]) # name
        row.append(column[header[1]]) # sku
        row.append(column[header[2]]) # subtitle
        row.append(column[header[3]]) # description
        row.append(column[header[4]]) # category1
        row.append(column[header[5]]) # category2
        row.append(column[header[6]]) # category3
        row.append(column[header[7]]) # image
        row.append(column[header[8]]) # ribbon
        row.append(column[header[9]]) # ribboncolour
        row.append(column[header[10]]) # weight
        row.append(column[header[11]]) # price
        row.append(column[header[12]]) # recommended_price
        row.append(column[header[13]]) # quantity
        row.append(column[header[14]]) # enabled
        row.append(column[header[15]]) # taxClassCode
        row.append(column[header[16]]) # shipping_freight
        row.append(column[header[17]]) # fixed_shipping_rate_only
        row.append(column[header[18]]) # shippingType
        row.append(column[header[19]]) # shippingMethodMarkup
        row.append(column[header[20]]) # shippingFlatRate
        row.append(column[header[21]]) # shippingDisabledMethods
        row.append(column[header[22]]) # shippingEnabledMethods
        row.append(column[header[23]]) # upc
        row.append(column[header[24]]) # brand
        row.append(column[header[25]]) # seo_title
        row.append(column[header[26]]) # seo_description
        row.append(column[header[27]]) # product_url
        row.append(column[header[28]]) # product_id
        rows.append(row)

        set_counter = column.get('sku').split('-')[-1] # set up global counter 
        try:
            set_counter = int(set_counter)
            counter.append(set_counter)
            counter.sort()
        except:
            print("Einige SKUs konnten nicht zugeordnet werden:")
        elements = column.get('name') # search for product names
        if elements not in names: 
            names.append(elements)
        sku_elements = column.get('sku').split('-')[0] # get skus

        if "lug" in sku_elements:
            my_lugert_books.append(sku_elements)
            my_lugert_books.sort()
        if "b0" in sku_elements:
            my_mini_books.append(sku_elements)
            if sku_elements.startswith("hb"):
                my_mini_books.remove(sku_elements)
            my_mini_books.sort()
        if "cop" in sku_elements:
            my_coppenrath_books.append(sku_elements)
            my_coppenrath_books.sort()         
        if "p" in sku_elements:
            my_pos_ints = []
            my_poster.append(sku_elements)
            if sku_elements.startswith("cop"):
                my_poster.remove(sku_elements)
            elif sku_elements.startswith("mp"):
                my_poster.remove(sku_elements)
            elif sku_elements.startswith("sp"):
                my_poster.remove(sku_elements)
            if "pb" in sku_elements:
                my_poster.remove(sku_elements)
            for pos_ints in my_poster:
                try:
                    pos_ints = int(pos_ints[-1])
                    my_pos_ints.append(pos_ints)
                except:
                    print("Keine Zahl vorhanden")
            my_poster.sort()
            my_pos_ints.sort()
        if "cd" in sku_elements:
            my_cds.append(sku_elements)
            my_cds.sort()
            if "digi" in sku_elements:
                my_cds.remove(sku_elements)
        if "digi" in sku_elements:
            my_digitals.append(sku_elements)
            my_digitals.sort()
        if "ton" in sku_elements:
            my_tonies.append(sku_elements)
            my_tonies.sort()
        if "kg" in sku_elements:
            my_klanggeschichten.append(sku_elements)
            my_klanggeschichten.sort()
        if "kl" in sku_elements:
            my_kl_ints = []
            my_liedersammlungen.append(sku_elements)
            for kl_ints in my_liedersammlungen:
                try:
                    kl_ints = int(kl_ints[2:])
                    my_kl_ints.append(kl_ints)
                    my_kl_ints.sort()
                except:
                    print("Keine Zahl vorhanden")
            my_liedersammlungen.sort()
        if "mp" in sku_elements:
            my_mp_ints = []
            my_materialpakete.append(sku_elements)
            for mp_ints in my_materialpakete:
                try:
                    mp_ints = int(mp_ints[2:])
                    my_mp_ints.append(mp_ints)
                    my_mp_ints.sort()
                except:
                    print("Keine Zahl vorhanden")
            my_materialpakete.sort()
        if "sp" in sku_elements:
            my_songpakete.append(sku_elements)
            my_songpakete.sort()
        if "vid" in sku_elements:
            my_videos.append(sku_elements)
            my_videos.sort()
        if "rhy" in sku_elements:
            my_rhythmicals.append(sku_elements)
            my_rhythmicals.sort()
        if "s" in sku_elements:
            my_song_ints = []
            my_songs.append(sku_elements)
            if "sp" in sku_elements:
                my_songs.remove(sku_elements)
            my_songs.sort()
            for song_ints in my_songs:
                try:
                    song_ints = int(song_ints[0:3])
                    my_song_ints.append(song_ints)
                except:
                    pass
                            
        elements = column.get('subtitle') # search for subtitles to categorize
        if elements not in subtitles: 
            subtitles.append(elements)
            subtitles.sort()

        cat_elements = column.get('category1').split(' / ')[-1] # search for categories to show
        if cat_elements not in categories: 
            categories.append(cat_elements)
            categories.sort()

    writer.writerows(rows)
    
    global_counter = int(counter[-1]) # product counter
    song_counter = int(my_song_ints[-1]) + 1
    cop_counter = int(len(my_coppenrath_books))
    poster_counter = int(len(my_poster))
    mini_counter = int(len(my_mini_books))
    lugert_counter = int(len(my_lugert_books))
    klanggeschichten_counter = int(len(my_klanggeschichten))
    liedersammlung_counter = int(my_kl_ints[-1])
    songpakete_counter = int(len(my_songpakete))
    materialpakete_counter = int(my_mp_ints[-1])
    rhythmical_counter = int(len(my_rhythmicals))
    video_counter = int(len(my_videos))
    cd_counter = int(len(my_cds))
    tonie_counter = int(len(my_tonies))

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n>>> Willkommen bei:\n")
    logo()

    while True: # main loop
        new_product = input("Neues Produkt hinzufügen? (j/n) ")
        if new_product == "j" or new_product == "J":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n>>> NEUES PRODUKT ANLEGEN <<<\n")
            global_counter += 1
            
            print("Neuer Datensatz:", global_counter, "wurde angelegt!")

            while True:
                new_product_name = input("Produktname: ")
                if new_product_name not in names:
                    names.append(new_product_name)
                    break
                else: 
                    print("Produkt schon vorhanden!")   
                    continue
            
            while True:
                print("\n>>> PRODUKTKATEGORIE WÄHLEN <<<\n")
                cat_counter = 1
                for cat1 in categories:
                    print(cat_counter, cat1)
                    cat_counter += 1
                print("\n")

                set_category = input("Produktkategorie: ")

                if set_category == "1": # leer
                    new_sku = "LEER"
                    continue
                elif set_category == "2": # lugert und sing mit den minimusikern
                    while True:
                        new_book = input("Neues Buch? (mini/lug) ")
                        if new_book == "mini":
                            mini_counter += 1
                            new_sku = "b" + str(mini_counter).zfill(2) + "-" + str(global_counter).zfill(4)
                            new_subtitle = "Buch"
                            new_category1 = "Material für deinen Musikunterricht / Bücher"
                            new_price = new_price_function()
                            new_description = book_description()
                            new_seo_title = "📗 Buch: " + new_product_name + " | minimusiker.de"
                            print(">>>  Neues Minimusiker-Buch:", new_product_name, new_sku, "hinzugefügt!  <<<")
                            break
                        elif new_book == "lug":
                            lugert_counter += 1
                            new_sku = "lug" + str(lugert_counter) + "-" + str(global_counter).zfill(4)
                            new_subtitle = "Heft"
                            new_category1 = "Material für deinen Musikunterricht / Bücher"
                            new_description = book_description()
                            new_seo_title = new_product_name + " | THEMA | minimusiker.de"
                            print(">>>  Neues Lugert-Buch:", new_product_name, new_sku, "hinzugefügt!   <<<")
                            while True:
                                new_price_abfrage = input("Wieviel kostet das Produkt in €? ")
                                try:
                                    new_price = float(new_price_abfrage)
                                    break
                                except:
                                    print("Das ist keine Zahl! z.B. 14.99")
                                    continue
                            break
                        else:
                            continue
                    break
                elif set_category == "3": # bücher + co
                    while True:
                        new_book = input("Neues Coppenrath-Buch? Neues Poster? (cop/p) ")
                        if new_book == "cop":
                            cop_counter += 1
                            new_sku = "cop" + str(cop_counter) + "-" + str(global_counter).zfill(4)
                            new_subtitle = "Buch"
                            new_category1 = "Musik für Zuhause / Bücher + Co"
                            new_price = new_price_function()
                            new_description = cop_description()
                            new_seo_title = new_product_name + " |📖 Buch | minimusiker.de"
                            print(">>>  Neues Coppenrath-Buch:", new_product_name, new_sku, "hinzugefügt! <<<")
                            break
                        elif new_book == "p":
                            poster_counter += 1
                            new_sku = "p" + str(poster_counter) + "-" + str(global_counter).zfill(4)
                            new_subtitle = "Poster"
                            new_category1 = "Musik für Zuhause / für Viertis"
                            new_category2 = "Musik für Zuhause / Bücher + Co"
                            new_category3 = "Material für deinen Musikunterricht / Klassenposter"
                            new_seo_title = new_product_name + " |📃 Poster | minimusiker.de"
                            print(">>>  Neues Poster:", new_product_name, new_sku, "hinzugefügt!  <<<")
                            while True:
                                new_price_abfrage = input("Wieviel kostet das Produkt in €? ")
                                try:
                                    new_price = float(new_price_abfrage)
                                    break
                                except:
                                    print("Das ist keine Zahl! z.B. 14.99")
                                    continue
                            break
                        else:
                            continue
                    break
                elif set_category == "4": # cds + tonies
                    while True:
                        new_tonträger = input("Neue CD, digitals oder Tonie? (cd/digi/ton) ")
                        if new_tonträger == "cd":
                            cd_counter += 1
                            new_cd_sku = "cd" + str(cd_counter) + "-" + str(global_counter).zfill(4)
                            cd_subtitle = "CD"
                            new_cd_category1 = "Musik für Zuhause / für Viertis"
                            new_cd_category2 = "Musik für Zuhause / CDs + Tonies"
                            new_cd_price = new_price_function()
                            new_cd_description = cd_description()
                            print(">>>  Neue CD:", new_product_name, new_cd_sku, "hinzugefügt!  <<<")
                            new_digi = input("Willst du die CD als digitalen Download anbieten? j/n ")
                            global_counter += 1
                            new_digi_sku = "cd" + str(cd_counter) + "digi" + "-" + str(global_counter).zfill(4)
                            digi_subtitle = "digi"
                            new_digi_category1 = "Musik für Zuhause / für Viertis"
                            new_digi_category2 = "Musik für Zuhause / CDs + Tonies"
                            new_cd_seo_title = new_product_name + " |💿 Kinderlieder | minimusiker.de"
                            new_digi_seo_title = new_product_name + " digital |📀 Kinderlieder | minimusiker.de"
                            while True:
                                if new_digi == "j" or new_digi == "J":
                                    new_digi_price = new_price_function()
                                    print(">>>  Neues digitals Produkt:", new_product_name, new_digi_sku, "hinzugefügt! <<<")
                                    break
                                elif new_digi == "n" or new_digi == "N":
                                    print("!!!  Digitale CD-SKU: " + new_digi_sku + "wurde reserviert   !!!")
                                    break
                                else:
                                    continue
                            break
                        elif new_tonträger == "digi":
                            while True:
                                cd_counter += 1
                                new_cd_sku = "cd" + str(cd_counter) + "-" + str(global_counter).zfill(4)
                                cd_subtitle = "CD"
                                new_cd_category1 = "Musik für Zuhause / für Viertis"
                                new_cd_category2 = "Musik für Zuhause / CDs + Tonies"
                                global_counter += 1
                                new_digi_sku = "cd" + str(cd_counter) + "digi" + "-" + str(global_counter).zfill(4)
                                digi_subtitle = "digi"
                                new_digi_category1 = "Musik für Zuhause / für Viertis"
                                new_digi_category2 = "Musik für Zuhause / CDs + Tonies"
                                new_cd_description = cd_description()
                                new_cd = input("Willst du zuerst eine neue CD hinzufügen? j/n ")
                                new_cd_seo_title = new_product_name + " |💿 Kinderlieder | minimusiker.de"
                                new_digi_seo_title = new_product_name + " digital |📀 Kinderlieder | minimusiker.de"
                                if new_cd == "j" or new_cd == "J":
                                    new_cd_price = new_price_function()
                                    print(">>>  Neue CD:", new_product_name, new_cd_sku, "hinzugefügt!  <<<")
                                    print("Lege einen Preis für den mp3-Download fest!")
                                    new_digi_price = new_price_function()
                                    print(">>>  Neues digitales Produkt:", new_product_name, new_digi_sku, "hinzugefügt!    <<<")
                                    break
                                elif new_cd == "n" or new_cd == "N":
                                    print("!!!  CD-SKU: " + new_cd_sku + " wurde reserviert !!!")
                                    print("Lege einen Preis für den mp3-Download fest!")
                                    new_digi_price = new_price_function()
                                    print(">>>  Neues digitales Produkt:", new_product_name, new_digi_sku, "hinzugefügt!    <<<")
                                    break
                                else:
                                    continue
                            break
                        elif new_tonträger == "ton":
                            tonie_counter += 1
                            new_sku = "ton" + str(tonie_counter) + "-" + str(global_counter).zfill(4)
                            new_subtitle = "Tonie"
                            new_category1 = "Musik für Zuhause / für Viertis"
                            new_category2 = "Musik für Zuhause / CDs + Tonies"
                            new_price = 14.99
                            new_description = cd_description()
                            new_seo_title = new_product_name + " - Tonie | Kinderlieder | minimusiker.de"
                            print(">>>  Neuer Tonie:", new_product_name, new_sku, "hinzugefügt! <<<")
                            break
                        else:
                            continue
                    break
                elif set_category == "5": # fanartikel
                    continue
                elif set_category == "6": # klanggeschichten
                    klanggeschichten_counter += 1
                    new_sku = "kg" + str(klanggeschichten_counter) + "-" + str(global_counter).zfill(4)
                    new_subtitle = "Klanggeschichte"
                    new_category1 = "Material für deinen Musikunterricht / Klanggeschichten"
                    new_price = new_price_function()
                    print(">>>  Neues Klanggeschichte:", new_product_name, new_sku, "hinzugefügt!   <<<")
                    break
                elif set_category == "7": # liedersammlungen
                    liedersammlung_counter += 1
                    new_sku = "kl" + str(liedersammlung_counter) + "-" + str(global_counter).zfill(4)
                    new_subtitle = "kreative Liedersammlung"
                    new_category1 = "Musik für Zuhause / Liedersammlungen"
                    new_price = 3.0
                    new_description = kl_description()
                    new_seo_title = "Liedersammlung #" + str(liedersammlung_counter) + " |🎶 Kinderlieder | minimusiker.de"
                    print(">>>  Neue Liedersammlung:", new_product_name, new_sku, "hinzugefügt! <<<")
                    break
                elif set_category == "8": # materialpakete
                    materialpakete_counter += 1
                    new_sku = "mp" + str(materialpakete_counter) + "-" + str(global_counter).zfill(4)
                    new_subtitle = "Materialpakete"
                    new_category1 = "Material für deinen Musikunterricht / Materialpakete"
                    new_price = 13.0
                    new_description = mat_description()
                    new_seo_title = "Unterrichtsmaterial #" + str(materialpakete_counter) + " |📚 Grundschule | minimusiker.de"
                    print(">>>  Neues Materialpaket: #"+ str(materialpakete_counter), new_product_name, new_sku, "hinzugefügt!   <<<")
                    break
                elif set_category == "9": # minimusiker-songpakete
                    songpakete_counter += 1
                    new_sku = "sp" + str(songpakete_counter) + "-" + str(global_counter).zfill(4)
                    new_subtitle = "Minimusiker-Songpaket"
                    new_category1 = "Material für deinen Musikunterricht / Minimusiker-Songpakete"
                    new_price = 7.0
                    new_description = song_description()
                    new_seo_title = new_product_name + " |🧺 Songpaket | minimusiker.de"
                    print(">>>  Neue Liedersammlung:", new_product_name, new_sku, "hinzugefügt! <<<")
                    break
                elif set_category == "10": # nachbestellung
                    continue
                elif set_category == "11" or set_category == "12" or set_category == "15"  or set_category == "16" or set_category == "14": # song hinzufügen
                    new_song_description = song_description()
                    if set_category == "14":
                        global_counter += 1
                        new_song_sku = str(song_counter) + "s-" + str(global_counter).zfill(4)
                        new_subtitle = "Song"
                        new_song_category1 = "Material für deinen Musikunterricht / Songs"
                        new_song_category2 = "Musik für Zuhause / Songs"
                        new_song_price = 1.0
                        new_song_description = song_description()
                        new_song_seo_title = new_product_name + " | 🎵 Kinderlied | minimusiker.de"
                        print(">>>  Neuer Song:", new_product_name, new_song_sku, "hinzugefügt!  <<<")
                    if set_category == "11" or set_category == "12" or set_category == "15"  or set_category == "16": # bei noten, playback, text und songtext
                        while True: # song hinzufügen
                            new_song = input("Willst du zuerst einen neuen Song hinzufügen? j/n ")
                            global_counter += 1
                            new_song_sku = str(song_counter) + "s-" + str(global_counter).zfill(4)
                            new_subtitle = "Song"
                            new_song_category1 = "Material für deinen Musikunterricht / Songs"
                            new_song_category2 = "Musik für Zuhause / Songs"
                            new_song_price = 1.0
                            new_song_description = song_description()
                            new_song_seo_title = new_product_name + " | 🎵 Kinderlied | minimusiker.de"
                            if new_song == "j" or new_song == "J":
                                print(">>>  Neuer Song:", new_product_name, new_song_sku, "hinzugefügt! <<<")
                                break
                            elif new_song == "n" or new_song == "N":
                                print("!!!  Song-SKU: " + new_song_sku + "wurde reserviert  !!!")
                                break
                            else:
                                continue
                    while True: # playback hinzufügen
                        new_playback = input("Playback hinzufügen? j/n ")
                        global_counter += 1
                        new_playback_sku = str(song_counter) + "pb-" + str(global_counter).zfill(4)
                        playback_subtitle = "Playback"
                        new_playback_category1 = "Material für deinen Musikunterricht / Playbacks"
                        new_playback_category2 = "Musik für Zuhause / Playbacks"
                        new_playback_price = 4.0
                        new_playback_description = playback_description()
                        new_playback_seo_title = new_product_name + " | 🎤 Playback | minimusiker.de"
                        if new_playback == "j" or new_playback == "J":
                            print(">>>  Neues Playback:", new_product_name, new_playback_sku, "hinzugefügt! <<<")
                            break
                        elif new_playback == "n" or new_playback == "N":
                            print("!!!  Playback-SKU: " + new_playback_sku + "wurde reserviert  !!!")
                            break
                        else:
                            continue
                    while True: # noten hinzufügen
                        new_noten = input("Noten hinzufügen? j/n ")
                        global_counter += 1
                        new_noten_sku = str(song_counter) + "n-" + str(global_counter).zfill(4)
                        noten_subtitle = "Noten"
                        new_noten_category1 = "Material für deinen Musikunterricht / Noten+"
                        new_noten_category2 = None
                        new_noten_price = 2.0
                        new_song_description = song_description()
                        new_noten_seo_title = new_product_name + " | 🎼 Noten | minimusiker.de"
                        if new_noten == "j" or new_noten == "J":
                            print(">>>  Neue Noten:", new_product_name, new_noten_sku, "hinzugefügt!    <<<")
                            break
                        elif new_noten == "n" or new_noten == "N":
                            print("!!!  Noten-SKU: " + new_noten_sku + "wurde reserviert    !!!")
                            break
                        else:
                            continue
                    while True: # text hinzufügen
                        new_text = input("Text hinzufügen? j/n ")
                        global_counter += 1
                        new_text_sku = str(song_counter) + "t-" + str(global_counter).zfill(4)
                        text_subtitle = "Text"
                        new_text_category1 = "Material für deinen Musikunterricht / Texte"
                        new_text_category2 = "Musik für Zuhause / Songtexte"
                        new_text_price = 0.0
                        new_song_description = song_description()
                        new_text_seo_title = new_product_name + " | 📝 Text | minimusiker.de"
                        if new_text == "j" or new_text == "J":
                            print(">>>  Neuer Text:", new_product_name, new_text_sku, "hinzugefügt! <<<")
                            break
                        elif new_text == "n" or new_text == "N":
                            print("!!!  Text-SKU: " + new_text_sku + "wurde reserviert  !!!")
                            break
                        else:
                            continue
                    song_counter += 1
                    break
                elif set_category == "13": # rhythmicals
                    rhythmical_counter += 1
                    new_sku = "rhy" + str(rhythmical_counter) + "-" + str(global_counter).zfill(4)
                    new_subtitle = "Rhythmical"
                    new_category1 = "Material für deinen Musikunterricht / Rhythmicals"
                    new_price = 0.0
                    new_description = rhy_description()
                    new_seo_title = "Rhythmical | " + new_product_name + " | minimusiker.de"
                    print(">>>  Neues Rhythmical:", new_product_name, new_sku, "hinzugefügt!  <<<")
                    break
                elif set_category == "17": # für vierties
                    continue
                elif set_category == "18": # interaktive Lerninhalte
                    video_counter += 1
                    new_product_name = "Lernvideo: " + new_product_name
                    new_sku = "vid" + str(video_counter) + "-" + str(global_counter).zfill(4)
                    new_subtitle = "Video"
                    new_category1 = "Material für deinen Musikunterricht / Noten+"
                    new_category2 = None
                    new_price = new_price_function()
                    new_description = vid_description()
                    new_seo_title = new_product_name + " |🎥 Lernvideo | minimusiker.de"
                    print(">>>  Neues Produkt:", new_product_name, new_sku, "hinzugefügt! <<<")
                    break
                else:
                    continue

            def full_line_any():
                full_line = [new_product_name, new_sku, new_subtitle, new_description, new_category1, new_category2, new_category3, new_image, 
                new_ribbon, new_ribbon_colour, new_weight, new_price, new_recommended_price, new_quantiy, new_enabled, new_taxClassCode, new_shipping_freight, new_fixed_shipping_rate_only, 
                new_shippingType, new_shippingMethodMarkup, new_shippingFlatRate, new_shippingDisabledMethods, new_shippingEnabledMethods, new_upc, new_brand, new_seo_title, new_seo_description, 
                new_product_url, new_product_id]
                writer.writerow(full_line)

            def full_line_cd():
                full_line = [new_product_name, new_cd_sku, cd_subtitle, new_cd_description, new_cd_category1, new_cd_category2, new_cd_category3, new_image, 
                new_ribbon, new_ribbon_colour, new_weight, new_cd_price, new_recommended_price, new_quantiy, new_enabled, new_taxClassCode, new_shipping_freight, new_fixed_shipping_rate_only, 
                new_shippingType, new_shippingMethodMarkup, new_shippingFlatRate, new_shippingDisabledMethods, new_shippingEnabledMethods, new_upc, new_brand, new_cd_seo_title, new_seo_description, 
                new_product_url, new_product_id]
                writer.writerow(full_line)
            
            def full_line_digi():
                full_line = [new_product_name, new_digi_sku, digi_subtitle, new_cd_description, new_cd_category1, new_cd_category2, new_cd_category3, new_image, 
                new_ribbon, new_ribbon_colour, new_weight, new_digi_price, new_recommended_price, new_quantiy, new_enabled, new_taxClassCode, new_shipping_freight, new_fixed_shipping_rate_only, 
                new_shippingType, new_shippingMethodMarkup, new_shippingFlatRate, new_shippingDisabledMethods, new_shippingEnabledMethods, new_upc, new_brand, new_digi_seo_title, new_seo_description, 
                new_product_url, new_product_id]
                writer.writerow(full_line)

            if set_category == "11" or set_category == "12" or set_category == "14" or set_category == "15" or set_category == "16": # write rows for new product
                full_line = [new_product_name, new_song_sku, new_subtitle, new_song_description, new_song_category1, new_song_category2, new_category3, new_image, 
                new_ribbon, new_ribbon_colour, new_weight, new_song_price, new_recommended_price, new_quantiy, new_enabled, new_taxClassCode, new_shipping_freight, new_fixed_shipping_rate_only, 
                new_shippingType, new_shippingMethodMarkup, new_shippingFlatRate, new_shippingDisabledMethods, new_shippingEnabledMethods, new_upc, new_brand, new_song_seo_title, new_seo_description, 
                new_product_url, new_product_id]
                writer.writerow(full_line)
                if new_playback == "j" or new_playback == "J":
                    full_line = [new_product_name, new_playback_sku, playback_subtitle, new_playback_description, new_playback_category1, new_playback_category2, new_category3, new_image, 
                    new_ribbon, new_ribbon_colour, new_weight, new_playback_price, new_recommended_price, new_quantiy, new_enabled, new_taxClassCode, new_shipping_freight, new_fixed_shipping_rate_only, 
                    new_shippingType, new_shippingMethodMarkup, new_shippingFlatRate, new_shippingDisabledMethods, new_shippingEnabledMethods, new_upc, new_brand, new_playback_seo_title, new_seo_description, 
                    new_product_url, new_product_id]
                    writer.writerow(full_line)
                if new_noten == "j" or new_noten == "J":
                    full_line = [new_product_name, new_noten_sku, noten_subtitle, new_song_description, new_noten_category1, new_noten_category1, new_category3, new_image, 
                    new_ribbon, new_ribbon_colour, new_weight, new_noten_price, new_recommended_price, new_quantiy, new_enabled, new_taxClassCode, new_shipping_freight, new_fixed_shipping_rate_only, 
                    new_shippingType, new_shippingMethodMarkup, new_shippingFlatRate, new_shippingDisabledMethods, new_shippingEnabledMethods, new_upc, new_brand, new_noten_seo_title, new_seo_description, 
                    new_product_url, new_product_id]
                    writer.writerow(full_line)
                if new_text == "j" or new_text == "J":
                    full_line = [new_product_name, new_text_sku, text_subtitle, new_song_description, new_text_category1, new_text_category2, new_category3, new_image, 
                    new_ribbon, new_ribbon_colour, new_weight, new_text_price, new_recommended_price, new_quantiy, new_enabled, new_taxClassCode, new_shipping_freight, new_fixed_shipping_rate_only, 
                    new_shippingType, new_shippingMethodMarkup, new_shippingFlatRate, new_shippingDisabledMethods, new_shippingEnabledMethods, new_upc, new_brand, new_text_seo_title, new_seo_description, 
                    new_product_url, new_product_id]
                    writer.writerow(full_line)
            elif set_category == "4":
                if new_tonträger == "cd": # das hier muss neu gemacht werden
                    full_line_cd()
                    if new_digi == "j" or new_digi == "J":
                        full_line_digi()   
                elif new_tonträger == "digi":
                    if new_cd == "j" or new_cd == "J":
                        full_line_cd()
                    full_line_digi()
                    continue
                elif new_tonträger == "ton":
                    full_line_any()
                    continue
            else:
                full_line_any()
                continue
        elif new_product == "n" or new_product == "N":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n>>> Bis bald!\n")
            logo()
            break
        else:
            continue

csvfile.close()
productfile.close()