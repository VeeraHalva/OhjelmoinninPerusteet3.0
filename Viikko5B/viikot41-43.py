
# Copyright (c) 2025 Veera Hälvä
# License: MIT License

from datetime import datetime
 
#Uutta koodia

def muunna_tiedot(kulutusTuotanto: list) -> list:
    #muuttaa jokaisen tietorivin sopivaan tietotyyppiin
    muutettu_tietorivi = []
    muutettu_tietorivi.append(datetime.fromisoformat(kulutusTuotanto[0]))
    muutettu_tietorivi.append(int(kulutusTuotanto[1]))
    muutettu_tietorivi.append(int(kulutusTuotanto[2]))
    muutettu_tietorivi.append(int(kulutusTuotanto[3]))
    muutettu_tietorivi.append(int(kulutusTuotanto[4]))
    muutettu_tietorivi.append(int(kulutusTuotanto[5]))
    muutettu_tietorivi.append(int(kulutusTuotanto[6]))
    return muutettu_tietorivi

def lue_data(tiedoston_nimi: str) -> list:
    """Luekee tiedoston ja palauta rivit sopivassa rakenteessa ja tietotyypeissä"""
    kulutusJaTuotantoTiedot = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f) # Ohitetaan otsikkorivi
        for kulutusTuotantoTieto in f:
            kulutusTuotantoTieto = kulutusTuotantoTieto.strip()
            kulutusTuotantoTietoSarakkeet = kulutusTuotantoTieto.split(';')
            kulutusJaTuotantoTiedot.append(muunna_tiedot(kulutusTuotantoTietoSarakkeet))

    return kulutusJaTuotantoTiedot

def paivantiedot(paivamaara: str, lukemat: list) -> int:
    pv = int(paivamaara.split('.')[0])
    kk = int(paivamaara.split('.')[1])
    vuosi = int(paivamaara.split('.')[2])
    lasketutTiedot = [] 
    kulutus1vaihe = 0   
    kulutus2vaihe = 0
    kulutus3vaihe = 0
    tuotanto1vaihe = 0
    tuotanto2vaihe = 0  
    tuotanto3vaihe = 0
    for lukema in lukemat:
        if lukema[0].date() == datetime(vuosi, kk, pv).date():
            kulutus1vaihe += lukema[1]   
            kulutus2vaihe += lukema[2]
            kulutus3vaihe += lukema[3]
            tuotanto1vaihe += lukema[4]
            tuotanto2vaihe += lukema[5]  
            tuotanto3vaihe += lukema[6]

    lasketutTiedot.append(kulutus1vaihe/1000)
    lasketutTiedot.append(kulutus2vaihe/1000)
    lasketutTiedot.append(kulutus3vaihe/1000)
    lasketutTiedot.append(tuotanto1vaihe/1000)
    lasketutTiedot.append(tuotanto2vaihe/1000)
    lasketutTiedot.append(tuotanto3vaihe/1000)
    return lasketutTiedot

            
def main():
    """ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin"""
    
   
    lukemat = lue_data("viikko42.csv")
    #print(lue_data("viikko42.csv"))
    #print(lue_data("viikko42.csv")[0][0])
    print("viikon 42 sähkönkulutis ja -tuotanto (kWh, vaiheittain)")
    print( )
    Päivä = "päivä"
    Pvm = "pvm"
    Kulutus = "Kulutus [kWh]"
    Tuotanto = "Tuotanto [kWh]" 
    print(f"{Päivä:<12}{Pvm:<12}{Kulutus:>17}{Tuotanto :>24}")
    
    pvkkvvvv="pv.kk.vvvv"
    v1="v1"
    v2="v2"
    v3="v3"
    print(f"{'':<12}{pvkkvvvv:<12}{v1:>7}{v2:>7}{v3:>6}{v1:>10}{v2:>7}{v3:>7}")
    print("---------------------------------------------------------------------------")
    Maanantai= "Maanantai"
    Päivämäärä= "13.10.2025"
    maanantailukemat = paivantiedot("13.10.2025", lukemat)
    print(f"{Maanantai:<12}{Päivämäärä:<12}",f"{maanantailukemat[0]:>9.2f}".replace('.',','), f"{maanantailukemat[1]:>5.2f}".replace('.',','),
          f"{maanantailukemat[2]:>5.2f}".replace('.',','),f"{maanantailukemat[3]:>9.2f}".replace('.',','),
          f"{maanantailukemat[4]:>6.2f}".replace('.',','),f"{maanantailukemat[5]:>6.2f}".replace('.',','))
    
