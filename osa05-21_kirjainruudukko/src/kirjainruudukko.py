# Kirjoita ratkaisu tähän

kerrokset = int(input("Kerrokset: "))
aakkoset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
vasen = ""
oikea = ""
i = kerrokset-1
j = 2*kerrokset-1

while i >= 1:
    vasen = vasen+aakkoset[i]
    oikea = aakkoset[i]+oikea
    j -= 2
    print(vasen+aakkoset[i]*j+oikea)
    i -= 1

while i <= kerrokset-1:
    print(vasen+aakkoset[i]*j+oikea)
    vasen = vasen[:-1]
    oikea = oikea[1:]
    j += 2
    i += 1
 