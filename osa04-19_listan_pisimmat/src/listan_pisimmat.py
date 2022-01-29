# tee ratkaisu tänne

def pisimmat(lista: list):
    lista.sort(key = len)
    pisimmat_sanat = []
    for i in lista:
        if len(i) == len(lista[-1]):
            pisimmat_sanat.append(i)
    if len(pisimmat_sanat) > 0:
        return pisimmat_sanat
    else:
        return lista[-1]

def pisimmat(nimet: list):
    tulos = []
 
    for nimi in nimet:
        if tulos == [] or len(nimi) > len(tulos[0]):
            tulos = [nimi]
        elif len(nimi) == len(tulos[0]):
            tulos.append(nimi)
 
    return tulos
