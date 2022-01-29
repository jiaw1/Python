# tee ratkaisu tänne

import math

def parilliset(lista: list):
    parilliset = []
    for i in lista:
        if i%2 == 0:
            parilliset.append(i)
    return parilliset
