# tee ratkaisu tänne

def suurin():

    with open("luvut.txt") as tiedosto:

        suurin = 0

        for i in tiedosto:
            if int(i) > suurin:
                suurin = int(i)

    return suurin
