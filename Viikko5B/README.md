# tehtävä pipeline

1. Luetaan tiedostot

```py
    KulutusTuotantoViikko41 = lue_data("viikko41.csv")
    KulutusTuotantoViikko42 = lue_data("viikko42.csv")
    KulutusTuotantoViikko43 = lue_data("viikko43.csv")
```
2. Tiedostot ovat oikean tyyppiset

```py
        print("Viikko 41")
    print("----------------------------")
    print(KulutusTuotantoViikko41[0])
    for i, arvo in enumerate(KulutusTuotantoViikko41[0]):
        print(f"Indeksi {i}: {arvo} -> {type(arvo)}")
    print(" ")
    print("Viikko 42")
    print("----------------------------")
    print(KulutusTuotantoViikko42[0])
    for i, arvo in enumerate(KulutusTuotantoViikko42[0]):
        print(f"Indeksi {i}: {arvo} -> {type(arvo)}")
    print(" ")
    print("Viikko 43")
    print("----------------------------")
    print(KulutusTuotantoViikko43[0])
    for i, arvo in enumerate(KulutusTuotantoViikko43[0]):
        print(f"Indeksi {i}: {arvo} -> {type(arvo)}")
```
3. Raportoidaan tiedostoista jotain (konsoli)
```py
    #Viikko 41 raportti
    print("\nViikon 41 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\tPvm\t\tKulutus [kWh]\t\tTuotanto [kWh]")
    print("\t\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\tv2\tv3")
    print("---------------------------------------------------------------------------")
    print("Maanantai\t" + "\t".join(paivantiedot(date(2025, 10, 6), KulutusTuotantoViikko41)))
    print("Tiistai\t\t" + "\t".join(paivantiedot(date(2025, 10, 7), KulutusTuotantoViikko41))) 
    print("Keskiviikko\t" + "\t".join(paivantiedot(date(2025, 10, 8), KulutusTuotantoViikko41)))
    print("Torstai\t\t" + "\t".join(paivantiedot(date(2025, 10, 9), KulutusTuotantoViikko41)))
    print("Perjantai\t" + "\t".join(paivantiedot(date(2025, 10, 10), KulutusTuotantoViikko41)))
    print("Lauantai\t" + "\t".join(paivantiedot(date(2025, 10, 11), KulutusTuotantoViikko41)))
    print("Sunnuntai\t" + "\t".join(paivantiedot(date(2025, 10, 12), KulutusTuotantoViikko41)))
    print("---------------------------------------------------------------------------")
    # Viikko 42 raportti
    print("\nViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\tPvm\t\tKulutus [kWh]\t\tTuotanto [kWh]")
    print("\t\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\tv2\tv3")
    print("---------------------------------------------------------------------------")
    print("Maanantai\t" + "\t".join(paivantiedot(date(2025, 10, 13), KulutusTuotantoViikko42)))
    print("Tiistai\t\t" + "\t".join(paivantiedot(date(2025, 10, 14), KulutusTuotantoViikko42))) 
    print("Keskiviikko\t" + "\t".join(paivantiedot(date(2025, 10, 15), KulutusTuotantoViikko42)))
    print("Torstai\t\t" + "\t".join(paivantiedot(date(2025, 10, 16), KulutusTuotantoViikko42)))
    print("Perjantai\t" + "\t".join(paivantiedot(date(2025, 10, 17), KulutusTuotantoViikko42)))
    print("Lauantai\t" + "\t".join(paivantiedot(date(2025, 10, 18), KulutusTuotantoViikko42)))
    print("Sunnuntai\t" + "\t".join(paivantiedot(date(2025, 10, 19), KulutusTuotantoViikko42)))
    print("---------------------------------------------------------------------------")

    # Viikko 43 raportti
    print("\nViikon 43 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\tPvm\t\tKulutus [kWh]\t\tTuotanto [kWh]")
    print("\t\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\tv2\tv3")
    print("---------------------------------------------------------------------------")
    print("Maanantai\t" + "\t".join(paivantiedot(date(2025, 10, 20), KulutusTuotantoViikko43)))
    print("Tiistai\t\t" + "\t".join(paivantiedot(date(2025, 10, 21), KulutusTuotantoViikko43))) 
    print("Keskiviikko\t" + "\t".join(paivantiedot(date(2025, 10, 22), KulutusTuotantoViikko43)))
    print("Torstai\t\t" + "\t".join(paivantiedot(date(2025, 10, 23), KulutusTuotantoViikko43)))
    print("Perjantai\t" + "\t".join(paivantiedot(date(2025, 10, 24), KulutusTuotantoViikko43)))
    print("Lauantai\t" + "\t".join(paivantiedot(date(2025, 10, 25), KulutusTuotantoViikko43)))
    print("Sunnuntai\t" + "\t".join(paivantiedot(date(2025, 10, 26), KulutusTuotantoViikko43)))
    print("---------------------------------------------------------------------------")
```
4. Kiroitetaan tiedostoon jotain
```py 
    with open("yhteenveto.txt","w", encoding="utf-8") as f:
       f.write("Hei maailma!\n")
```
5. Kirjoitetaan tiedostoon raportin pohja
```py
    with open("yhteenveto.txt", "w", encoding="utf-8") as f:
        f.write(viikko41)
        f.write(viikko42)
        f.write(viikko43)   
```