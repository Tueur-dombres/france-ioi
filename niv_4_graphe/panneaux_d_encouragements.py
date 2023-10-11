L,C = map(int,input().split())
lab = [[1]*(C+2)]+[[1]+[1 if e=="#" else 0 for e in input()]+[1] for _ in range(L)]+[[1]*(C+2)]
d_max = int(input())
row = [[L,C-1]]
lab[L][C-1]=True
panneaux = []
for i in range(d_max):
    row_suivante = []
    for y,x in row:
        for dy,dx in (-1,0),(1,0),(0,-1),(0,1):
            if not lab[y+dy][x+dx]:
                lab[y+dy][x+dx]=True
                row_suivante+=[[y+dy,x+dx]]
    panneaux+=[len(row_suivante)]
    row = row_suivante.copy()
print(" ".join(str(e) for e in panneaux))