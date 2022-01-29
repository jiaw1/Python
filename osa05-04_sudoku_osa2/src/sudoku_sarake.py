# tee ratkaisu tänne

def sarake_oikein(sudoku: list, sarake_nro: int):
    sarake = []
    for i in sudoku:
        if i[sarake_nro] != 0 and i[sarake_nro] in sarake:
            return False
        else:
            sarake.append(i[sarake_nro]) 
    return True
