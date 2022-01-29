# tee ratkaisu tänne

def summa(lista1: list, lista2: list):
    summalista = []
    for i in range(0, len(lista1)):
        summalista.append(lista1[i]+lista2[i])
    return summalista
