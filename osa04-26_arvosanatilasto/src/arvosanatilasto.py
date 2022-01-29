# Kirjoita ratkaisu tähän

pistetaulukko = []

while True:
    pistemaara = input("Koepisteet ja harjoitusten määrä: ")
    if pistemaara == "":
        break
    pisteet = pistemaara.split(" ")
    pistetaulukko.append(int(pisteet[0]))
    pistetaulukko.append(int(pisteet[1]) // 10)

i = 0
tahdet = ["","","","","",""]

while True:
    if i >= len(pistetaulukko):
        break
    if pistetaulukko[i] >= 10:
        if  pistetaulukko[i] + pistetaulukko[i+1] >= 28:
            tahdet[0] +="*"
        elif pistetaulukko[i] + pistetaulukko[i+1] >= 24:
            tahdet[1] += "*"
        elif pistetaulukko[i] + pistetaulukko[i+1] >= 21:
            tahdet[2] += "*"
        elif pistetaulukko[i] + pistetaulukko[i+1] >= 18:
            tahdet[3] += "*"
        elif pistetaulukko[i] + pistetaulukko[i+1] >= 15:
            tahdet[4] += "*"
        else:
            tahdet[5] += "*"
    else:
        tahdet[5] += "*"
    i +=2

keskiarvo = f"{2*sum(pistetaulukko)/len(pistetaulukko):.1f}"
if sum(pistetaulukko) > 0:
    hyvaksymisprosentti = f"{100 * (1 - len(tahdet[5])/(len(tahdet[0]+tahdet[1]+tahdet[2]+tahdet[3]+tahdet[4]+tahdet[5] ))):.1f}"

print("Tilasto:")
print(f"Pisteiden keskiarvo: {keskiarvo}")
print(f"Hyväksymisprosentti: {hyvaksymisprosentti}")
print("Arvosanajakauma:")
print(f"  5: {tahdet[0]}")
print(f"  4: {tahdet[1]}")
print(f"  3: {tahdet[2]}")
print(f"  2: {tahdet[3]}")
print(f"  1: {tahdet[4]}")
print(f"  0: {tahdet[5]}")
