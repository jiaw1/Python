# tee ratkaisu tänne

def uniikit(lista : list):
    lista.sort()
    uniikkilista = []
    for luku in lista:
        if luku not in uniikkilista:
            uniikkilista.append(luku)
    return uniikkilista
