# tee ratkaisu tänne

def laske_alkiot(matriisi: list, alkio: int):
    alkiomaara = 0
    for i in matriisi:
        for j in i:
            if j == alkio:
                alkiomaara += 1
    return alkiomaara


if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))
