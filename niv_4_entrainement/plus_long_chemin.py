L,C = map(int,input().split())
labyrinthe = [[1]*(C+2)] + [[1]+[1 if e == "#" else 0 for e in input()]+[1] for _ in range(L)] + [[1]*(C+2)]
L+=2;C+=2

for e in labyrinthe:print(e)
print((C-2,L-1))
def nb_chemins_vers_sortie(x,y,chemin):
    print("appel",x,y,chemin)
    global labyrinthe
    if (x,y) == (C-3,L-2):
        return [[len(chemin),chemin]]
    labyrinthe[y][x] = True
    retour = []
    for xi,yi,dir in ((1,0,"E"),(0,-1,"N"),(-1,0,"O"),(0,1,"S")):
        if not labyrinthe[y+yi][x+xi]:
            retour+=nb_chemins_vers_sortie(x+xi,y+yi,chemin+[dir])
    labyrinthe[y][x] = False
    print("retour",x,y,retour)
    return retour
plus_long = max(nb_chemins_vers_sortie(1,2,[]), key = lambda x:x[0])
print(plus_long[0])
print("".join(plus_long[1]))