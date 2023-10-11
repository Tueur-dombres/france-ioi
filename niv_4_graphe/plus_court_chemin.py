L,C = map(int,input().split())
lab = [[1]*(C+2)]+[[1]+[1 if e=="#" else 0 for e in input()]+[1] for _ in range(L)]+[[1]*(C+2)]
row = [[2,1]] #y,x
E,N,O,S = 1,2,3,4
lab[2][1] = 1
while not lab[L][C-1]:
    row_suivante = []
    for y,x in row:
        for dir,dy,dx in (E,0,1),(N,-1,0),(O,0,-1),(S,1,0):
            if not lab[y+dy][x+dx]:
                lab[y+dy][x+dx] = dir
                row_suivante += [[y+dy,x+dx]]
    row = row_suivante

etapes = ""
pos = (L,C-1)
while pos != (2,1):
    y,x = pos
    etapes = "ENOS"[lab[y][x]-1] + etapes
    dy,dx = [(0,-1),(1,0),(0,1),(-1,0)][lab[y][x]-1]
    pos = (y+dy,x+dx)
print(len(etapes))
print(etapes)