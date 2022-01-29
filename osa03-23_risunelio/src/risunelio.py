# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)

def risunelio(koko):
    rivit = koko
    while rivit > 0:
        print("#" * koko)
        rivit -= 1
        
if __name__ == "__main__":
    risunelio(5)
