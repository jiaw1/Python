# Kirjoita ratkaisu tähän
sana = input("Anna sana: ")
if len(sana) > 1 and sana[1] == sana[-2]:
    print("Toinen ja toiseksi viimeinen kirjain on " + sana[1])
else:
    print("Toinen ja toiseksi viimeinen kirjain eroavat")
 
