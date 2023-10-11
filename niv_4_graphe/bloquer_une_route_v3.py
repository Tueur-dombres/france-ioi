from sys import setrecursionlimit
nbIntersections,nbSentiers = map(int,input().split())
setrecursionlimit(nbIntersections+50)
adjacents = [[] for _ in range(nbIntersections)]
for _ in range(nbSentiers):
    n1,n2 = map(int,input().split())
    adjacents[n1-1]+=[n2-1]
    adjacents[n2-1]+=[n1-1]

noeuds_vus = [False for _ in range(nbIntersections)]
i_prof = [0]*nbIntersections
rang = 0
T_arcs = [[] for _ in range(nbIntersections)]
G_T_arcs = [[] for _ in range(nbIntersections)]
arcs_vus = [[False]*nbIntersections for _ in range(nbIntersections)]
plus_bas = [0]*nbIntersections

#parcours en profondeur
def parcour(point):
    global noeuds_vus,i_prof,rang,T_arcs,G_T_arcs,arcs_vus,plus_bas
    rang+=1
    i_prof[point]=rang
    noeuds_vus[point]=True
    for chemin in adjacents[point]:
        if noeuds_vus[chemin]:
            if not arcs_vus[max(chemin,point)][min(chemin,point)]:
                G_T_arcs[point] += [chemin]
        else:
            if not arcs_vus[max(chemin,point)][min(chemin,point)]:
                arcs_vus[max(chemin,point)][min(chemin,point)] = True
                T_arcs[point] += [chemin]
                parcour(chemin)
    plus_bas[point]=min([i_prof[point]]+[i_prof[y] for y in G_T_arcs[point]]+[plus_bas[t] for t in T_arcs[point]])
parcour(0)

isthmes = []
for x,ys in enumerate(T_arcs):
    for y in ys:
        if i_prof[x]<plus_bas[y]:
            isthmes+=[sorted([x+1,y+1])]
ithmes = sorted(isthmes)
print(len(isthmes))
print("\n".join(str(n1)+" "+str(n2) for n1,n2 in isthmes))