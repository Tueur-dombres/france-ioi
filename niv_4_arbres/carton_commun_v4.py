N = int(input())
Ks = list(map(int,input().split()))
R = int(input())
Rs = [list(map(int,input().split())) for _ in range(R)]

arbre = [[] for _ in range(N+1)]
vus_dans_Rs = [False for _ in range(N+1)]
row_actu = []
for o1,o2 in Rs:
    if  not vus_dans_Rs[o1]:
        vus_dans_Rs[o1] = True
        row_actu += [o1]
    if  not vus_dans_Rs[o2]:
        vus_dans_Rs[o2] = True
        row_actu += [o2]

vus_dans_larbre = [False for _ in range(N+1)]
vus_dans_larbre[0] = True
for e in row_actu:
    vus_dans_larbre[e] = True 
while row_actu:
    row_suivante = []
    for e in row_actu:
        arbre[Ks[e-1]]+=[e]
        if not vus_dans_larbre[Ks[e-1]]:
            vus_dans_larbre[Ks[e-1]] = True
            row_suivante += [Ks[e-1]]
    row_actu = row_suivante.copy()


distances = {}
d_actuelle = 0
current_row = [0]
while current_row:
    suivante_row = []
    for e in current_row:
        if vus_dans_Rs[e]:
            distances[e] = d_actuelle
        suivante_row += arbre[e]
    current_row = suivante_row.copy()
    d_actuelle+=1

for o1,o2 in Rs:
    if distances[o1]>distances[o2]:
        for i in range(distances[o1]-distances[o2]):
            o1 = Ks[o1-1]
    else:
        for i in range(distances[o2]-distances[o1]):
            o2 = Ks[o2-1]
    while o2!=o1:
        o1 = Ks[o1-1]
        o2 = Ks[o2-1]
    print(o1)