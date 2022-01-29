# tee ratkaisu tänne

def lue_hedelmat():
    
    with open('hedelmat.csv') as tiedosto:

        sanakirja = {}

        for rivi in tiedosto:

            rivit = rivi.replace('\ln','')
            osat = rivi.split(';')
            hedelma = osat[0]
            hinta = float(osat[1])
            sanakirja[hedelma] = hinta 
       
    return sanakirja
