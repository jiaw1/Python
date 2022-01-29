# Kirjoita ratkaisu tähän
yritykset = 0

while True:
    tunnus = input("Anna PIN-koodi: ")
    yritykset += 1

    if tunnus == "4321":
        onnistui = True
        break

    print("Väärin")

if onnistui:
    if yritykset == 1 and tunnus == "4321":
        print("Oikein, tarvitsit vain yhden yrityksen!")  
    else:
        print(f"Oikein, tarvitsit {yritykset} yritystä")
    