from string import ascii_lowercase

hlbka = 3
vysledok = []
for i in range(hlbka):
    vysledok.append("a")

def genhesla(h=0):
    if h == hlbka:
        print(vysledok)
    else:
        for pis in ascii_lowercase:
            vysledok[h] = pis
            genhesla(h+1)

genhesla()

