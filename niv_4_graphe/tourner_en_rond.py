N,A = input().split()
N,A = int(N),int(A)
noeuds_adjacents = {str(i):[] for i in range(1,N+1)}
for _ in range(A):
    n1,n2 = input().split()
    noeuds_adjacents[n1]+=[n2]

def recherche(point,boucle):
    for chemin in noeuds_adjacents[point]:
        if boucle[chemin]:return True
        boucle[chemin]=True
        return recherche(chemin,boucle)
    return False
print("OUI" if recherche("1",{str(i):False for i in range(1,N+1)}) else "NON")