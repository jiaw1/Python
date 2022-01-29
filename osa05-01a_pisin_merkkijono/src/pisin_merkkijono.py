# tee ratkaisu tänne

def pisin(merkkijonot: list):
    pisin = ""
    for i in merkkijonot:
        if len(i) > len(pisin):
            pisin = i
    return pisin

if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))
