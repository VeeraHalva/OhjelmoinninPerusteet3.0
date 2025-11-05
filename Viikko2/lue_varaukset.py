"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""

from datetime import datetime


def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    Kokonaissumma = 0.0
    maksettujen_summa = 0.0
    klo12jälkeen_summa = 0.0
    kaikki_varaukset = []

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        for rivi in f:
            varaus = rivi.strip()
            kaikki_varaukset.append(varaus.split('|'))

        # Tulostetaan varaus konsoliin
        # print(varaus.split('|'))

        # Muutetaan yksikköjä

            varausnumero = int(varaus.split('|')[0])
            print("Varausnumero:", varausnumero)

            varaaja = str(varaus.split('|')[1])
            print("Varaaja:", varaaja)

            from datetime import datetime
            Päivämäärä = datetime.strptime(varaus.split('|')[2], "%Y-%m-%d").date()
            print("Päivämäärä:", Päivämäärä)

            Aloitusaika = datetime.strptime(varaus.split('|')[3], "%H:%M").time()
            print("Aloitusaika:", Aloitusaika)

            Tuntimäärä = int(varaus.split('|')[4])
            print("Tuntimäärä:", Tuntimäärä)

            import locale
            locale.setlocale(locale.LC_ALL, 'fi_FI.UTF-8')  # Suomalainen muotoilu
            Tuntihinta = float(varaus.split('|')[5])
            print("Tuntihinta:", locale.format_string("%.2f €", Tuntihinta, grouping=True))

            Kokonaishinta = Tuntihinta * Tuntimäärä
            print("Kokonaishinta:", locale.format_string("%.2f €", Kokonaishinta, grouping=True))

            Maksettu = bool(varaus.split('|')[6] == "True")
            print(f"Maksettu: {'Kyllä' if Maksettu else 'Ei'}")

            Varauskohde = str(varaus.split('|')[7])
            print("Varauskohde:", Varauskohde)

            Puhelinnumero = str(varaus.split('|')[8])
            print("Puhelinnumero:", Puhelinnumero)

            Sähköposti = str(varaus.split('|')[9])
            print("Sähköposti:",Sähköposti)
            from datetime import datetime, timedelta
            Aloitusahetki= datetime.combine(Päivämäärä, Aloitusaika)
            Lopetusaika = Aloitusahetki + timedelta(hours=Tuntimäärä)
        
            print("Varaus alkaa:", Aloitusahetki.strftime("%d.%m.%Y %H:%M"))
            print("Varaus loppuu:", Lopetusaika.strftime("%d.%m.%Y %H:%M"))
            print("-"*40)  # Tyhjä rivi varausten väliin

            Kokonaissumma += Kokonaishinta
            maksettujen_summa += Kokonaishinta if Maksettu else 0
        print("="*40)  # Tyhjä rivi varausten väliin
#Miten tulostan yhteenvedot hinnoista?
        print("varausten yhteishinta:", locale.format_string("%.2f €", Kokonaissumma))
        print("-"*40)  # Tyhjä rivi varausten väliin
        print("maksamattomat:", locale.format_string("%.2f €", Kokonaissumma - maksettujen_summa))
        print("="*40)  # Tyhjä rivi varausten väliin ¨
        #Tulostaa klo:12 
        print("vain klo 12:00 jälkeen alkavat varaukset:")
        print("_"*40)  # Tyhjä rivi varausten väliin
        
    for osat in kaikki_varaukset:
        Aloitusaika = datetime.strptime(osat[3], "%H:%M").time()
        if Aloitusaika >= datetime.strptime("12:00", "%H:%M").time():
            Kokonaishinta = float(osat[5]) * int(osat[4])
            klo12jälkeen_summa += Kokonaishinta
            print("Varaus alkaa klo 12:00 jälkeen:")
            print("Varausnumero:", osat[0])
            print("Aloitusaika:", osat[3])
            print("Kokonaishinta:", locale.format_string("%.2f €", Kokonaishinta))
            print("jne...")
            print("-" * 40)
              

if __name__ == "__main__":
    main()