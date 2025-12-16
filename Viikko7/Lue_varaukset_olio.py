# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime

class Varaus:
    def __init__(self, varaus_id: int, nimi:str, sahkoposti:str, puhelin:str,
                 paiva:datetime.date, kellonaika:datetime.time, kesto:int, hinta:float,
                 vahvistettu:bool, kohde:str, luotu:datetime, asiakasnumero:int):
        self.varaus_id = varaus_id
        self.nimi = nimi
        self.sahkoposti = sahkoposti
        self.puhelin = puhelin
        self.paiva = paiva
        self.kellonaika = kellonaika
        self.kesto = kesto
        self.hinta = hinta
        self.vahvistettu = vahvistettu
        self.kohde = kohde
        self.luotu = luotu
        self.asiakasnumero = asiakasnumero

    # Hyödyllisiä metodeja
    def is_confirmed(self):
        return self.vahvistettu

    def is_long(self):
        return self.kesto >= 3

    def total_price(self):
        return self.kesto * self.hinta
            

def muunna_varaustiedot(varaus: list, asiakasnumero: int) -> Varaus:
    return Varaus(
        varaus_id=int(varaus[0]),
        nimi=varaus[1],
        sahkoposti=varaus[2],
        puhelin=varaus[3],
        paiva=datetime.strptime(varaus[4], "%Y-%m-%d").date(),
        kellonaika=datetime.strptime(varaus[5], "%H:%M").time(),
        kesto=int(varaus[6]),
        hinta=float(varaus[7]),
        vahvistettu=varaus[8].lower() == "true",
        kohde=varaus[9],
        luotu=datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S"),
        asiakasnumero=asiakasnumero
    )

def hae_varaukset(tiedosto: str) -> list[Varaus]:
    varaukset = []
    with open(tiedosto, "r", encoding="utf-8") as f:
        for index, rivi in enumerate(f, start=1):
            osat = rivi.strip().split('|')
            varaus = muunna_varaustiedot(osat, asiakasnumero=index)
            varaukset.append(varaus)
    return varaukset


def vahvistetut_varaukset(varaukset: list[Varaus]) -> None:
    for varaus in varaukset:
        if varaus.is_confirmed():
            print(f"- {varaus.nimi}, {varaus.kohde}, "
                  f"{varaus.paiva.strftime('%d.%m.%Y')} klo {varaus.kellonaika.strftime('%H.%M')}, asiakasnumero {varaus.asiakasnumero}")
    print()

def pitkat_varaukset(varaukset: list[Varaus]) -> None:
    for varaus in varaukset:
        if varaus.is_long():
            print(f"- {varaus.nimi}, {varaus.paiva.strftime('%d.%m.%Y')} klo {varaus.kellonaika.strftime('%H.%M')}, "
                  f"kesto {varaus.kesto} h, {varaus.kohde}, asiakasnumero {varaus.asiakasnumero}")
    print()

def varausten_vahvistusstatus(varaukset: list[Varaus]) -> None:
    for varaus in varaukset:
        if varaus.is_confirmed():
            print(f"{varaus.nimi} → Vahvistettu")
        else:
            print(f"{varaus.nimi} → EI vahvistettu")
    print()

def varausten_lkm(varaukset: list[Varaus]) -> None:
    vahvistetut = sum(1 for v in varaukset if v.is_confirmed())
    ei_vahvistetut = len(varaukset) - vahvistetut

    print(f"- Vahvistettuja varauksia: {vahvistetut} kpl")
    print(f"- Ei-vahvistettuja varauksia: {ei_vahvistetut} kpl")
    print()

def varausten_kokonaistulot(varaukset: list[Varaus]):
    tulot = sum(v.total_price() for v in varaukset if v.is_confirmed())

    print("Vahvistettujen varausten kokonaistulot:",
          f"{tulot:.2f}".replace('.', ','), "€")
    print()

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