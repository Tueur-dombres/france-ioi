N,A = map(int,input().split())
noeuds_adjacents = [[] for _ in range(N+1)]
for _ in range(A):
    n1,n2,d = map(int,input().split())
    noeuds_adjacents[n1]+=[n2]
    noeuds_adjacents[n2]+=[n1]
noeuds_visites = [False for _ in range(N+1)]
graphes = []
for noeud in range(1,N+1):
    if not noeuds_visites[noeud]:
        noeuds_visites[noeud] = True
        noeuds_dans_le_graphe = [noeud]
        i = 0
        graphe_size = 1
        while i < len(noeuds_dans_le_graphe):
            for noeud_suivant in noeuds_adjacents[noeuds_dans_le_graphe[i]]:
                if not noeuds_visites[noeud_suivant]:
                    noeuds_visites[noeud_suivant] = True
                    noeuds_dans_le_graphe+=[noeud_suivant]
                    graphe_size+=1
            i+=1
        graphes+=[graphe_size]
print(len(graphes),max(graphes))
