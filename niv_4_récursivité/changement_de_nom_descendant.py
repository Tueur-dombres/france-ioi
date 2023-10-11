L = int(input())
lettres = input()
N = int(input())
pos_lettre = {lettres[i]:i for i in range(L)}

def choisir(nbLettres,choix):
    global lettres
    if nbLettres == 0:
        print("".join(choix))
    else:
        for lettre in lettres:
            choisir(nbLettres-1,choix+[lettre])

print(L**N)
choisir(N,[])