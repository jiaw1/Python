# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti

def vaihteluvali(lista):
    erotus = max(lista)-min(lista)
    return erotus

if __name__ == "__main__":
    lista = [3, 6, -4]
    tulos = vaihteluvali(lista)
    print(tulos)
