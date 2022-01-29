# Kirjoita ratkaisu tähän
lampotila = int(input("Lämpötila:"))
sataa = input("Sataako (kyllä/ei):")

if lampotila > 20 and sataa == "kyllä":
    print("Pue housut ja t-paita")
    print("Muista sateenvarjo!")
elif lampotila > 10 and sataa == "kyllä":
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")
    print("Muista sateenvarjo!")
elif lampotila > 5 and sataa == "kyllä":
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")
    print("Pue päälle takki")
    print("Suosittelen lämmintä takkia")
elif lampotila <= 5 and sataa == "kyllä":
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")
    print("Pue päälle takki")
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")
    print("Muista sateenvarjo!")

if lampotila > 20 and sataa == "ei":
    print("Pue housut ja t-paita")
elif lampotila > 10 and sataa == "ei":
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")
elif lampotila > 5 and sataa == "ei":
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")
    print("Pue päälle takki")
elif lampotila <= 5 and sataa == "ei":
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")
    print("Pue päälle takki")
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")
