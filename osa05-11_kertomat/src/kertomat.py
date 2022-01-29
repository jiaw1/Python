# tee ratkaisu tänne

def kertomat(n: int):
    sanakirja = {}
    kertoma = 1
    i = 1
    while i<=n:
        kertoma *= i
        sanakirja[i] = kertoma
        i += 1
    return sanakirja

def kertomat(n: int):
    tulos = {}
    tulos[1] = 1
    for i in range(2, n + 1):
        tulos[i] = tulos[i-1] * i
    return tulos
