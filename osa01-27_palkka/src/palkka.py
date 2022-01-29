# Kirjoita ratkaisu tähän
tuntipalkka = float(input("Tuntipalkka:"))
tunti = int(input("Työtunnit:"))
viikonpaiva = str(input("Viikonpäivä:"))

if viikonpaiva == "sunnuntai":
    print(f"Palkka {(tuntipalkka*tunti)*2} euroa")
if viikonpaiva == "maanantai":
    print(f"Palkka {tuntipalkka*tunti} euroa") 
if viikonpaiva == "tiistai":
    print(f"Palkka {tuntipalkka*tunti} euroa")
if viikonpaiva == "keskiviikko":
    print(f"Palkka {tuntipalkka*tunti} euroa")
if viikonpaiva == "torstai":
    print(f"Palkka {tuntipalkka*tunti} euroa")
if viikonpaiva == "perjantai":
    print(f"Palkka {tuntipalkka*tunti} euroa")
if viikonpaiva == "lauantai":
    print(f"Palkka {tuntipalkka*tunti} euroa")
