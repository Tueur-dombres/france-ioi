N = int(input())
Ks = list(map(int,input().split()))

arbre = {i:[] for i in range(N+1)}
for i in range(1,N+1):
    arbre[Ks[i-1]]+=[i]

racines = arbre[0].copy()
d_max = 0
while racines:
    new_row = []
    for elt in racines:
        new_row += arbre[elt]
    racines = new_row.copy()
    d_max+=1
print(d_max)