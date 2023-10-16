N, R = map(int,input().split())
visiteurs = [0]+list(map(int,input().split()))
intervalles = [list(map(int,input().split()))+[i] for i in range(R)]
intervalles_tries = sorted(intervalles)

valeurs_actuelle = visiteurs[0]
D_actuel, F_actuel = 0, 0
for inter in intervalles_tries:
    D_suivant, F_suivant, pos = inter
    valeurs_actuelle -= sum(visiteurs[D_actuel:D_suivant])
    if D_suivant>F_actuel:
        valeurs_actuelle = sum(visiteurs[D_suivant:F_suivant+1])
    elif F_suivant > F_actuel:
        valeurs_actuelle += sum(visiteurs[F_actuel+1:F_suivant+1])
    else:
        valeurs_actuelle -= sum(visiteurs[F_suivant+1:F_actuel+1])
    
    D_actuel, F_actuel = D_suivant, F_suivant
    intervalles[pos] = valeurs_actuelle

for inter in intervalles:
    print(inter)