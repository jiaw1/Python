# Kirjoita ratkaisu tähän
sana = input("Sana: ")
 
print("*" * 30)
alkuvalit = (28 - len(sana)) // 2
loppuvalit = alkuvalit

if len(sana) % 2 != 0:
    loppuvalit += 1
 
print("*" + alkuvalit * " " + sana + loppuvalit * " " + "*")
print("*" * 30)
