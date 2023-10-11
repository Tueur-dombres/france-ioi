L,C = map(int,input().split())
labyrinthe = [[True if e == "#" else False for e in input()] for _ in range(L)]+[[True for _ in range(C)]]
nbvides = sum(e.count(False) for e in labyrinthe)
current_cases = [(0,1)]
labyrinthe[1][0] = True
cps = 0
while current_cases:
    cases_suivantes = []
    for x,y in current_cases:
        for xi,yi in ((-1,0),(1,0),(0,-1),(0,1)):
            if not labyrinthe[y+yi][x+xi]:
                cases_suivantes += [(x+xi,y+yi)]
                labyrinthe[y+yi][x+xi] = True
        cps+=1        
    current_cases = cases_suivantes.copy()
print(nbvides-cps)
