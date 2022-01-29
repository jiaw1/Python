# kopioi edellisestä tehtävästä funktion viiva koodi tänne

def viiva(leveys, merkkijono):
    if merkkijono == "":
        print("*"*leveys)
    else:
        print(merkkijono[0]*leveys)

def risulaatikko(korkeus):
    i = 0
    while i<korkeus:
        viiva(10,"#")
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)
