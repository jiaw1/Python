# kopioi edellisestä tehtävästä funktion viiva koodi tänne

def viiva(leveys, merkkijono):
    if merkkijono == "":
        print("*"*leveys)
    else:
        print(merkkijono[0]*leveys)

def kolmio(koko):
    i = 0
    j = 1
    while i<koko:
        viiva(j,"#")
        i += 1 
        j += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(5)
