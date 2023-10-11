nb = int(input())
L = [list(map(int,input().split()))for _ in range(nb)]
L = sorted(sorted(L,key=lambda x:x[1],reverse=True),key=lambda x:x[0])
i=0
cps = []
while i <len(L)-1:
    cp=0
    j=i
    while j <len(L)-1 and L[i][1]>=L[j][0]:
        if L[i][1]>=L[j][1]:
            cp+=1
        j+=1
    i+=1
    cps+=[cp]
print(max(cps))