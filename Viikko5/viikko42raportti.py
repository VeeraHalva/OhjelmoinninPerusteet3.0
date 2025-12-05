
# Copyright (c) 2025 Oma Nimi
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

        
#päivämäärät voisi varmaan käydä omassa silmukassaan läpi, niin ei tulisi toistoa. Mutta tämä tulostaa jo halutun lopputuloksen.
#bonus tehtävän tulostus pyritty tekemään silmukoita hyväksi käyttäen. tehty uudestaan, ettei sotke alkuperäistä toimivaa koodia.

    print("Bonus-tehtävät:")
    paivat =[
        ("Maanantai", "13.10.2025"),
        ("Tiistai", "14.10.2025"),
        ("Keskiviikko", "15.10.2025"),
        ("Torstai", "16.10.2025"),
        ("Perjantai", "17.10.2025"),
        ("Lauantai", "18.10.2025"),
        ("Sunnuntai", "19.10.2025")]
    
    print(f"{Päivä:<12}{Pvm:<12}{Kulutus:>17}{Tuotanto :>24}{"Nettokulutus":>24}")
    print(f"{'':<12}{pvkkvvvv:<12}{v1:>7}{v2:>7}{v3:>6}{v1:>10}{v2:>7}{v3:>7}{"päivittäin":>20}")
    print("--------------------------------------------------------------------------------------------")
# ensin lasketaan kaikki nettokulutukset talteen
    nettokulutukset = {}
    for nimi, pvm in paivat:
        arvot = paivantiedot(pvm, lukemat)
        nettokulutus = (arvot[0]+arvot[1]+arvot[2]) - (arvot[3]+arvot[4]+arvot[5])
        nettokulutukset[pvm] = nettokulutus

# haetaan suurin nettokulutus (numeroarvo)
    paras_pvm = max(nettokulutukset, key=nettokulutukset.get)

# tulostetaan taulukko
    for nimi, pvm in paivat:
        arvot = paivantiedot(pvm, lukemat)
        kulutus = [f"{x:.2f}".replace('.', ',') for x in arvot[:3]]
        tuotanto = [f"{x:.2f}".replace('.', ',') for x in arvot[3:]]
        nettokulutus = (arvot[0]+arvot[1]+arvot[2]) - (arvot[3]+arvot[4]+arvot[5])
        nettokulutus_str = f"{nettokulutus:.2f}".replace('.', ',')
        merkki = "*" if pvm == paras_pvm else ""

        print(f"{nimi:<12}{pvm:<12}"
          f"{kulutus[0]:>9}{kulutus[1]:>7}{kulutus[2]:>6}"
          f"{tuotanto[0]:>10}{tuotanto[1]:>7}{tuotanto[2]:>7}"
          f"{nettokulutus_str:>15}{merkki:>1}")
        
    kokonaiskulutus_v1 = sum(paivantiedot(pvm, lukemat)[0] for _, pvm in paivat)
    kokonaiskulutus_v2 = sum(paivantiedot(pvm, lukemat)[1] for _, pvm in paivat)
    kokonaiskulutus_v3 = sum(paivantiedot(pvm, lukemat)[2] for _, pvm in paivat)
    kokonaisproduktio_v1 = sum(paivantiedot(pvm, lukemat)[3] for _, pvm in paivat)
    kokonaisproduktio_v2 = sum(paivantiedot(pvm, lukemat)[4] for _, pvm in paivat)
    kokonaisproduktio_v3 = sum(paivantiedot(pvm, lukemat)[5] for _, pvm in paivat)

    print("____________________________________________________________________________________________")
    print( )       
    print("viikon yhteenveto (kokonaiskulutus ja -tuotanto vaiheittain)")
    print(" ")
    print(F"{'':>30}v1{'':>7}v2{'':>7}v3{'':>6}")
    print("--------------------------------------------------------------")
    print("kulutus yhteensä [kWh]", f"{kokonaiskulutus_v1:>12.2f}".replace('.',','), f"{kokonaiskulutus_v2:>8.2f}".replace('.',','),
          f"{kokonaiskulutus_v3:>8.2f}".replace('.',','))
    print("tuotanto yhteensä [kWh]", f"{kokonaisproduktio_v1:>11.2f}".replace('.',','), f"{kokonaisproduktio_v2:>8.2f}".replace('.',','),
          f"{kokonaisproduktio_v3:>8.2f}".replace('.',',')) 
    print("--------------------------------------------------------------") 

