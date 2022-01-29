# tee ratkaisu tänne

def vanhin(henkilot: list):
    vanhin = []
    for i in henkilot:
        vanhin.append(i[1])
    
    hakusana = min(vanhin)
    for i in henkilot:
        if hakusana == i[1]:
            return i[0]
