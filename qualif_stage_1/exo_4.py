def dicho(L, elt):
    a = 0
    b = len(L)
    while b > a + 1:
        m = (a + b) // 2
        if L[m] > elt:
            b = m
        else:
            a = m
    return a
"""
from random import shuffle
N,Q = 10,0
L_originale = [i for i in range(1,N+1)]
shuffle(L_originale)
print(L_originale)
"""
N,Q = map(int,input().split())
L_originale = list(map(int,input().split()))
Qs = [input() for i in range(Q)]

tours = 0
L_passé = []
for j in range(N):
    if L_originale[j]==N:
        pos_max=j
    if L_originale[j]==1:
        L_passé = [1]+L_passé
    elif L_passé == []:
        tours+=1
        L_passé = [L_originale[j]]
    else:
        a = dicho(L_passé, L_originale[j])
        if not L_passé[a]==L_originale[j]-1:
            tours += 1
        L_passé = L_passé[:a+1]+[L_originale[j]]+L_passé[a+1:]
finish_t = tours
finish_p = pos_max
print(N*finish_t+finish_p)
for elt in Qs:
    inf,sup = map(int,elt.split())
    L_work = L_originale[inf-1:sup][::-1]
    L_modif = L_originale[:inf-1]+L_work+L_originale[sup:]
    L_sor_work = sorted(L_work)
    dico = {L_sor_work[i]:i+1 for i in range(len(L_work))}
    L_work = [dico[e]for e in L_work]
    tours = 0
    L_passé = []
    for j in range(len(L_work)):
        if L_work[j]==1:
            L_passé = [1]+L_passé
        elif L_passé == []:
            tours+=1
            L_passé = [L_work[j]]
        else:
            a = dicho(L_passé, L_work[j])
            if not L_passé[a]==L_work[j]-1:
                tours += 1
            L_passé = L_passé[:a+1]+[L_work[j]]+L_passé[a+1:]
    print((finish_t-len(L_work)+2*tours+1)*N+L_modif.index(N))
