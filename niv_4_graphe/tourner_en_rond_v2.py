N,A = map(int,input().split())
mat_adj = [[0]*N for _ in range(N)]
for _ in range(A):
    n1,n2 = map(int,input().split())
    mat_adj[n1-1][n2-1]=1

def ExistChemin(matriceAdj, u, v):
    n = len(matriceAdj) # nombre de sommets
    file = []
    visites = [False] * n
    file.append(u)
    while file:
        courant = file.pop(0)
        visites[courant] = True
        for i in range(n):
            if matriceAdj[courant][i] > 0 and visites[i] == False:
                file.append(i)
                visites[i] = True
 
            # Si i est un noeud adjacent et égal à v (destination)
            # donc il existe un chemin de u à i
            elif matriceAdj[courant][i] > 0 and i == v:
                return True
    # pas de chemin entre u et v
    return False

def estCycle(matriceAdj):
    n = len(matriceAdj)
    for i in range(n):
        if ExistChemin(matriceAdj, i, i) == True:
            return True
    return False

print("OUI" if estCycle(mat_adj) else "NON")