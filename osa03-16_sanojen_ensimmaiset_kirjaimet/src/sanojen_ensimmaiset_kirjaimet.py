# Kirjoita ratkaisu tähän
lause = input("Anna lause: ")

lause = " " + lause

kohta = 1
while kohta < len(lause):
    if lause[kohta-1] == " " and lause[kohta] != " ":
        print(lause[kohta])
    kohta += 1
