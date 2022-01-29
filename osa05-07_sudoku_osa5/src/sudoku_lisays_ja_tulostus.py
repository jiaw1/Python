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
 
def lisays(sudoku: list, rivi: int, sarake: int, luku: int):
    sudoku[rivi][sarake] = luku

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
    
    tulosta(sudoku)
    lisays(sudoku, 0, 0, 2)
    lisays(sudoku, 1, 2, 7)
    lisays(sudoku, 5, 7, 3)
    print()
    print("Kolme numeroa lisätty:")
    print()
    tulosta(sudoku)
    print()
