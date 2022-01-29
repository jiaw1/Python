# tee ratkaisu tänne

def eniten_kirjainta(mjono: str):
    eniten = mjono[0]
    for i in mjono:
        if mjono.count(i) > mjono.count(eniten):
            eniten = i
    return eniten
