# tee ratkaisu tänne

def samat(merkkijono, merkki1, merkki2):
    if merkki1>=len(merkkijono) or merkki2>=len(merkkijono):
        return False
    elif merkki1<len(merkkijono) or merkki2<len(merkkijono):
        if merkkijono[merkki1] == merkkijono[merkki2]:
            return True
        else:
            return False
