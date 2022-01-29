# tee ratkaisu tähän
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    tulosta_monesti("python", 5)

def tulosta_monesti(merkkijono, kertaa):
    while kertaa > 0:
        print(merkkijono)
        kertaa -= 1
    
if __name__ == "__main__":
    tulosta_monesti("python", 5)