#no nyt kyllä loin semmosen koodi-hirviön, että huh huh. sekoitus tekoälyä, selkeästi python kirjaa ja työpajaa. muttaa näyttää toimivan niin saa jäädä tähän.
#erikoiset välimäärät johtuu varmaan välilyönnstä f-stringeissä.tähän lopputulokseen tulin. voin olla myös väärässä selviäsi testaanalla, mutta nyt olen laiska.
#kopio sitten muille viikonpäiville

    Tiistai= "Tiistai"
    Päivämäärä= "14.10.2025" 
    tiistailukemat = paivantiedot("14.10.2025", lukemat)
    print(f"{Tiistai:<12}{Päivämäärä:<12}",f"{tiistailukemat[0]:>9.2f}".replace('.',','), f"{tiistailukemat[1]:>5.2f}".replace('.',','),
          f"{tiistailukemat[2]:>5.2f}".replace('.',','),f"{tiistailukemat[3]:>9.2f}".replace('.',','),
          f"{tiistailukemat[4]:>6.2f}".replace('.',','),f"{tiistailukemat[5]:>6.2f}".replace('.',','))

    Keskiviikko= "Keskiviikko"
    Päivämäärä= "15.10.2025"
    keskiviikkolukemat = paivantiedot("15.10.2025", lukemat)
    print(f"{Keskiviikko:<12}{Päivämäärä:<12}",f"{keskiviikkolukemat[0]:>9.2f}".replace('.',','), f"{keskiviikkolukemat[1]:>5.2f}".replace('.',','),
          f"{keskiviikkolukemat[2]:>5.2f}". replace('.',','),f"{keskiviikkolukemat[3]:>9.2f}".replace('.',','),
          f"{keskiviikkolukemat[4]:>6.2f}".replace('.',','),f"{keskiviikkolukemat[5]:>6.2f}".replace('.',','))

    Torstai= "Torstai"
    Päivämäärä= "16.10.2025"
    torstaillukemat = paivantiedot("16.10.2025", lukemat)
    print(f"{Torstai:<12}{Päivämäärä:<12}",f"{torstaillukemat[0]:>9.2f}".replace('.',','), f"{torstaillukemat[1]:>5.2f}".replace('.',','),
          f"{torstaillukemat[2]:>5.2f}". replace('.',','),f"{torstaillukemat[3]:>9.2f}".replace('.',','),
          f"{torstaillukemat[4]:>6.2f}".replace('.',','),f"{torstaillukemat[5]:>6.2f}".replace('.',','))

    Perjantai= "Perjantai"
    Päivämäärä= "17.10.2025"
    perjantailukemat = paivantiedot("17.10.2025", lukemat)
    print(f"{Perjantai:<12}{Päivämäärä:<12}",f"{perjantailukemat[0]:>9.2f}".replace('.',','), f"{perjantailukemat[1]:>5.2f}".replace('.',','),
          f"{perjantailukemat[2]:>5.2f}". replace('.',','),f"{perjantailukemat[3]:>9.2f}".replace('.',','),
          f"{perjantailukemat[4]:>6.2f}".replace('.',','),f"{perjantailukemat[5]:>6.2f}".replace('.',','))

    Lauantai= "Lauantai"
    Päivämäärä= "18.10.2025"
    lauantailukemat = paivantiedot("18.10.2025", lukemat)
    print(f"{Lauantai:<12}{Päivämäärä:<12}",f"{lauantailukemat[0]:>9.2f}".replace('.',','), f"{lauantailukemat[1]:>5.2f}".replace('.',','),
          f"{lauantailukemat[2]:>5.2f}". replace('.',','),f"{lauantailukemat[3]:>9.2f}".replace('.',','),
          f"{lauantailukemat[4]:>6.2f}".replace('.',','),f"{lauantailukemat[5]:>6.2f}".replace('.',','))

    Sunnuntai= "Sunnuntai"
    Päivämäärä= "19.10.2025"
    sunnuntailukemat = paivantiedot("19.10.2025", lukemat)
    print(f"{Sunnuntai:<12}{Päivämäärä:<12}",f"{sunnuntailukemat[0]:>9.2f}".replace('.',','), f"{sunnuntailukemat[1]:>5.2f}".replace('.',','),
          f"{sunnuntailukemat[2]:>5.2f}". replace('.',','),f"{sunnuntailukemat[3]:>9.2f}".replace('.',','),
          f"{sunnuntailukemat[4]:>6.2f}".replace('.',','),f"{sunnuntailukemat[5]:>6.2f}".replace('.',','))
    
    print("---------------------------------------------------------------------------")
    print( )