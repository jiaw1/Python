# tee ratkaisu tänne

def ilman_vokaaleja(mjono: str):
    vokaalit = "aeiouyåäö"
    mjono_uusi = ''
    for i in mjono:
        if i not in vokaalit:
            mjono_uusi += i
    return mjono_uusi
