# Kirjoita ratkaisu tähän
kerta = int(input("Montako kertaa viikossa syöt Unicafessa?"))
hinta = float(input("Unicafe-lounaan hinta:"))
kulut = float(input("Paljonko käytät viikossa ruokaostoksiin? \n"))

print("Kustannukset keskimäärin:")
print(f"Päivässä {((hinta*kerta)+kulut)/7} euroa")
print(f"Viikossa {(hinta*kerta)+kulut} euroa")
