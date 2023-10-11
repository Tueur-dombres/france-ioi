N,A = map(int,input().split())
mat_adj = [[0]*N for _ in range(N)]
for _ in range(A):
    n1,n2 = map(int,input().split())
    mat_adj[n1-1][n2-1]=1

def estCyclique(matriceAdj, visites, u, pile):
    n = len(matriceAdj)
 
    visites[u] = True
    pile[u] = True
    for i in range(n):  # éléments adjacents
        if matriceAdj[u][i] > 0 and visites[i] == False:
            if estCyclique(matriceAdj, visites, i, pile):
                return True
 
        # si i est un element adjacent (matriceAdj[u][i] > 0)
        # i existe déjà dans la pile
        # i est déjà visité
        # donc il existe un cycle
        elif matriceAdj[u][i] > 0 and pile[i] == True and visites[i] == True:
            return True
 
    pile[u] = False
    return False


print("OUI" if estCyclique(mat_adj,[False]*N,0,[False]*N) else "NON")