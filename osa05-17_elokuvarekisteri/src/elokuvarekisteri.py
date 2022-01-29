# tee ratkaisu tänne

def lisaa_elokuva(rekisteri: list, nimi: str, ohjaaja: str, vuosi: int, pituus: int):
    elokuva = {"nimi": nimi, "ohjaaja": ohjaaja, "vuosi": vuosi, "pituus": pituus}
    rekisteri.append(elokuva)
