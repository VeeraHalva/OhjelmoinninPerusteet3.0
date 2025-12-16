# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime

# Muuntaa varauksen tiedot oikeisiin tietotyyppeihin
def muunna_varaustiedot(varaus: list) -> dict:
    return {
        "id": int(varaus[0]),
        "nimi": varaus[1],
        "sahkoposti": varaus[2],
        "puhelin": varaus[3],
        "paiva": datetime.strptime(varaus[4], "%Y-%m-%d").date(),
        "kellonaika": datetime.strptime(varaus[5], "%H:%M").time(),
        "kesto": int(varaus[6]),
        "hinta": float(varaus[7]),
        "vahvistettu": varaus[8].lower() == "true",
        "kohde": varaus[9],
        "luotu": datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S"),
        
    }
# Lukee varaukset tiedostosta ja palauttaa listan sanakirjoja
def hae_varaukset(varaustiedosto: str) -> list[dict]:
    varaukset = []
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for rivi in f:
            rivi = rivi.strip()
            osat = rivi.split('|')
            varaukset.append(muunna_varaustiedot(osat))
    return varaukset

#luotu Hakemaan asiakasnumero, joka määräytyy rivin perusteella. Ei siis voida määrittää onko sama henkilö tehnyt varauksen, numero aina eri.
def hae_varaukset(varaustiedosto: str) -> list[dict]:
    varaukset = []
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for index, rivi in enumerate(f, start=1):
            rivi = rivi.strip()
            osat = rivi.split('|')
            varaus = muunna_varaustiedot(osat)

            # Lisää asiakasnumero automaattisesti
            varaus["asiakasnumero"] = index

            varaukset.append(varaus)
    return varaukset

# Tulostaa vahvistetut varaukset
def vahvistetut_varaukset(varaukset: list[dict]):
    for varaus in varaukset:
        if varaus["vahvistettu"]:
            print(f"- {varaus['nimi']}, {varaus['kohde']}, "
                  f"{varaus['paiva'].strftime('%d.%m.%Y')} klo {varaus['kellonaika'].strftime('%H.%M')}, asiakasnumero {varaus['asiakasnumero']}")
    print()
# Tulostaa pitkät varaukset (kesto ≥ 3 tuntia)
def pitkat_varaukset(varaukset: list[dict]):
    for varaus in varaukset:
        if varaus["kesto"] >= 3:
            print(f"- {varaus['nimi']}, {varaus['paiva'].strftime('%d.%m.%Y')} klo {varaus['kellonaika'].strftime('%H.%M')}, "
                  f"kesto {varaus['kesto']} h, {varaus['kohde']}, asiakasnumero {varaus['asiakasnumero']}")
    print()
# Tulostaa varausten vahvistusstatus
def varausten_vahvistusstatus(varaukset: list[dict]):
    for varaus in varaukset:
        if varaus["vahvistettu"]:
            print(f"{varaus['nimi']} → Vahvistettu")
        else:
            print(f"{varaus['nimi']} → EI vahvistettu")
    print()
# Tulostaa vahvistettujen ja ei-vahvistettujen varausten lukumäärän
def varausten_lkm(varaukset: list[dict]):
    vahvistetut = sum(1 for v in varaukset if v["vahvistettu"])
    ei_vahvistetut = len(varaukset) - vahvistetut

    print(f"- Vahvistettuja varauksia: {vahvistetut} kpl")
    print(f"- Ei-vahvistettuja varauksia: {ei_vahvistetut} kpl")
    print()
# Laskee ja tulostaa vahvistettujen varausten kokonaistulot
def varausten_kokonaistulot(varaukset: list[dict]):
    tulot = sum(v["kesto"] * v["hinta"] for v in varaukset if v["vahvistettu"])

    print("Vahvistettujen varausten kokonaistulot:",
          f"{tulot:.2f}".replace('.', ','), "€")
    print()
# Pääohjelma
def main():
    varaukset = hae_varaukset("varaukset.txt")

    print("1) Vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)

    print("2) Pitkät varaukset (≥ 3 h)")
    pitkat_varaukset(varaukset)

    print("3) Varausten vahvistusstatus")
    varausten_vahvistusstatus(varaukset)

    print("4) Yhteenveto vahvistuksista")
    varausten_lkm(varaukset)

    print("5) Vahvistettujen varausten kokonaistulot")
    varausten_kokonaistulot(varaukset)

if __name__ == "__main__":
    main()