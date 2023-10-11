from math import factorial
def arrangements (n,k):
    if n == 0 or k > n :return 0
    return factorial(n)//factorial(abs(n-k))
L = int(input())
lettres = input()
N = int(input())
pos_lettre = {lettres[i]:i for i in range(L)}

def choisir(nbLettres,choix,choisis):
    global lettres
    if nbLettres == 0:
        print("".join(choix))
    else:
        for lettre in lettres:
            if not choisis[pos_lettre[lettre]]:
                choisis[pos_lettre[lettre]] = True
                choisir(nbLettres-1,choix+[lettre],choisis)
                choisis[pos_lettre[lettre]] = False

print(arrangements(L,N))
choisir(N,[],[False]*L)