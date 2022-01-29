# Kirjoita ratkaisu tähän
asti = int(input("Mihin asti: "))
luku = 1
summa = 1
luvut = "1"
while summa < asti:
    luku += 1
    summa += luku
    luvut += f" + {luku}" 
print(f"Laskettiin {luvut} = {summa}")
