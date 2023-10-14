M = int(input())
entree = list(map(int,input().split()))

L = []
tempo = [0]*10**5
tempo_long = 0
tempo_vus = []
for i in range(len(entree)):
    if entree[i]==0:
        L+=[tempo_long]
        for elt in tempo_vus:
            tempo[elt] = 0
        tempo_vus = []
        tempo_long = 0
    else:
        if not tempo[entree[i]]:
            tempo_long+=1
            tempo[entree[i]] = 1
            tempo_vus += [entree[i]]
L+=[tempo_long]
    
print(max(L) if L else 0)