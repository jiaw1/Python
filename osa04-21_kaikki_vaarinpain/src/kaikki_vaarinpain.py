# tee ratkaisu tänne
 
def kaikki_vaarinpain(lista: list):
    lista_uusi = []
    for i in lista[::-1]:
        lista_uusi.append(i[::-1])
    return lista_uusi
