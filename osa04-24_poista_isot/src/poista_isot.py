# tee ratkaisu tänne

def poista_isot(lista: list):
    lista_uusi = []
    for i in lista:
        if i.isupper() == False:
            lista_uusi.append(i)
    return lista_uusi


