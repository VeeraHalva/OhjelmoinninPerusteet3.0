
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

#TÄSTÄ ALKAA BONARIT

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
    
    lukemat1 = lue_data("viikko41.csv")
    lukemat2 = lue_data("viikko42.csv")
    lukemat3 = lue_data("viikko43.csv")
    #print(lue_data("viikko42.csv"))
    #print(lue_data("viikko42.csv")[0][0])
    
    print( )
    Päivä = "päivä"
    Pvm = "pvm"
    Kulutus = "Kulutus [kWh]"
    Tuotanto = "Tuotanto [kWh]" 
    pvkkvvvv = "(pv.kk.vvvv)"
    v1 = "v1"   
    v2 = "v2"
    v3 = "v3"
        
#päivämäärät voisi varmaan käydä omassa silmukassaan läpi, niin ei tulisi toistoa. Mutta tämä tulostaa jo halutun lopputuloksen.
#bonus tehtävän tulostus pyritty tekemään silmukoita hyväksi käyttäen. tehty uudestaan, ettei sotke alkuperäistä toimivaa koodia.

    otsikkooo = "Bonus-tehtävät:\n"
    paivat1 =[
        ("Maanantai", "06.10.2025"),
        ("Tiistai", "07.10.2025"),
        ("Keskiviikko", "08.10.2025"),
        ("Torstai", "09.10.2025"),
        ("Perjantai", "10.10.2025"),
        ("Lauantai", "11.10.2025"),
        ("Sunnuntai", "12.10.2025"),
        ("Maanantai", "13.10.2025")]
    paivat2 =[
        ("Maanantai", "13.10.2025"),
        ("Tiistai", "14.10.2025"),
        ("Keskiviikko", "15.10.2025"),
        ("Torstai", "16.10.2025"),
        ("Perjantai", "17.10.2025"),
        ("Lauantai", "18.10.2025"),
        ("Sunnuntai", "19.10.2025")]
    paivat3 =[
        ("Maanantai", "20.10.2025"),
        ("Tiistai", "21.10.2025"),
        ("Keskiviikko", "22.10.2025"),
        ("Torstai", "23.10.2025"),
        ("Perjantai", "24.10.2025"),
        ("Lauantai", "25.10.2025"),
        ("Sunnuntai", "26.10.2025"), 
        ]
    
# ensin lasketaan kaikki nettokulutukset talteen
    nettokulutukset = {}
    lukemat = lukemat1 + lukemat2 + lukemat3
    paivat = paivat1 + paivat2 + paivat3
    for nimi, pvm in paivat:
        arvot = paivantiedot(pvm, lukemat)
        nettokulutus = (arvot[0]+arvot[1]+arvot[2]) - (arvot[3]+arvot[4]+arvot[5])
        nettokulutukset[pvm] = nettokulutus

# haetaan suurin nettokulutus (numeroarvo)
    paras_pvm = max(nettokulutukset, key=nettokulutukset.get)
# tulosteen taulukko vko 41
    Bviikko41 = "Viikon 41 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n"
    Bviikko41 += " \n"
    Bviikko41 += f"{Päivä:<12}{Pvm:<12}{Kulutus:>17}{Tuotanto :>24}{'Nettokulutus':>24}\n"
    Bviikko41 += f"{'':<12}{pvkkvvvv:<12}{v1:>7}{v2:>7}{v3:>6}{v1:>10}{v2:>7}{v3:>7}{'päivittäin':>20}\n"
    Bviikko41 += "--------------------------------------------------------------------------------------------\n"
    for nimi, pvm in paivat1:
        arvot = paivantiedot(pvm, lukemat1)
        kulutus = [f"{x:.2f}".replace('.', ',') for x in arvot[:3]]
        tuotanto = [f"{x:.2f}".replace('.', ',') for x in arvot[3:]]
        nettokulutus = (arvot[0]+arvot[1]+arvot[2]) - (arvot[3]+arvot[4]+arvot[5])
        nettokulutus_str = f"{nettokulutus:.2f}".replace('.', ',')
        merkki = "*" if pvm == paras_pvm else ""

        Bviikko41 += (f"{nimi:<12}{pvm:<12}"
          f"{kulutus[0]:>9}{kulutus[1]:>7}{kulutus[2]:>6}"
          f"{tuotanto[0]:>10}{tuotanto[1]:>7}{tuotanto[2]:>7}"
          f"{nettokulutus_str:>15}{merkki:>1}\n")
        
    Bviikko41 += "-------------------------------------------------------------------------------------------\n"
    Bviikko41 += "\n"
