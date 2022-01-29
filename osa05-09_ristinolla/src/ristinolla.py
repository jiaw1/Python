# tee ratkaisu tänne

def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
    if x not in (0,1,2) or y not in (0,1,2):
        return False
    elif lauta[y][x] == "":
        lauta[y][x] = nappula
        return True
    else:
        return False

if __name__ == "__main__":
    lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(pelaa_siirto(lauta,  0, 1, "X"))
    print(lauta)
