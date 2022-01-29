# kopioi edellisestä tehtävästä funktion viiva koodi tänne

def viiva(leveys, merkkijono):
    if merkkijono == "":
        print("*"*leveys)
    else:
        print(merkkijono[0]*leveys)

def nelio(koko, merkkijono):
    i = 0
    while i<koko:
        viiva(koko,merkkijono)
        i += 1 

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "x")
