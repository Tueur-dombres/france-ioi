L,C = map(int,input().split())
image = [[True for _ in range(C+2)]] + [[True]+[True if e == "#" else False for e in input()]+[True] for _ in range(L)]+[[True for _ in range(C+2)]]

def fill(x,y):
    image[y][x] = True
    for xi,yi in ((-1,0),(1,0),(0,-1),(0,1)):
        if not image[y+yi][x+xi]:
            fill(x+xi,y+yi)

cp_zones = 0
for y in range(L+2):
    for x in range(C+2):
        if not image[y][x]:
            cp_zones+=1
            fill(x,y)
        
print(cp_zones)