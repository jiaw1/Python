# tee ratkaisu tänne

def lyhin(lista: list):
    lista.sort(key = len)
    lyhin = lista[0]
    return lyhin

def lyhin(nimet: list):
    tulos = ""
    for nimi in nimet:
        if tulos == "" or len(nimi) < len(tulos):
            tulos = nimi
    return tulos