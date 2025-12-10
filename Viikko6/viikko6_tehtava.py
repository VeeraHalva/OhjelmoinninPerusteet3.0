# Copyright (c) 2025 Veera Hälvä
#

from datetime import datetime, date, timedelta

def muunna_tiedot(tietue: list) -> list:
 
    return [
        datetime.fromisoformat(tietue[0]),
        float(tietue[1].replace(",", ".")),
        float(tietue[2].replace(",", ".")),
        float(tietue[3].replace(",", ".")),
    ]


def lue_data(tiedoston_nimi: str) -> list:


    tietokanta = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)  # Otetaan kenttien esittelytiedot pois
        for tietue in f:
            tietue = tietue.split(";")
            tietokanta.append(muunna_tiedot(tietue))

    return tietokanta


def raportti_tiedstoon(raportti: str):
    """Kirjoittaa annetun sisällön tiedostoon
    parametrit:
        raportti: str: tiedostoon kirjoitettava sisältö
    """
    with open("raportti.txt", "w", encoding="utf-8") as f:
        f.write(raportti)
def raportti_aikavali(alku_pvm: date, loppu_pvm: date, tietokanta: list) -> str:
    return True    

#______________________________________________________________________________________________________________
def main():
    """
    Ohjelman pää funktio: kysyy käyttäjältä inputteja ja tulostaa/vie tiedostoon raportteja
    """
    KulutusTuotanto2025=lue_data("2025.csv")
    print(len(KulutusTuotanto2025))

    while True:
        print("Valitse raportti tyyppi:")
        print("1) päiväkohtainen yhteenveto aikaväliltä")
        print("2) kuukausikohtainen yhtenveto yhdelle kuukaudelle")
        print("3) vuoden 2025 kokonasiyhteenveto")
        print("4) lopeta ohjelma")

        ensimmäinen_valinta = int(input("Anna valinta numero 1-4:"))
        #print("valitsit ", ensimmäinen_valinta)

        if ensimmäinen_valinta == 1:
            alku_pvm = input("Anna alku päivämäärä (pv.kk.vvvv): ")
            loppu_pvm = input("Anna loppu päivämäärä (pv.kk.vvvv): ")
            #raportti_aikavali tämä tähän seuraavaksi
            print(KulutusTuotanto2025[0])  

        elif ensimmäinen_valinta == 2:
            kuukausi = int(input("Anna kuukausi numero(1-12): "))
            print(KulutusTuotanto2025[1])

        elif ensimmäinen_valinta == 3:
            print("Vuosiraportti tulostuu...")

        elif ensimmäinen_valinta == 4:
            print("Lopetetaan ohjelmaa...")
            break

        else:
            continue

        print("------------------------------------------------------------------------------------------")
    
        print("mitä haluat tehdä seuraavaksi?")
        print("1) Kirjoittaa raportin teodostoon raportti.txt")
        print("2) Luo uusi raportti")
        print("3) Lopeta")
        toinen_valinta = int(input("Anna valinta numero 1-3: "))
        if toinen_valinta == 1:
            print("Kirjoitetaan raportti tiedostoon...")
            raportti_tiedstoon(str(KulutusTuotanto2025[0][1]))
        elif toinen_valinta == 2:
            continue
        elif toinen_valinta == 3:
            print("Lopetetaan ohjelma...")
            break
        else:
            continue

        print("--------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()