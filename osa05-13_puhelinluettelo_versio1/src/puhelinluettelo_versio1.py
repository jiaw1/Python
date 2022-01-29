# tee ratkaisu tänne

def komento():
    henkilot = {}
    while True:
        luku = input("komento (1 hae, 2 lisää, 3 lopeta): ")
        if luku == "1":
            nimi = input("nimi: ")
            if nimi in henkilot:
                print(henkilot[nimi])
            else:
                print("ei numeroa")
        if luku == "2":
            nimi = input("nimi: ")
            numero = input("numero: ")
            henkilot[nimi] = numero
            print("ok!")
        if luku == "3":
            break
    print("lopetetaan...")

komento()