# tulostetaan taulukko vko 42
    Bviikko42 = "Viikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n"
    Bviikko42 += " \n"
    Bviikko42 += f"{Päivä:<12}{Pvm:<12}{Kulutus:>17}{Tuotanto :>24}{'Nettokulutus':>24}\n"
    Bviikko42 += f"{'':<12}{pvkkvvvv:<12}{v1:>7}{v2:>7}{v3:>6}{v1:>10}{v2:>7}{v3:>7}{'päivittäin':>20}\n"
    Bviikko42 += "--------------------------------------------------------------------------------------------\n"
    for nimi, pvm in paivat2:
        arvot = paivantiedot(pvm, lukemat2)
        kulutus = [f"{x:.2f}".replace('.', ',') for x in arvot[:3]]
        tuotanto = [f"{x:.2f}".replace('.', ',') for x in arvot[3:]]
        nettokulutus = (arvot[0]+arvot[1]+arvot[2]) - (arvot[3]+arvot[4]+arvot[5])
        nettokulutus_str = f"{nettokulutus:.2f}".replace('.', ',')
        merkki = "*" if pvm == paras_pvm else ""

        Bviikko42 += (f"{nimi:<12}{pvm:<12}"
          f"{kulutus[0]:>9}{kulutus[1]:>7}{kulutus[2]:>6}"
          f"{tuotanto[0]:>10}{tuotanto[1]:>7}{tuotanto[2]:>7}"
          f"{nettokulutus_str:>15}{merkki:>1}\n")
    Bviikko42 += "-------------------------------------------------------------------------------------------\n"
    Bviikko42 += "\n"
