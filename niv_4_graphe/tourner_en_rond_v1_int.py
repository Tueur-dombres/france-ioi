N,A = input().split()
N,A = int(N),int(A)
noeuds_adjacents = [[] for _ in range(N+1)]
for _ in range(A):
    n1,n2 = input().split()
    noeuds_adjacents[int(n1)]+=[int(n2)]

def recherche(point,boucle):
    for chemin in noeuds_adjacents[point]:
        if boucle[chemin]:return True
        boucle[chemin]=True
        return recherche(chemin,boucle)
    return False
print("OUI" if recherche(1,[[] for _ in range(N+1)]) else "NON")