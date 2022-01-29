# Kirjoita ratkaisu tähän
print("Syötä kokonaislukuja, 0 lopettaa:")
lukuja = 0
summa = 0
positiivisia = 0
 
while True:
    luku = int(input("luku: "))
    if luku == 0:
        break
    lukuja += 1
    summa += luku
    if luku>0:
        positiivisia += 1
 
print("Lukuja yhteensä", lukuja)
print("Lukujen summa", summa)
print("Lukujen keskiarvo", summa/lukuja)
print("Positiivisia", positiivisia)
print("Negatiivisia", lukuja-positiivisia)
