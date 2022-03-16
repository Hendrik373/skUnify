

def logo():
    print("\n>>> Willkommen bei: <<<\n")
    print("                                                     ")
    print("              _     _   _         _   __             ")
    print("             | |   | | | |       (_) / _|            ")
    print("         ___ | | __| | | | _ __   _ | |_  _   _      ")
    print("        / __|| |/ /| | | || '_ \ | ||  _|| | | |     ")
    print("        \__ \|   < | |_| || | | || || |  | |_| |     ")
    print("        |___/|_|\_\ \___/ |_| |_||_||_|   \__, |     ")
    print("                                           __/ |     ")
    print("                            © minimusiker |___/     \n")

def new_price_function():
    while True:
        price_abfrage = input("Wieviel kostet das Produkt in €? ")
        try:
            price = float(price_abfrage)
            break
        except:
            print("Das ist keine Zahl! z.B. 14.99")
            continue
    return price

new_description = None # für produkte individualisieren
new_category2 = None
new_category3 = None
new_image = None
new_ribbon = "NEU!!!"
new_ribbon_colour = "#7091DA"
new_weight = None
new_price = None
new_recommended_price = None
new_quantiy = None
new_enabled = "no"
new_taxClassCode = "default"
new_shipping_freight = 0.00
new_fixed_shipping_rate_only = "no"
new_shippingType = "GLOBAL_METHODS"
new_shippingMethodMarkup = 0.00
new_shippingFlatRate = 0.00
new_shippingDisabledMethods = None
new_shippingEnabledMethods = None
new_upc = None
new_brand = None
new_seo_title = None # für produkte individualisieren
new_seo_description = None # für produkte individualisieren
new_product_url = None
new_product_id = None