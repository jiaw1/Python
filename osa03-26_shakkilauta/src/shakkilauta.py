# tee ratkaisu tänne

# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    shakkilauta(3)

def shakkilauta(koko):
    i = 0
    while i < koko:
        if i % 2 == 0:
            rivi = "10"*koko
        else:
            rivi = "01"*koko
        # poistetaan rivin lopusta ylimääräiset merkit
        print(rivi[0:koko])
        i += 1
