# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti

def eka_sana(merkkijono):
    i = 0
    tulos = ""
    while merkkijono[i] != " ":
       tulos += merkkijono[i]
       i += 1
    return tulos

def toka_sana(merkkijono):
    i = 0
    j = 0
    tulos = ""
    while i<len(merkkijono):
        if merkkijono[i] == " ":
            j += 1
            if j == 2:
                break
            tulos = ""
        else:
            tulos += merkkijono[i]
        i += 1
    return tulos

def vika_sana(merkkijono):
    i = 0
    j = 0
    tulos = ""
    while i<len(merkkijono):
        if merkkijono[i] == " ":
            j += 1
            if j == 0:
                break
            tulos = ""
        else:
            tulos += merkkijono[i]
        i += 1
    return tulos

if __name__ == "__main__":
    lause = "olipa kerran kauan sitten ohjelmoija"
    print(eka_sana(lause))
    print(toka_sana(lause)) 
    print(vika_sana(lause))
