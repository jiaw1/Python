# tee ratkaisu tänne

def transponoi(matriisi: list):
    transpoosi = [[matriisi[i][j] for i in range(len(matriisi))] for j in range(len(matriisi[0]))]

    for i in range(len(matriisi)):
        for j in range(len(matriisi[0])):
            matriisi[j][i] = transpoosi[j][i]

def transponoi(matriisi: list):
    n = len(matriisi)
    for i in range(n):
        for j in range(i, n):
            temp = matriisi[i][j]
            matriisi[i][j] = matriisi[j][i]
            matriisi[j][i] = temp
