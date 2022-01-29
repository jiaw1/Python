# Kirjoita ratkaisu tähän
opiskelija = int(input("Montako opiskelijaa?"))
koko = int(input("Mikä on ryhmän koko?"))

maara = (opiskelija//koko)
jako = (opiskelija%koko)

if jako > 0:
    print(f"Ryhmien määrä: {maara+1}")
else:
    print(f"Ryhmien määrä: {maara}")
