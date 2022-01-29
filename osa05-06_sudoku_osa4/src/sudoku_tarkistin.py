# tee ratkaisu tänne

def rivi_oikein(sudoku: list, rivi_nro: int):
    rivi = []
    for i in sudoku[rivi_nro]:
        if i != 0 and i in rivi:
            return False
        else:
            rivi.append(i)
    return True

def sarake_oikein(sudoku: list, sarake_nro: int):
    sarake = []
    for i in sudoku:
        if i[sarake_nro] != 0 and i[sarake_nro] in sarake:
            return False
        else:
            sarake.append(i[sarake_nro]) 
    return True

def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int):
    tulos = []
    for i in range(rivi_nro, rivi_nro+3):
        for j in range(sarake_nro, sarake_nro+3):
            if sudoku[i][j] != 0 and sudoku[i][j] in tulos:
                return False
            else:
                tulos.append(sudoku[i][j])
    return True

def sudoku_oikein(sudoku: list):
    neliot = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
    tulos = []
    rivi = 0
    sarake = 0
    i = 0

    while rivi < 9:
        tulos.append(rivi_oikein(sudoku, rivi))
        rivi += 1

    while sarake < 9:
        tulos.append(sarake_oikein(sudoku, sarake))
        sarake += 1

    while i < 9:
        tulos.append(nelio_oikein(sudoku, neliot[i][0], neliot[i][1]))
        i += 1
    print(tulos)

    for j in tulos:
        if j is False:
            return False       
    return True

def sudoku_oikein(sudoku: list):
    for rivi in range(0,9):
        if not rivi_oikein(sudoku, rivi):
            return False
 
    for sarake in range(0,9):
        if not sarake_oikein(sudoku, sarake):
            return False
 
    for rivi in range(0,9,3):
        for sarake in range(0,9,3):
            if not nelio_oikein(sudoku, rivi, sarake):
                return False
 
    return True