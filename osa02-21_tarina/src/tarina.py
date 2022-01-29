# Kirjoita ratkaisu tähän
tarina = ""
edellinen = ""

while True:
    sana = input("anna sana:")
    if sana == "loppu" or sana == edellinen:
        break
    tarina += sana + " "
    edellinen = sana
 
print(tarina)
