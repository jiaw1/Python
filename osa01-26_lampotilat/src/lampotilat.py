# Kirjoita ratkaisu tähän
lampotila = int(input("Anna lämpötila (F):"))
celsius = (lampotila-32)/1.8

print(f"{lampotila} fahrenheit-astetta on {celsius} celsius-astetta")

if celsius < 0:
    print("Paleltaa!")
