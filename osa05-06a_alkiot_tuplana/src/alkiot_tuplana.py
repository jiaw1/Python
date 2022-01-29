# tee ratkaisu tänne

def tuplaa_alkiot(luvut):
    tupla = []
    for i in luvut:
        tupla.append(i*2)
    return tupla

def tuplaa_alkiot(luvut: list):
    tupla = luvut[:]
    for i in range(len(tupla)):
        tupla[i] *= 2
    
    return tupla

if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)
