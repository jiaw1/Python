# tee ratkaisu tänne

def rivi_oikein(sudoku: list, rivi_nro: int):
    rivi = []
    for i in sudoku[rivi_nro]:
        if i != 0 and i in rivi:
            return False
        else:
            rivi.append(i)
    return True
