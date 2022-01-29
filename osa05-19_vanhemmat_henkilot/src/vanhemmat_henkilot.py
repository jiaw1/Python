# tee ratkaisu tänne

def vanhemmat(henkilot: list, vuosi: int):
    vanhimmat = []
    for i in henkilot:
        if i[1] < vuosi:
            vanhimmat.append(i[0])
    return vanhimmat