#Tästä alkaa bonus valikon koodi. tulostaa siis pelkän valikon. koodi muuhun löytyy myös, mutta erillisenä funktiona.Jos haluaa nähdä aikaisemmat on nämä laitettava kommentteina "pois päältä".
# kai tämänkin olisi voinut eri tavalla, mutta osaaminen loppuu ainakin vielä kesken. Koodi myös vähän kamalan näköinen, mutta toimii.
#käytetty samoja apufunktioita kuin aikaisemminkin, mutta tehty uudestaan, jotta alkuperäinen pysyy ehjänä.
def nayta_valikko() -> str:
    """Näyttää valikon ja palauttaa käyttäjän valinnan."""
    print("\nValikko:")
    print("1) Näytä vain kulutus")
    print("2) Näytä vain tuotanto")
    print("3) Näytä molemmat")
    valinta = input("Valitse (1-3): ")
    return valinta

def main():
    lukemat = lue_data("viikko42.csv")
    paivat = [
        ("Maanantai", "13.10.2025"),
        ("Tiistai", "14.10.2025"),
        ("Keskiviikko", "15.10.2025"),
        ("Torstai", "16.10.2025"),
        ("Perjantai", "17.10.2025"),
        ("Lauantai", "18.10.2025"),
        ("Sunnuntai", "19.10.2025"),
    ]

    valinta = nayta_valikko()

    1
    if valinta == "1":
        print("\nViikon 42 sähkönkulutus kWh, vaiheittain:\n")
        print(f"{'Päivä':<12}{'Pvm':<12}{'v1':>10}{'v2':>8}{'v3':>8}")
        print("----------------------------------------------------------")
        for nimi, pvm in paivat:
            arvot = paivantiedot(pvm, lukemat)
            kulutus = [f"{x:.2f}".replace('.', ',') for x in arvot[:3]]
            print(f"{nimi:<12}{pvm:<12}{kulutus[0]:>12}{kulutus[1]:>8}{kulutus[2]:>8}")

    elif valinta == "2":
        print("\nViikon 42 sähköntuotanto kWh, vaiheittain:\n")
        print(f"{'Päivä':<12}{'Pvm':<12}{'v1':>10}{'v2':>8}{'v3':>8}")
        print("----------------------------------------------------------")
        for nimi, pvm in paivat:
            arvot = paivantiedot(pvm, lukemat)
            tuotanto = [f"{x:.2f}".replace('.', ',') for x in arvot[3:]]
            print(f"{nimi:<12}{pvm:<12}{tuotanto[0]:>12}{tuotanto[1]:>8}{tuotanto[2]:>8}")

    else: 
        print("\nViikon 42 sähkönkulutus ja -tuotanto kWh, vaiheittain:\n") 
        print(f"{'Kulutus':>38}{'Tuotanto':>30}")
        print(f"{'Päivä':<12}{'Pvm':<12}{'v1':>9}{'v2':>8}{'v3':>8}{'v1':>13}{'v2':>8}{'v3':>8}")
        print("-----------------------------------------------------------------------------------")
        for nimi, pvm in paivat:
            arvot = paivantiedot(pvm, lukemat)
            kulutus = [f"{x:.2f}".replace('.', ',') for x in arvot[:3]]
            tuotanto = [f"{x:.2f}".replace('.', ',') for x in arvot[3:]]
            print(f"{nimi:<12}{pvm:<12}{kulutus[0]:>12}{kulutus[1]:>8}{kulutus[2]:>8}"
                  f"{tuotanto[0]:>12}{tuotanto[1]:>8}{tuotanto[2]:>8}")

if __name__ == "__main__":
    main()