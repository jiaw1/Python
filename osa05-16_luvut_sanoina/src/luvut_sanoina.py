# tee ratkaisu tänne

def lukukirja():
    numerot = {0:"nolla", 1:"yksi", 2:"kaksi", 3:"kolme", 4:"neljä", 5:"viisi", 6:"kuusi", 7:"seitsemän", 8:"kahdeksan", 9:"yhdeksän"}
    luvut = {}
 
    for i in range(10):
        luvut[i] = numerot[i]
 
    luvut[10] = "kymmenen"
 
    for i in range(1, 10):
        luvut[i + 10] = numerot[i] + "toista"
 
    for i in range(2, 10):
        luvut[i * 10] = numerot[i] + "kymmentä"
        for j in range(1, 10):
            luvut[i * 10 + j] = numerot[i] + "kymmentä" + numerot[j]
 
    return luvut
    