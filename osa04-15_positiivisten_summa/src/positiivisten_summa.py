# tee ratkaisu tänne

def positiivisten_summa(lista : list):

    positiiviset = []

    for i in lista:
        if i > 0:
            positiiviset.append(i)
    
    return sum(positiiviset)
