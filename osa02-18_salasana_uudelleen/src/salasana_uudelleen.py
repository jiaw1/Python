# Kirjoita ratkaisu tähän
salasana1 = str(input("Salasana:"))

while True:
    salasana2 = str(input("Toista salasana:"))
    if salasana1 == salasana2:
        print("Käyttäjätunnus luotu!")
        break
    elif salasana1 != salasana2:
        print("Ei ollut sama!")

