# tee ratkaisu tänne

def joulukuusi(koko):
    print("joulukuusi!")
    i = 1
    while i<=koko:
        vali = " "*(koko-i)
        tahti = "*"*(2*i-1)
        print(vali+tahti)
        i += 1
    print((koko-1)*" "+"*")
