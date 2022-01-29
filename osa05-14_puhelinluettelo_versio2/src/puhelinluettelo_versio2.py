# tee ratkaisu tänne

def komento():
    henkilot = {}
    while True:
        luku = input("komento (1 hae, 2 lisää, 3 lopeta): ")
        if (luku == "1"):
            nimi = input("nimi: ")
            if nimi in henkilot:
                for numero in henkilot[nimi]:
                    print(numero)
            else:
                print("ei numeroa")
        if (luku == "2"):
            nimi = input("nimi: ")
            numero = input("numero: ")
            if nimi not in henkilot:
                henkilot[nimi] = []
            henkilot[nimi].append(numero)
            print("ok!")
        if (luku == "3"):
            break

    print("lopetetaan...")

komento()
