# tee ratkaisu tänne

def histogrammi(mjono):
    merkit = []
    for i in mjono:
        tahdet = i + " " + (mjono.count(i) * "*")
        if tahdet not in merkit:
            merkit.append(tahdet)
    
    for j in merkit:
        print(j)
