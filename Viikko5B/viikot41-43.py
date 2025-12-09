
# Copyright (c) 2025 Veera Hälvä
# License: MIT License

# Otettu ja muokattu versio kurssin esimerkkikoodista.

# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime, date


def muunna_tiedot(tietue: list) -> list:
    """
    Muuttaa jokaisen annetun tietorivin tietotyypit oikeiksi

    Parametrit:
     tietue: Sisältää 7 kenttää, joista ensimmäinen date -> loput int

    Palautus:
     Listan, jossa muutetut tietotyypit
    """
    return [
        datetime.fromisoformat(tietue[0]),
        int(tietue[1]),
        int(tietue[2]),
        int(tietue[3]),
        int(tietue[4]),
        int(tietue[5]),
        int(tietue[6]),
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
            tietue = tietue.split(";")
            tietokanta.append(muunna_tiedot(tietue))

    return tietokanta


def paivantiedot(paiva: date, tietokanta: list) -> list:
    """
    Laskee kulutus- ja tuotantotiedot vaiheittain ja palauttaa listan
    Laskettavat tiedot muutetaan Wh -> kWh

    Parametrit:
     paiva (date): Raportoitava päivä
     tietokanta (list): Kulutus- ja tuotantotiedot + päivämäärät

    Palautus:
     Listan, jossa tulostettavat merkkijonot
    """
    kulutus = [0, 0, 0]
    tuotanto = [0, 0, 0]
    for tietue in tietokanta:
        if tietue[0].date() == paiva:
            kulutus[0] += tietue[1] / 1000
            kulutus[1] += tietue[2] / 1000
            kulutus[2] += tietue[3] / 1000
            tuotanto[0] += tietue[4] / 1000
            tuotanto[1] += tietue[5] / 1000
            tuotanto[2] += tietue[6] / 1000

    return [
        f"{paiva.day}.{paiva.month}.{paiva.year}",
        f"{kulutus[0]:.2f}".replace(".", ","),
        f"{kulutus[1]:.2f}".replace(".", ","),
        f"{kulutus[2]:.2f}".replace(".", ","),
        f"{tuotanto[0]:.2f}".replace(".", ","),
        f"{tuotanto[1]:.2f}".replace(".", ","),
        f"{tuotanto[2]:.2f}".replace(".", ","),
    ]
def main():
    """
    Ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin.
    """

def main():
    """
    Ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin.
    """
    KulutusTuotantoViikko41 = lue_data("viikko41.csv")
    KulutusTuotantoViikko42 = lue_data("viikko42.csv")
    KulutusTuotantoViikko43 = lue_data("viikko43.csv")
    väli = "\t"


    #Viikko 41 raportti
    viikko41 = "\nViikon 41 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n"
    viikko41 += " \n"
    viikko41 += "Päivä\t\tPvm\t\t\t\t\t\tKulutus [kWh]\t\t\t\t\tTuotanto [kWh]\n"
    viikko41 += "\t\t\t(pv.kk.vvvv)\tv1\t\t\tv2\t\t\tv3\t\t\tv1\t\t\tv2\t\t\tv3\n"
    viikko41 += "-------------------------------------------------------------------------------------------\n"
    viikko41 += "Maanantai\t" + "\t\t".join(paivantiedot(date(2025, 10, 6), KulutusTuotantoViikko41)) + "\n"
    viikko41 += "Tiistai\t\t" + "\t\t".join(paivantiedot(date(2025, 10, 7), KulutusTuotantoViikko41)) + "\n"
    viikko41 += "Keskiviikko\t" + "\t\t".join(paivantiedot(date(2025, 10, 8), KulutusTuotantoViikko41)) + "\n"
    viikko41 += "Torstai\t\t" + "\t\t".join(paivantiedot(date(2025, 10, 9), KulutusTuotantoViikko41)) + "\n"
    viikko41 += "Perjantai\t" + "\t\t".join(paivantiedot(date(2025, 10, 10), KulutusTuotantoViikko41)) + "\n"
    viikko41 += "Lauantai\t" + "\t\t".join(paivantiedot(date(2025, 10, 11), KulutusTuotantoViikko41)) + "\n"
    viikko41 += "Sunnuntai\t" + "\t\t".join(paivantiedot(date(2025, 10, 12), KulutusTuotantoViikko41)) + "\n"
    viikko41 += "-------------------------------------------------------------------------------------------\n"
    # Viikko 42 raportti
    viikko42 = "\nViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n"
    viikko42 += " \n"
    viikko42 += "Päivä\t\tPvm\t\t\t\t\t\tKulutus [kWh]\t\t\t\t\tTuotanto [kWh]\n"
    viikko42 += "\t\t\t(pv.kk.vvvv)\tv1\t\t\tv2\t\t\tv3\t\t\tv1\t\t\tv2\t\t\tv3\n"
    viikko42 += "-------------------------------------------------------------------------------------------\n"
    viikko42 += "Maanantai\t" + "\t\t".join(paivantiedot(date(2025, 10, 13), KulutusTuotantoViikko42)) + "\n"
    viikko42 += "Tiistai\t\t" + "\t\t".join(paivantiedot(date(2025, 10, 14), KulutusTuotantoViikko42)) + "\n"
    viikko42 += "Keskiviikko\t" + "\t\t".join(paivantiedot(date(2025, 10, 15), KulutusTuotantoViikko42)) + "\n"
    viikko42 += "Torstai\t\t" + "\t\t".join(paivantiedot(date(2025, 10, 16), KulutusTuotantoViikko42)) + "\n"
    viikko42 += "Perjantai\t" + "\t\t".join(paivantiedot(date(2025, 10, 17), KulutusTuotantoViikko42)) + "\n"
    viikko42 += "Lauantai\t" + "\t\t".join(paivantiedot(date(2025, 10, 18), KulutusTuotantoViikko42)) + "\n"
    viikko42 += "Sunnuntai\t" + "\t\t".join(paivantiedot(date(2025, 10, 19), KulutusTuotantoViikko42)) + "\n"
    viikko42 += "-------------------------------------------------------------------------------------------\n"

    # Viikko 43 raportti
    viikko43 = "\nViikon 43 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n"
    viikko43 += "\n" #minkä pahuksen takkai tämä pahuksen väli ei tule tulosteeseen oikein??? Tuolta puuttu \n ylempää!!! mitä pahusta????????
    viikko43 += "Päivä\t\tPvm\t\t\t\t\t\tKulutus [kWh]\t\t\t\t\tTuotanto [kWh]\n"
    viikko43 += "\t\t\t(pv.kk.vvvv)\tv1\t\t\tv2\t\t\tv3\t\t\tv1\t\t\tv2\t\t\tv3\n"
    viikko43 += "-------------------------------------------------------------------------------------------\n"
    viikko43 += "Maanantai\t" + "\t\t".join(paivantiedot(date(2025, 10, 20), KulutusTuotantoViikko43)) + "\n"
    viikko43 += "Tiistai\t\t" + "\t\t".join(paivantiedot(date(2025, 10, 21), KulutusTuotantoViikko43)) + "\n"
    viikko43 += "Keskiviikko\t" + "\t\t".join(paivantiedot(date(2025, 10, 22), KulutusTuotantoViikko43)) + "\n"
    viikko43 += "Torstai\t\t" + "\t\t".join(paivantiedot(date(2025, 10, 23), KulutusTuotantoViikko43)) + "\n"
    viikko43 += "Perjantai\t" + "\t\t".join(paivantiedot(date(2025, 10, 24), KulutusTuotantoViikko43)) + "\n"
    viikko43 += "Lauantai\t" + "\t\t".join(paivantiedot(date(2025, 10, 25), KulutusTuotantoViikko43)) + "\n"
    viikko43 += "Sunnuntai\t" + "\t\t".join(paivantiedot(date(2025, 10, 26), KulutusTuotantoViikko43)) + "\n"
    viikko43 += "-------------------------------------------------------------------------------------------\n"

#Nämäkin vosi tehdä funktiona. katsoo jaksaako myöhemmin tai bonustehtävissä.

#kirjoitetaan jotain tiedostoon
    with open("yhteenveto.txt", "w", encoding="utf-8") as f:
        f.write(viikko41)
        f.write(viikko42)
        f.write(viikko43)   
#joku rikki!! mikä rikki??? ei s**tna!! No nyt toimii vähän turhan paljon välejä, mutta toimii
#tulosteessa Liian vähän välekä... LIIKAA välejä???? (VITUTTAA!!) en osaa/jaksa korjata!... mutta tieto tulee selkeästi esille.

print("raportti luotu")

if __name__ == "__main__":
    main()