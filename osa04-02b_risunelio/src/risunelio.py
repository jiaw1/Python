# kopioi edellisestä tehtävästä funktion viiva koodi tänne

def viiva(leveys, merkkijono):
    if merkkijono == "":
        print("*"*leveys)
    else:
        print(merkkijono[0]*leveys)

def risunelio(koko):
    i = 0
    while i<koko:
        viiva(koko,"#")
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)
