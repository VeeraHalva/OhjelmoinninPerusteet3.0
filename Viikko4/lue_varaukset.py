"""
Ohjelma joka tulostaa tiedostosta luettujen varausten alkiot ja niiden tietotyypit

varausId | nimi | sähköposti | puhelin | varauksenPvm | varauksenKlo | varauksenKesto | hinta | varausVahvistettu | varattuTila | varausLuotu
------------------------------------------------------------------------
201 | Muumi Muumilaakso | muumi@valkoinenlaakso.org | 0509876543 | 2025-11-12 | 09:00 | 2 | 18.50 | True | Metsätila 1 | 2025-08-12 14:33:20
int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
------------------------------------------------------------------------
202 | Niiskuneiti Muumilaakso | niisku@muumiglam.fi | 0451122334 | 2025-12-01 | 11:30 | 1 | 12.00 | False | Kukkahuone | 2025-09-03 09:12:48
int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
------------------------------------------------------------------------
203 | Pikku Myy Myrsky | myy@pikkuraivo.net | 0415566778 | 2025-10-22 | 15:45 | 3 | 27.90 | True | Punainen Huone | 2025-07-29 18:05:11
int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
------------------------------------------------------------------------
204 | Nipsu Rahapulainen | nipsu@rahahuolet.me | 0442233445 | 2025-09-18 | 13:00 | 4 | 39.95 | False | Varastotila N | 2025-08-01 10:59:02
int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
------------------------------------------------------------------------
205 | Hemuli Kasvikerääjä | hemuli@kasvikeraily.club | 0463344556 | 2025-11-05 | 08:15 | 2 | 19.95 | True | Kasvitutkimuslabra | 2025-10-09 16:41:55
int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
------------------------------------------------------------------------
"""
from datetime import datetime

