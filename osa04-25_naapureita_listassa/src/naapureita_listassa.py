# tee ratkaisu tänne

def pisin_naapurijono(lista: list):
    pisin = 1
    naapurijono = 1
    for i in range(1, len(lista)):
        if abs(lista[i-1]-lista[i]) == 1:
            naapurijono += 1
        else:
            naapurijono = 1
        pisin = max(pisin, naapurijono)
    return pisin    

