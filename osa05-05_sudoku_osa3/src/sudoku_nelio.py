# tee ratkaisu tänne

def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int):
    tulos = []
    for i in range(rivi_nro, rivi_nro+3):
        for j in range(sarake_nro, sarake_nro+3):
            if sudoku[i][j] != 0 and sudoku[i][j] in tulos:
                return False
            else:
                tulos.append(sudoku[i][j])
    return True
