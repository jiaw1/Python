# Kirjoita ratkaisu tähän
k1 = input("Anna 1.kirjain:")
k2 = input("Anna 2.kirjain:")
k3 = input("Anna 3.kirjain:")

if k1<k2<k3 or k3<k2<k1:
    print(f"Keskimmäinen kirjain on {k2}")
elif k3<k1<k2 or k2<k1<k3:
    print(f"Keskimmäinen kirjain on {k1}")
elif k1<k3<k2 or k2<k3<k1:
    print(f"Keskimmäinen kirjain on {k3}")
