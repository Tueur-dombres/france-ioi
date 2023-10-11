L = int(input())
lettres = input()
N = int(input())

def noms(taille):
    global lettres
    if taille == 1:
        return lettres
    elif taille%2:
        precedent = noms((taille-1)//2)
        return [a+e+l for l in lettres for a in precedent for e in precedent]
    else:
        precedent = noms(taille//2)
        return [a+e for a in precedent for e in precedent]


print(L**N)
for mot in noms(N):
    print(mot)