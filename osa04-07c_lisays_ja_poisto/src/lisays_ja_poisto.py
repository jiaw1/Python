# Kirjoita ratkaisu tähän

lista = []

while True:
    print(f"Lista on nyt {lista}")
    komento = input("(l)isää, (p)oista vai e(x)it:")
    if komento == "l":
        lista.append(len(lista)+1)
    elif komento == "p":
        lista.pop(len(lista)-1)
    elif komento == "x":
        break
print("Moi!")
