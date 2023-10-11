from random import randint
nb = int(input())
L = [list(map(int,input().split()))for _ in range(nb)]
"""
L = []
for i in range(nb):
    a = randint(0,500000)
    b = randint(a,500000)
    L+=[[a,b]]
"""
#print(L)
L_size = []
for x in L:
    if x[1]-x[0] not in L_size:
        L_size += [x[1]-x[0]]
L_size.sort()
nb_size = len(L_size)
Ls = {i:[] for i in L_size}

for x in L:
    Ls[x[1]-x[0]]+=[x]
Ls = {k:sorted(v) for k,v in Ls.items()}
L = []
cp_max = 0
#print()
#print(Ls)
for k,v in Ls.items():
    L = sorted(L+v)
    for j in range(len(v)):
        cp = -1
        k=0
        #print(L)
        while k < len(L) and v[j][0]>L[k][0]:
            #print(v[j],L[k])
            k+=1
        #print("pass")
        while k < len(L) and v[j][1]>=L[k][0]:
            #print(v[j],L[k])
            if v[j][1]>=L[k][1]:
                cp+=1
            k+=1
            #print("cp", cp)
        if cp>cp_max:cp_max = cp
print(cp_max)