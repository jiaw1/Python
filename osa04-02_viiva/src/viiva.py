# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti

def viiva(leveys, merkkijono):
    if merkkijono == "":
        print("*"*leveys)
    else:
        print(merkkijono[0]*leveys)