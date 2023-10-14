L,H,M = map(int,input().split())
changements_murs = {}
for _ in range(M):
    X1,Y1,X2,Y2 = map(int,input().split())
    hauteur = Y2-Y1
    if X1 in changements_murs:
        changements_murs[X1] = changements_murs[X1] + hauteur
    else:
        changements_murs[X1] = hauteur
    
    if X2 in changements_murs:
        changements_murs[X2] = changements_murs[X2] - hauteur
    else:
        changements_murs[X2] = -hauteur

changements_murs = sorted([(k,v) for k,v in changements_murs.items()]+[(L,0)], key = lambda x:x[0])

mini = H
current_epaisseur = 0
for X,diff in changements_murs:
    if X!=0 and current_epaisseur < mini:
        mini = current_epaisseur
    if X == L:
        if current_epaisseur < mini:
            mini = current_epaisseur
        break
    current_epaisseur+=diff
print(mini)