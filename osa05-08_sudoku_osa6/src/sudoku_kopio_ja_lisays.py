# tee ratkaisu tänne

def tulosta(sudoku: list):
    i = 0
    for rivi in sudoku:
        j = 0
        for luku in rivi:
            j += 1
            if luku == 0:
                luku = "_"
            tulos = f"{luku} "
            if j%3 == 0:
                tulos += " "
            print(tulos, end="")
 
        print()
        
        i += 1
        if i%3 == 0:
            print()

def kopioi_ja_lisaa(sudoku: list, rivi: int, sarake: int, luku: int):
    lisätty = []
    for k in sudoku:
        lisätty.append(k[:])
    lisätty[rivi][sarake] = luku
    return lisätty

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    kopio = kopioi_ja_lisaa(sudoku, 0, 0, 2)
    print("Alkuperäinen:")
    tulosta(sudoku)
    print()
    print("Kopio:")
    tulosta(kopio)
