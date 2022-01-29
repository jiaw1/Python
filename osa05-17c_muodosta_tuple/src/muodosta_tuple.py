# tee ratkaisu tänne

def tee_tuple(x: int, y: int, z: int):
    lista = []
    lista.append(x)
    lista.append(y)
    lista.append(z)
    pienin = min(lista)
    suurin = max(lista)
    summa = sum(lista)

    tuple = (pienin, suurin, summa)
    return(tuple[0], tuple[1], tuple[2])
