# tee ratkaisu tänne

def kumpi_voitti(pelilauta: list):
    pelaaja1 = 0
    pelaaja2 = 0

    for i in pelilauta:
        for j in i:
            if j == 1:
                pelaaja1 += 1
            elif j == 2:
                pelaaja2 += 1
    
    if pelaaja1 > pelaaja2:
        return 1
    elif pelaaja1 < pelaaja2:
        return 2
    elif pelaaja1 == pelaaja2:
        return 0
