# tee ratkaisu tänne
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!

def palindromi(sana: str):
    if sana[0:] == sana[::-1]:
        return True
    else:
        return False

while True:
    sana = input("Anna sana: ")
    if palindromi(sana) == True:
        print(f"{sana} on palindromi!")
        break
    elif palindromi(sana) == False:
        print(f"ei ollut palindromi")
