# tee ratkaisu tänne

def pisimman_pituus(lista: list):
    lista.sort(key = len)
    pisin = lista[0]
    return pisin

def pisimman_pituus(lista: list):
    pisin = 0
    for i in lista:
        if len(i) > pisin:
          pisin = len(i)
    return pisin
