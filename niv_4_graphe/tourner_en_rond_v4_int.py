from sys import setrecursionlimit
N,A = input().split()
N,A = int(N),int(A)
setrecursionlimit(N+50)
noeuds_adjacents = [[] for _ in range(N+1)]
for _ in range(A):
    n1,n2 = input().split()
    noeuds_adjacents[int(n1)]+=[int(n2)]
vus = [[] for _ in range(N+1)]
def recherche(point,boucle):
    vus[point]=True
    boucle[point]=True
    for chemin in noeuds_adjacents[point]:
        if not vus[chemin] and recherche(chemin,boucle):return True
        elif boucle[chemin]:return True
    boucle[point]=False
    return False
print("OUI" if recherche(1,[[] for _ in range(N+1)]) else "NON")