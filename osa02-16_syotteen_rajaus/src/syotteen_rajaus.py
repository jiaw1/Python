from math import sqrt
# Kirjoita ratkaisu tähän
while True:
    luku = float(input("Syötä luku:"))
    if luku < 0:
        print("Epäkelpo luku")
        luku = int(input("Syötä luku:"))
        if luku < 0:
            print("Lopetetaan...")
            break
    elif luku > 0:
        print(sqrt(luku))
    if luku == 0:
        print("Lopetetaan...") 
        break 
