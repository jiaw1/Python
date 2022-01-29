# tee ratkaisu tänne

def etsi_elokuvat(rekisteri: list, hakusana: str):
    lista = []
    for i in rekisteri:
        if hakusana.lower() in i['nimi'].lower():
            lista.append(i)
    return lista
