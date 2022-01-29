# Kirjoita ratkaisu tähän
aloitusvuosi = int(input("Vuosi: "))
vuosi = aloitusvuosi + 1

while True:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            break
    elif vuosi % 4 == 0:
        break
    vuosi += 1
 
print(f"Vuotta {aloitusvuosi} seuraava karkausvuosi on {vuosi}")
