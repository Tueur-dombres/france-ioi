N,A = map(int,input().split())
nb_before = [0]*N
noeuds_suivants=[[]for _ in range(N)]

for _ in range(A):
    n1,n2 = map(int,input().split())
    nb_before[n2-1]+=1
    noeuds_suivants[n1-1]+=[n2-1]

pile = [i for i in range(N) if nb_before[i]==0]
cp = N
i = 0

while i<len(pile):
    noeud_actuel = pile[i]
    for noeud in noeuds_suivants[noeud_actuel]:
        nb_before[noeud] -= 1
        if nb_before[noeud] == 0:
            pile+=[noeud]
    i+=1
    cp-=1

if cp != 0:
    print(-1)
else:
    print(" ".join(str(e+1) for e in pile))