#tulostetaan taulukko vko 43
    Bviikko43 = "Viikon 43 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n"
    Bviikko43 += " \n"
    Bviikko43 += f"{Päivä:<12}{Pvm:<12}{Kulutus:>17}{Tuotanto :>24}{'Nettokulutus':>24}\n"
    Bviikko43 += f"{'':<12}{pvkkvvvv:<12}{v1:>7}{v2:>7}{v3:>6}{v1:>10}{v2:>7}{v3:>7}{'päivittäin':>20}\n"
    Bviikko43 += "--------------------------------------------------------------------------------------------\n"
    Bviikko43 += "\n"
    for nimi, pvm in paivat3:
        arvot = paivantiedot(pvm, lukemat3)
        kulutus = [f"{x:.2f}".replace('.', ',') for x in arvot[:3]]
        tuotanto = [f"{x:.2f}".replace('.', ',') for x in arvot[3:]]
        nettokulutus = (arvot[0]+arvot[1]+arvot[2]) - (arvot[3]+arvot[4]+arvot[5])
        nettokulutus_str = f"{nettokulutus:.2f}".replace('.', ',')
        merkki = "*" if pvm == paras_pvm else ""  

        Bviikko43 += (f"{nimi:<12}{pvm:<12}"
          f"{kulutus[0]:>9}{kulutus[1]:>7}{kulutus[2]:>6}"
          f"{tuotanto[0]:>10}{tuotanto[1]:>7}{tuotanto[2]:>7}"
          f"{nettokulutus_str:>15}{merkki:>1}\n")
    Bviikko43 += "-------------------------------------------------------------------------------------------\n"

    #print("viikon 41 yhteenveto:")
    kokonaiskulutus_vk41_v1 = sum(paivantiedot(pvm, lukemat1)[0] for _, pvm in paivat1)
    kokonaiskulutus_vk41_v2 = sum(paivantiedot(pvm, lukemat1)[1] for _, pvm in paivat1)
    kokonaiskulutus_vk41_v3 = sum(paivantiedot(pvm, lukemat1)[2] for _, pvm in paivat1)
    kokonaisproduktio_vk41_v1 = sum(paivantiedot(pvm, lukemat1)[3] for _, pvm in paivat1)
    kokonaisproduktio_vk41_v2 = sum(paivantiedot(pvm, lukemat1)[4] for _, pvm in paivat1)
    kokonaisproduktio_vk41_v3 = sum(paivantiedot(pvm, lukemat1)[5] for _, pvm in paivat1)

    Viikko41yht =("\n")       
    Viikko41yht += "Viikon 41 yhteenveto (kokonaiskulutus ja -tuotanto vaiheittain)\n"
    Viikko41yht += F"{'':>30}v1{'':>7}v2{'':>7}v3{'':>6}\n"
    Viikko41yht += "--------------------------------------------------------------\n"
    Viikko41yht += "kulutus yhteensä [kWh]" + f"{kokonaiskulutus_vk41_v1:>12.2f}".replace('.',',') + f"{kokonaiskulutus_vk41_v2:>8.2f}".replace('.',',') + f"{kokonaiskulutus_vk41_v3:>8.2f}".replace('.',',') + "\n"
    Viikko41yht += "tuotanto yhteensä [kWh]" + f"{kokonaisproduktio_vk41_v1:>11.2f}".replace('.',',') + f"{kokonaisproduktio_vk41_v2:>8.2f}".replace('.',',') + f"{kokonaisproduktio_vk41_v3:>8.2f}".replace('.',',') + "\n"
    Viikko41yht += "--------------------------------------------------------------\n"

    #print("viikon 42 yhteenveto:")
    kokonaiskulutus_vk42_v1 = sum(paivantiedot(pvm, lukemat2)[0] for _, pvm in paivat2)
    kokonaiskulutus_vk42_v2 = sum(paivantiedot(pvm, lukemat2)[1] for _, pvm in paivat2) 
    kokonaiskulutus_vk42_v3 = sum(paivantiedot(pvm, lukemat2)[2] for _, pvm in paivat2)
    kokonaisproduktio_vk42_v1 = sum(paivantiedot(pvm, lukemat2)[3] for _, pvm in paivat2)
    kokonaisproduktio_vk42_v2 = sum(paivantiedot(pvm, lukemat2)[4] for _, pvm in paivat2)
    kokonaisproduktio_vk42_v3 = sum(paivantiedot(pvm, lukemat2)[5] for _, pvm in paivat2)

    Viikko42yht =("\n")      
    Viikko42yht += "Viikon 42 yhteenveto (kokonaiskulutus ja -tuotanto vaiheittain)\n"
    Viikko42yht += F"{'':>30}v1{'':>7}v2{'':>7}v3{'':>6}\n"
    Viikko42yht += "--------------------------------------------------------------\n"
    Viikko42yht += "kulutus yhteensä [kWh]" + f"{kokonaiskulutus_vk42_v1:>12.2f}".replace('.',',') + f"{kokonaiskulutus_vk42_v2:>8.2f}".replace('.',',') + f"{kokonaiskulutus_vk42_v3:>8.2f}".replace('.',',') + "\n"
    Viikko42yht += "tuotanto yhteensä [kWh]" + f"{kokonaisproduktio_vk42_v1:>11.2f}".replace('.',',') + f"{kokonaisproduktio_vk42_v2:>8.2f}".replace('.',',') + f"{kokonaisproduktio_vk42_v3:>8.2f}".replace('.',',') + "\n"
    Viikko42yht += "--------------------------------------------------------------\n"

    #print("viikon 43 yhteenveto:")
    kokonaiskulutus_vk43_v1 = sum(paivantiedot(pvm, lukemat3)[0] for _, pvm in paivat3)
    kokonaiskulutus_vk43_v2 = sum(paivantiedot(pvm, lukemat3)[1] for _, pvm in paivat3)
    kokonaiskulutus_vk43_v3 = sum(paivantiedot(pvm, lukemat3)[2] for _, pvm in paivat3)
    kokonaisproduktio_vk43_v1 = sum(paivantiedot(pvm, lukemat3)[3] for _, pvm in paivat3)
    kokonaisproduktio_vk43_v2 = sum(paivantiedot(pvm, lukemat3)[4] for _, pvm in paivat3)
    kokonaisproduktio_vk43_v3 = sum(paivantiedot(pvm, lukemat3)[5] for _, pvm in paivat3)

    Viikko43yht =("\n")    
    Viikko43yht += "Viikon 43 yhteenveto (kokonaiskulutus ja -tuotanto vaiheittain)\n"
    Viikko43yht += F"{'':>30}v1{'':>7}v2{'':>7}v3{'':>6}\n"
    Viikko43yht += "--------------------------------------------------------------\n"
    Viikko43yht += "kulutus yhteensä [kWh]" + f"{kokonaiskulutus_vk43_v1:>12.2f}".replace('.',',') + f"{kokonaiskulutus_vk43_v2:>8.2f}".replace('.',',') + f"{kokonaiskulutus_vk43_v3:>8.2f}".replace('.',',') + "\n"
    Viikko43yht += "tuotanto yhteensä [kWh]" + f"{kokonaisproduktio_vk43_v1:>11.2f}".replace('.',',') + f"{kokonaisproduktio_vk43_v2:>8.2f}".replace('.',',') + f"{kokonaisproduktio_vk43_v3:>8.2f}".replace('.',',') + "\n"
    Viikko43yht += "--------------------------------------------------------------\n"

    kokonaiskulutus_v1 = sum(paivantiedot(pvm, lukemat)[0] for _, pvm in paivat)
    kokonaiskulutus_v2 = sum(paivantiedot(pvm, lukemat)[1] for _, pvm in paivat)
    kokonaiskulutus_v3 = sum(paivantiedot(pvm, lukemat)[2] for _, pvm in paivat)
    kokonaisproduktio_v1 = sum(paivantiedot(pvm, lukemat)[3] for _, pvm in paivat)
    kokonaisproduktio_v2 = sum(paivantiedot(pvm, lukemat)[4] for _, pvm in paivat)
    kokonaisproduktio_v3 = sum(paivantiedot(pvm, lukemat)[5] for _, pvm in paivat)

    Kaikkiyht =("\n")       
    Kaikkiyht += "Kaikkien viikkojen yhteenveto (kokonaiskulutus ja -tuotanto vaiheittain)\n"

    Kaikkiyht += F"{'':>30}v1{'':>7}v2{'':>7}v3{'':>6}\n"
    Kaikkiyht += "--------------------------------------------------------------\n"
    Kaikkiyht += "kulutus yhteensä [kWh]" + f"{kokonaiskulutus_v1:>12.2f}".replace('.',',') + f"{kokonaiskulutus_v2:>8.2f}".replace('.',',') + f"{kokonaiskulutus_v3:>8.2f}".replace('.',',') + "\n"
    Kaikkiyht += "tuotanto yhteensä [kWh]" + f"{kokonaisproduktio_v1:>11.2f}".replace('.',',') + f"{kokonaisproduktio_v2:>8.2f}".replace('.',',') + f"{kokonaisproduktio_v3:>8.2f}".replace('.',',') + "\n"
    Kaikkiyht += "--------------------------------------------------------------\n"
#Siiretään bonustulokset tiedostoon
    with open("Bonukset.txt", "w", encoding="utf-8") as f:
        f.write(otsikkooo)
        f.write(Bviikko41)
        f.write(Bviikko42)
        f.write(Bviikko43) 
        f.write(Viikko41yht)
        f.write(Viikko42yht)
        f.write(Viikko43yht)
        f.write(Kaikkiyht)

    


if __name__ == "__main__":
    main()