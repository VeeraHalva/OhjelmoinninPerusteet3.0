# Copyright (c) 2025 Veera Hälvä
## License: MIT

#Alkuun otettu ohetta työpajasta. Muokattu tehtäväpohja viikko 6 tehtäviä varten.

from datetime import datetime, date, timedelta

def muunna_tiedot(tietue: list) -> list:
    """
    Muuttaa jokaisen annetun tietorivin tietotyypit oikeiksi

    Parametrit:
     tietue: Sisältää 7 kenttää, joista ensimmäinen date -> loput float

    Palautus:
     Listan, jossa muutetut tietotyypit
    """
    return [
        datetime.fromisoformat(tietue[0]),
        float(tietue[1].replace(",", ".")),
        float(tietue[2].replace(",", ".")),
        float(tietue[3].replace(",", ".")),
    ]

def lue_data(tiedoston_nimi: str) -> list:
    """
    Lukee CSV-tiedoston ja palauttaa rivit sopivassa rakenteessa ja tietotyypeissä.

    Kutsuu funktiota muunna_tiedot (lst):
     funktio palauttaa listan -> Tietotyypit muutettu

    Parametrit:
     tiedoston_nimi (str): ottaa vastaan tiedoston, jossa kentät jaettu merkillä ;

    Palautus:
     tietokanta (lst): palauttaa tietokannan, jossa tietotyypit on muutettu
    """
    tietokanta = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)  # Otetaan kenttien esittelytiedot pois
        for tietue in f:
            tietue = tietue.strip()
            if not tietue:
                continue
            tietue = tietue.split(";")
            tietokanta.append(muunna_tiedot(tietue))

    return tietokanta

def raportti_tiedostoon(raportti: str):
    """
    Kirjoittaa annetun sisällön tiedostoon

    Parametrit:
     raportti (str): raporttiteksti
    """
    with open("raportti.txt", "w", encoding="utf-8") as f:
        f.write(raportti)

def raportti_aikavali(alkupaiva: date, loppupaiva: date, tietokanta: list) -> str:
    """
    Luo yhteenvedon annetulta aikaväliltä (sama muoto kuin kuukausiraportissa).
    """
    raportti = (
        f"Raportti aikaväliltä "
        f"{alkupaiva:%d.%m.%Y} – {loppupaiva:%d.%m.%Y}\n\n"
    )

    kulutus = 0.0
    tuotanto = 0.0
    riveja = 0

    for pvm, k, t, h in tietokanta:
        paiva = pvm.date()
        if alkupaiva <= paiva <= loppupaiva:
            kulutus += k
            tuotanto += t
            riveja += 1

    if riveja == 0:
        return raportti + "Ei dataa annetulta aikaväliltä.\n"

    raportti += f"Kokonaiskulutus: {kulutus:.2f} MWh\n"
    raportti += f"Kokonaistuotanto: {tuotanto:.2f} MWh\n"
    raportti += f"Tunteja aikavälillä: {riveja}\n"

    return raportti

def raportti_kuukausi(kuukausi: int, tietokanta: list) -> str:
    """
    Luo kuukausikohtaisen yhteenvedon yhdelle kuukaudelle.
    """
    raportti = f"Kuukausiraportti {kuukausi}/2025\n\n"
    kulutus = 0.0
    tuotanto = 0.0
    paivia = 0

    for pvm, k, t, h in tietokanta:
        if pvm.year == 2025 and pvm.month == kuukausi:
            kulutus += k
            tuotanto += t
            paivia += 1

    if paivia == 0:
        return raportti + "Ei dataa tältä kuukaudelta.\n"

    raportti += f"Kokonaiskulutus: {kulutus:.2f} MWh\n"
    raportti += f"Kokonaistuotanto: {tuotanto:.2f} MWh\n"
    raportti += f"Päiviä: {paivia}\n"

    return raportti

def raportti_vuosi(tietokanta: list) -> str:
    """
    Luo vuoden 2025 kokonaisyhteenvedon.
    """
    raportti = "Vuoden 2025 raportti\n\n"

    kulutus = 0.0
    tuotanto = 0.0
    paivia = 0

    for pvm, k, t, h in tietokanta:
        if pvm.year == 2025:
            kulutus += k
            tuotanto += t
            paivia += 1

    if paivia == 0:
        return raportti + "Ei dataa vuodelta 2025.\n"

    raportti += f"Kokonaiskulutus: {kulutus:.2f} MWh\n"
    raportti += f"Kokonaistuotanto: {tuotanto:.2f} MWh\n"
    raportti += f"Päiviä: {paivia}\n"
    

    return raportti

def main():
    """
    Ohjelman pääfunktio: kysyy käyttäjältä inputteja ja tulostaa/vie tiedostoon raportteja
    """
    # Luetaan data tiedostosta
    kulutusTuotanto2025 = lue_data("2025.csv")
    raportti = ""

    while True:
        print("Valitse raporttityyppi:")
        print("1) Päiväkohtainen yhteenveto aikaväliltä")
        print("2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle")
        print("3) Vuoden 2025 kokonaisyhteenveto")
        print("4) Lopeta ohjelma")
        try:
            ensimmainen_valinta = int(input("Anna valinta (numero 1-4): "))
        except ValueError:
            print("Virheellinen syöte. Anna numero 1–4.")
            continue

        raportti = ""

        if ensimmainen_valinta == 1:
            alkupaiva_str = input("Anna alkupäivä (pv.kk.vvvv): ")
            loppupaiva_str = input("Anna loppupäivä (pv.kk.vvvv): ")
            try:
                alkupaiva = datetime.strptime(alkupaiva_str, "%d.%m.%Y").date()
                loppupaiva = datetime.strptime(loppupaiva_str, "%d.%m.%Y").date()
            except ValueError:
                print("Päivämäärä väärässä muodossa.")
                continue

            raportti = raportti_aikavali(alkupaiva, loppupaiva, kulutusTuotanto2025)
        

        elif ensimmainen_valinta == 2:
            kuukausi_str = input("Anna kuukauden numero (1–12): ")
            try:
                kuukausi = int(kuukausi_str)
                if not 1 <= kuukausi <= 12:
                    raise ValueError
            except ValueError:
                print("Virheellinen kuukauden numero.")
                continue

            raportti = raportti_kuukausi(kuukausi, kulutusTuotanto2025)
            

        elif ensimmainen_valinta == 3:
           raportti = raportti_vuosi(kulutusTuotanto2025)
           
            

        elif ensimmainen_valinta == 4:
            print("Lopetetaan ohjelma...")
            break
        else:
            print("Virheellinen valinta.")
            continue

        print("---------------------------------------------------------")
        print("Mitä haluat tehdä seuraavaksi?")
        print("1) Kirjoita raportti tiedostoon raportti.txt")
        print("2) Luo uusi raportti")
        print("3) Lopeta")
        try:
            toinen_valinta = int(input("Anna valinta (numero 1-3): "))
        except ValueError:
            print("Virheellinen syöte.")
            continue

        if toinen_valinta == 1:
            raportti_tiedostoon(raportti)
            print("Raportti tallennettu tiedostoon raportti.txt")
        elif toinen_valinta == 2:
            continue
        elif toinen_valinta == 3:
            print("Lopetetaan ohjelma...")
            break
        else:
            print("Virheellinen valinta.")
            continue

        print("---------------------------------------------------------")

if __name__ == "__main__":
    main()