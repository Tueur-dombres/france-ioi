L,C = map(int,input().split())
labyrinthe = [[True if e == "#" else False for e in input()] for _ in range(L)]
labyrinthe[1][0] = True
def nb_chemins_vers_sortie(x,y):
    global labyrinthe
    if (x,y) == (L-2,C-1):
        return 1
    labyrinthe[y][x] = True
    retour = 0
    for xi,yi in ((-1,0),(1,0),(0,-1),(0,1)):
        if not labyrinthe[y+yi][x+xi]:
            retour+=nb_chemins_vers_sortie(x+xi,y+yi)
    labyrinthe[y][x] = False
    return retour
print(nb_chemins_vers_sortie(1,1))