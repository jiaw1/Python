# tee ratkaisu tänne

def kaanna(sanakirja: dict):
    kopio = {}
    for i in sanakirja:         
        kopio[i] = sanakirja[i]
    for i in kopio:
        del sanakirja[i]
    for i in kopio:
        sanakirja[kopio[i]] = i
