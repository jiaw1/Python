# Kirjoita ratkaisu tähän
nimi = str(input("Anna nimesi:"))

#Aku ankan veljenpojat:
tupu = "Tupu"
hupu = "Hupu"
lupu = "Lupu"

#Mikki Hiiren veljenpojat:
mortti = "Mortti"
vertti = "Vertti"

if nimi == tupu or nimi == hupu or nimi == lupu:
    print("Olet luultavasti Aku Ankan veljenpoika.")
elif nimi == mortti or nimi == vertti:
    print("Olet luultavasti Mikki Hiiren veljenpoika.")
else:
    print("Et ole kenenkään tuntemani hahmon veljenpoika.")
