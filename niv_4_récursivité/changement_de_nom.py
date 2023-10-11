L = int(input())
lettres = input()
N = int(input())

def noms(taille):
    if taille == 1:
        return lettres
    return [l+e for l in lettres for e in noms(taille-1)]


print(L**N)
for mot in noms(N):
    print(mot)
   