# Kirjoita ratkaisu tähän

lista = []
i = -1

while True:
    i += 1
    sana = input("sana: ")
    if sana in lista:
        print(f"Annoit {i} eri sanaa")
        break
    lista.append(sana)