def muunna_varaustiedot(varaus: list) -> list:
    #print(varaus)
    # Tähän tulee siis varaus oletustietotyypeillä (str)
    # Varauksessa on 11 saraketta -> Lista -> Alkiot 0-10
    # Muuta tietotyypit haluamallasi tavalla -> Seuraavassa esimerkki ensimmäisestä alkioista
    muutettu_varaus = []
    muutettu_varaus.append(int(varaus[0]))
    muutettu_varaus.append(varaus[1])
    muutettu_varaus.append(varaus[2])
    muutettu_varaus.append(varaus[3])
    muutettu_varaus.append(datetime.strptime(varaus[4], "%Y-%m-%d").date())
    muutettu_varaus.append(datetime.strptime(varaus[5], "%H:%M").time())
    muutettu_varaus.append(int(varaus[6]))
    muutettu_varaus.append(float(varaus[7]))
    muutettu_varaus.append(varaus[8].lower() == 'true' )
    muutettu_varaus.append(varaus[9])
    muutettu_varaus.append(datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S"))
    return muutettu_varaus
    #return muutettu_varaus
    #return [int(varaus[0]), ]

def hae_varaukset(varaustiedosto: str) -> list:
    # HUOM! Tälle funktioille ei tarvitse tehdä mitään!
    # Jos muutat, kommentoi miksi muutit
    varaukset = []
    varaukset.append(["varausId", "nimi", "sähköposti", "puhelin", "varauksenPvm", "varauksenKlo", "varauksenKesto", "hinta", "varausVahvistettu", "varattuTila", "varausLuotu"])
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for varaus in f:
            varaus = varaus.strip()
            varaustiedot = varaus.split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

def vahvistetut_varaukset(varaukset: list):
    for varaus in varaukset[1:]:
        if varaus[8] == True:
         print(f"-{varaus[1]}, {varaus[9]}, pv.{varaus[4].strftime('%d.%m.%Y')} klo {varaus[5].strftime('%H.%M')}")

    print()

def pitkat_varaukset(varaukset: list):
    for varaus in varaukset[1:]:
        if varaus[6] >= 3:
         print(f"-{varaus[1]}, pv.{varaus[4].strftime('%d.%m.%Y')} klo {varaus[5].strftime('%H.%M')}, {varaus[6]} tuntia, {varaus[9]}")

    print()

def varauksen_vahvistusstatus(varaukset: list):
    for varaus in varaukset[1:]:
        status = "vahvistettu" if varaus[8] else "EI vahvistettu"
        print(f"-{varaus[1]} → {status}")

    print()

def yhteenveto_varauksista(varaukset: list):
    vahvistetutvaraukset = 0
    eiVahvistetutvaraukset = 0

    for varaus in varaukset[1:]:
        if varaus[8]:
            vahvistetutvaraukset += 1
        else:
            eiVahvistetutvaraukset += 1

    print(f"-Vahvistettuja varauksia: {vahvistetutvaraukset} kpl")
    print(f"-Ei-vahvistettuja varauksia: {eiVahvistetutvaraukset} kpl")  
  
    print()

def vahvistettujen_varausten_kokonaistulo(varaukset: list):
    kokonaistulo = 0
    for varaus in varaukset[1:]:
        if varaus[8]:
            kokonaistulo += varaus[6] * varaus[7]

    print(f"Vahvistettujen varausten kokonaistulo: {kokonaistulo:.2f}".replace('.', ',') + " € ")
    print()

def kallein_varaus(varaukset: list):
    kallein_hinta = 0
    kallein_varaus = None
    for varaus in varaukset[1:]:
        varauksen_hinta = varaus[6] * varaus[7]
        if varauksen_hinta > kallein_hinta:
            kallein_hinta = varauksen_hinta
            kallein_varaus = varaus

    if kallein_varaus:
        print(f"- {kallein_varaus[1]}) pv.")
        print(f"- Varattu tila: {kallein_varaus[9]}")
        print(f"- Päivä: {kallein_varaus[4].strftime('%d.%m.%Y')}")
        print(f"- Kellonaika: {kallein_varaus[5].strftime('%H.%M')}")
        print(f"- Kesto: {kallein_varaus[6]} tuntia")
        print(f"- Hinta yhteensä: {kallein_hinta:.2f}".replace('.', ',') + " €")

    
    print()

def Varausten_määrä_päivittäin(varaukset: list):
    paivittain = {}
    for varaus in varaukset[1:]:
        pvm = varaus[4]
        if pvm in paivittain:
            paivittain[pvm] += 1
        else:
            paivittain[pvm] = 1

    for pvm, maara in sorted(paivittain.items()):
        print(f"- {pvm.strftime('%d.%m.%Y')}: {maara} kpl")

    print()

def suodatettu_tila(varaukset: list):
    tila = input("anna tilan nimi: ")
    print(f"Varaukset tilassa '{tila}':")
    for varaus in varaukset[1:]:
        if varaus[9].lower() == tila.lower():
            print(f"- {varaus[1]}, {varaus[4].strftime('%d.%m.%Y')} klo {varaus[5].strftime('%H.%M')}, {varaus[6]} h")

    print()

def varaukset_tiettyyn_paivaan(varaukset: list):
    pvm_input = input("Anna päivämäärä (pp.kk.vvvv): ")
    pvm_raja = datetime.strptime(pvm_input, "%d.%m.%Y").date()
    print(f"Varaukset ennen päivämäärää {pvm_raja.strftime('%d.%m.%Y')}:")
    for varaus in varaukset[1:]:
        if varaus[4] <= pvm_raja:
            print(f"- {varaus[1]}, {varaus[4].strftime('%d.%m.%Y')} klo {varaus[5].strftime('%H.%M')}, {varaus[6]} h, {varaus[9]}")

    print()

def vahvistettujen_kesto(varaukset: list):
    total_kesto = 0
    vahvistettujen_maara = 0
    for varaus in varaukset[1:]:
        if varaus[8]:
            total_kesto += varaus[6]
            vahvistettujen_maara += 1

    if vahvistettujen_maara > 0:
        keskiarvo = total_kesto / vahvistettujen_maara
        print(f"- Vahvistettujen varausten keskimääräinen kesto: {keskiarvo:.2f} tuntia")
    else:
        print("- Ei vahvistettuja varauksia.")

    print()

def main():
    # HUOM! seuraaville riveille ei tarvitse tehdä mitään!
    # Jos muutat, kommentoi miksi muutit
    # Kutsutaan funkioita hae_varaukset, joka palauttaa kaikki varaukset oikeilla tietotyypeillä
    varaukset = hae_varaukset("varaukset.txt")
    print("1) vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)

    print("2) Pitkät varaukset (≥ 3 tuntia)")
    pitkat_varaukset(varaukset)

    print("3) Varausten vahvistusstatus")
    varauksen_vahvistusstatus(varaukset)

    print("4) yhteenveto varauksista")
    yhteenveto_varauksista(varaukset)

    print("vahvistettujen varausten kokonaistulo")
    vahvistettujen_varausten_kokonaistulo(varaukset)

    print("kallein varaus:")
    kallein_varaus(varaukset)

    print("Varausten määrä päivittäin:")
    Varausten_määrä_päivittäin(varaukset)   

    print("suodata varaukset tietyn tilan mukaan")
    suodatettu_tila(varaukset)

    print("varaukset tiettyyn päivään asti:")
    varaukset_tiettyyn_paivaan(varaukset)

    print(" vahvistettujen varausten keskimääräinen kesto:")
    vahvistettujen_kesto(varaukset)



    #print(" | ".join(varaukset[0]))
    #print("------------------------------------------------------------------------")
    #for varaus in varaukset[1:]:
    #    print(" | ".join(str(x) for x in varaus))
    #    tietotyypit = [type(x).__name__ for x in varaus]
    #    print(" | ".join(tietotyypit))
    #    print("------------------------------------------------------------------------")
    



if __name__ == "__main__":
    main()