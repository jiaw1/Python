# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen

def viiva(leveys, merkkijono):
    if merkkijono == "":
        print("*"*leveys)
    else:
        print(merkkijono[0]*leveys)

def kuvio(koko1,merkkijono1,koko2,merkkijono2):
    i = 0
    j = 1
    k = 0
    while i<koko1:
        viiva(j,merkkijono1)
        i += 1 
        j += 1
    while k<koko2:
        viiva(koko1,merkkijono2)
        k += 1 
