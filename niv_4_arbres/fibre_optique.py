nbNoeuds = int(input())
nbConnexions = nbNoeuds-1
couples = [list(map(int,input().split())) for _ in range(nbConnexions)]
connexions_du_noeud = [[] for _ in range(nbNoeuds)]
for n1,n2 in couples:
    connexions_du_noeud[n1] += [n2]
    connexions_du_noeud[n2] += [n1]

weights = [1 for _ in range(nbNoeuds)]
weights_connexions = []

while len(weights_connexions)<nbConnexions:
    i_noeuds_plein = []
    for i,voisins in enumerate(connexions_du_noeud):
        if len(voisins) == 1:
            i_noeuds_plein += [i]
    print(weights)
    print(connexions_du_noeud)
    print(weights_connexions)
    print(i_noeuds_plein)
    for i_noeud in i_noeuds_plein:
        print(i_noeud,connexions_du_noeud[i_noeud],connexions_du_noeud[connexions_du_noeud[i_noeud][0]])
        weights[connexions_du_noeud[i_noeud][0]]+=weights[i_noeud]
        weights_connexions += [max(weights[i_noeud],nbNoeuds-weights[i_noeud])]
        connexions_du_noeud[connexions_du_noeud[i_noeud][0]].pop(connexions_du_noeud[connexions_du_noeud[i_noeud][0]].index(i_noeud))
        connexions_du_noeud[i_noeud] = []
print(weights_connexions)