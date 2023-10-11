N,A = map(int,input().split())
liste_adjacences = [[] for _ in range(N)]

if A:
    n1,n2 = map(int,input().split())
    liste_adjacences[n1-1] += [n2-1]
    liste_adjacences[n2-1] += [n1-1]
    noeud_in_graphe = n1
    for _ in range(A-1):
        n1,n2 = map(int,input().split())
        liste_adjacences[n1-1] += [n2-1]
        liste_adjacences[n2-1] += [n1-1]

nb_impair = 0
degrés  = []
for adjacent in liste_adjacences:
    degrés += [len(adjacent)]
    if degrés[-1] % 2 :
        nb_impair += 1

if nb_impair != 0:
    print(-1)
else:
    def Euler(x):
        global liste_adjacences
        cycle = [x]
        if not liste_adjacences[x]:
            return cycle
        else:
            y = x
            while liste_adjacences[y]:
                z=liste_adjacences[y].pop(0)
                liste_adjacences[z].pop(liste_adjacences[z].index(y))
                y=z
                cycle += [y]
        return [elt for e in cycle for elt in Euler(e)]
    print(" ".join([str(e+1) for e in Euler(noeud_in_graphe)]))
    