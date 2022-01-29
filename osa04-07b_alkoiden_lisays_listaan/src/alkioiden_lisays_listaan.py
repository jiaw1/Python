# Kirjoita ratkaisu tähän

lukuja = int(input("Kuinka monta lukua: "))
lista = []
 
while len(lista) < lukuja:
    luku = int(input(f"Anna luku {len(lista) + 1}: "))
    lista.append(luku)
 
print(lista)
