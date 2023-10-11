N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]
L = sorted(L,key = lambda x:x[1]-x[0], reverse = True)
L_non_contenu = []
for e in L:
    found = False
    i = 0
    while i < len(L_non_contenu) and L_non_contenu[i][0] <= e[0]:
        if L_non_contenu[i][1]>=e[1]:
            found = True
            L_non_contenu[i][2]+=1
        i+=1
    if not found and len(L_non_contenu)<5:
        L_non_contenu=sorted(L_non_contenu+[e+[0]],key = lambda x:x[0])
print(max(L_non_contenu, key = lambda x:x[2])[2])