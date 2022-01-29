# tee ratkaisu tänne

def lisaa_opiskelija(opiskelijat: dict, nimi: str):
    opiskelijat[nimi] = []
 
def lisaa_suoritus(opiskelijat:dict, nimi:str, kurssi: tuple):
    loytyy = False

    for i in range(0, len(opiskelijat[nimi])):
        if opiskelijat[nimi][i][0] == kurssi[0]:
            loytyy = True
            if opiskelijat[nimi][i][1] < kurssi[1]:
                opiskelijat[nimi][i] = kurssi
                
    if loytyy == False and kurssi[1] != 0:
        opiskelijat[nimi].append(kurssi)
 
def tulosta(opiskelijat:dict, nimi: str):
    if nimi not in opiskelijat:
        print("ei löytynyt ketään nimellä",nimi)
    else:
        print(f"{nimi}:")
        if opiskelijat[nimi] == []:
            print(" ei suorituksia")
        else:
            summa = 0
            kurssit = 0
            suoritukset = []
            for i in range(len(opiskelijat[nimi])):
                if opiskelijat[nimi][i][1] != 0:
                    suoritukset.append(f"  {opiskelijat[nimi][i][0]} {opiskelijat[nimi][i][1]}")
                    summa += opiskelijat[nimi][i][1]
                    kurssit += 1
            print(" suorituksia", kurssit, "kurssilta:")
            for j in suoritukset:
                print(j)
            keskiarvo = summa/kurssit
            opiskelijat[nimi].append(keskiarvo)
            print(" keskiarvo",keskiarvo)
 
def kooste(opiskelijat: dict):
    print("opiskelijoita",len(opiskelijat))
    suoritus_max = 0
    ka_max = 0
    ka = []
    for nimi in opiskelijat:
        summa = 0
        kurssit = 0
        for i in range(len(opiskelijat[nimi])):
            summa += opiskelijat[nimi][i][1]
            kurssit += 1
        keskiarvo = summa / kurssit
        ka.append(keskiarvo)
        if keskiarvo > ka_max:
            ka_max = keskiarvo
            opiskelija_max = nimi
        if len(opiskelijat[nimi]) > suoritus_max:
            suoritus_max = kurssit
            suorittaja_max = nimi   
    print("eniten suorituksia",suoritus_max,suorittaja_max)
    print("paras keskiarvo", ka_max, opiskelija_max)
