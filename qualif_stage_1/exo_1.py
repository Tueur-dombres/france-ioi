nbjouets, nbcouleurs, nbgroupes = map(int,input().split())
L = list(map(int,input().split()))
dico = {i:[] for i in range(1,nbcouleurs+1)}
cp = 1
for i in range(1,nbjouets):
    if L[i]==L[i-1]:
        cp+=1
    else:
        dico[L[i-1]]+=[cp]
        cp=1
dico[L[i-1]]+=[cp]
for k,v in dico.items():
    dico[k] = sum(sorted(v,reverse = True)[:min(nbgroupes,len(v))])
print(max(dico.values()))