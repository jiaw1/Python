# tee ratkaisu tänne

def summa():

    with open ('matriisi.txt') as tiedosto:

        summa = 0
        i = 0

        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            alkiot = rivi.split(',')
            summa += int(alkiot[i])
            i += 1

    return summa

def maksimi():

    with open ('matriisi.txt') as tiedosto:

        maksimi = 0
        i = 0

        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            alkiot = rivi.split(",")
            alkio = int(alkiot[i])
            if alkio > maksimi:
                maksimi = alkio
            i += 1
    
    return maksimi

def rivisummat():

    with open ('matriisi.txt') as tiedosto:

        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            alkiot = rivi.split(',')
            rivisumma = int()




if __name__ == '__main__':
    print(summa())
    print(maksimi())
