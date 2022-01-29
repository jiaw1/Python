# Kirjoita ratkaisu tähän
piste = int(input("Anna pisteet [0-100]:"))

if piste < 0 or piste > 100:
    print("Arvosana: mahdotonta!")
elif 0 <= piste <= 49:
    print("Arvosana: hylätty")
elif 50 <= piste <= 59:
    print("Arvosana: 1")
elif 60 <= piste <= 69:
    print("Arvosana: 2")
elif 70 <= piste <= 79:
    print("Arvosana: 3")
elif 80 <= piste <= 89:
    print("Arvosana: 4")
elif 90 <= piste <= 100:
    print("Arvosana: 5")
