# Copyright (c) 2025 Veera Hälvä
## License: MIT

#Alkuun otettu ohetta työpajasta. Muokattu tehtäväpohja viikko 6 tehtäviä varten.

from datetime import datetime, date
from typing import List

def muunna_tiedot(tietue: List[str]) -> List:
    """Muuntaa CSV-rivin oikeisiin tietotyyppeihin."""
    return [
        datetime.fromisoformat(tietue[0]),
        float(tietue[1].replace(",", ".")),
        float(tietue[2].replace(",", ".")),
        float(tietue[3].replace(",", ".")),
    ]

def lue_data(tiedoston_nimi: str) -> List[list]:
    """Lukee CSV-tiedoston ja palauttaa tietokannan listana."""
    tietokanta = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)
        for rivi in f:
            rivi = rivi.strip()
            if not rivi:
                continue
            tietokanta.append(muunna_tiedot(rivi.split(";")))
    return tietokanta

def fmt(arvo: float) -> str:
    """Muotoilee desimaaliluvun pilkulla ja kahdella desimaalilla."""
    return f"{arvo:.2f}".replace(".", ",")

def nayta_paavalikko() -> str:
    """Näyttää päävalikon ja palauttaa käyttäjän valinnan."""
    print("Valitse raporttityyppi:")
    print("1) Päiväkohtainen yhteenveto aikaväliltä")
    print("2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle")
    print("3) Vuoden 2025 kokonaisyhteenveto")
    print("4) Lopeta ohjelma")
    return input("Anna valinta (1–4): ").strip()

def raportti_aikavali(alku: date, loppu: date, data: list) -> List[str]:
    """Muodostaa päiväkohtaisen yhteenvedon aikaväliltä."""
    rivit = [
        f"Raportti aikaväliltä {alku:%d.%m.%Y} – {loppu:%d.%m.%Y}",
        ""
    ]

    kulutus = 0.0
    tuotanto = 0.0
    lampotilat = []
    tunnit = 0

    for pvm, k, t, h in data:
        if alku <= pvm.date() <= loppu:
            kulutus += k
            tuotanto += t
            lampotilat.append(h)
            tunnit += 1

    if tunnit == 0:
        rivit.append("Ei dataa annetulta aikaväliltä.")
        return rivit

    keski = sum(lampotilat) / len(lampotilat)

    rivit.append(f"Kokonaiskulutus: {fmt(kulutus)} kWh")
    rivit.append(f"Kokonaistuotanto: {fmt(tuotanto)} kWh")
    rivit.append(f"Keskilämpötila: {fmt(keski)} °C")
    rivit.append(f"Tunteja aikavälillä: {tunnit}")

    return rivit

def raportti_kuukausi(kuukausi: int, data: list) -> List[str]:
    """Muodostaa kuukausikohtaisen yhteenvedon."""
    rivit = [f"Kuukausiraportti {kuukausi:02d}/2025", ""]

    kulutus = 0.0
    tuotanto = 0.0
    lampotilat = []
    tunnit = 0

    for pvm, k, t, h in data:
        if pvm.year == 2025 and pvm.month == kuukausi:
            kulutus += k
            tuotanto += t
            lampotilat.append(h)
            tunnit += 1

    if tunnit == 0:
        rivit.append("Ei dataa tältä kuukaudelta.")
        return rivit

    keski = sum(lampotilat) / len(lampotilat)

    rivit.append(f"Kokonaiskulutus: {fmt(kulutus)} kWh")
    rivit.append(f"Kokonaistuotanto: {fmt(tuotanto)} kWh")
    rivit.append(f"Keskilämpötila: {fmt(keski)} °C")
    rivit.append(f"Tunteja kuukaudessa: {tunnit}")

    return rivit

def raportti_vuosi(data: list) -> List[str]:
    """Muodostaa vuoden 2025 yhteenvedon."""
    rivit = ["Vuoden 2025 raportti", ""]

    kulutus = 0.0
    tuotanto = 0.0
    lampotilat = []
    tunnit = 0

    for pvm, k, t, h in data:
        if pvm.year == 2025:
            kulutus += k
            tuotanto += t
            lampotilat.append(h)
            tunnit += 1

    if tunnit == 0:
        rivit.append("Ei dataa vuodelta 2025.")
        return rivit

    keski = sum(lampotilat) / len(lampotilat)

    rivit.append(f"Kokonaiskulutus: {fmt(kulutus)} kWh")
    rivit.append(f"Kokonaistuotanto: {fmt(tuotanto)} kWh")
    rivit.append(f"Keskilämpötila: {fmt(keski)} °C")
    rivit.append(f"Tunteja vuodessa: {tunnit}")

    return rivit

def tulosta_raportti_konsoliin(rivit: List[str]) -> None:
    """Tulostaa raportin konsoliin."""
    print("\n".join(rivit))

def kirjoita_raportti_tiedostoon(rivit: List[str]) -> None:
    """Kirjoittaa raportin tiedostoon raportti.txt."""
    with open("raportti.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(rivit))

def main() -> None:
    """Ohjelman pääfunktio."""
    data = lue_data("2025.csv")

    while True:
        valinta = nayta_paavalikko()

        if valinta == "1":
            alku = input("Anna alkupäivä (pv.kk.vvvv): ")
            loppu = input("Anna loppupäivä (pv.kk.vvvv): ")
            try:
                alku_pvm = datetime.strptime(alku, "%d.%m.%Y").date()
                loppu_pvm = datetime.strptime(loppu, "%d.%m.%Y").date()
            except ValueError:
                print("Päivämäärä väärässä muodossa.")
                continue
            raportti = raportti_aikavali(alku_pvm, loppu_pvm, data)

        elif valinta == "2":
            kk = input("Anna kuukauden numero (1–12): ")
            if not kk.isdigit() or not 1 <= int(kk) <= 12:
                print("Virheellinen kuukauden numero.")
                continue
            raportti = raportti_kuukausi(int(kk), data)

        elif valinta == "3":
            raportti = raportti_vuosi(data)

        elif valinta == "4":
            print("Lopetetaan ohjelma...")
            break

        else:
            print("Virheellinen valinta.")
            continue

        tulosta_raportti_konsoliin(raportti)

        print("\nMitä haluat tehdä seuraavaksi?")
        print("1) Kirjoita raportti tiedostoon raportti.txt")
        print("2) Luo uusi raportti")
        print("3) Lopeta")

        jatko = input("Anna valinta (1–3): ").strip()

        if jatko == "1":
            kirjoita_raportti_tiedostoon(raportti)
            print("Raportti tallennettu.")
        elif jatko == "2":
            continue
        elif jatko == "3":
            print("Lopetetaan ohjelma...")
            break
        else:
            print("Virheellinen valinta.")

if __name__ == "__main__":
    main()