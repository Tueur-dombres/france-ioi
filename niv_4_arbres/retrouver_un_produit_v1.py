N = int(input())
Ks = list(map(int,input().split()))
R = int(input())
Rs = list(map(int,input().split()))
Chemins = [[i] for i in range(1,N+1)]

for i in range(1,N+1):
    j = i
    while Ks[j-1] != 0 and i<Ks[j-1]:
        j = Ks[j-1]
        Chemins[i-1] = [j] + Chemins[i-1]
    if Ks[j-1] != 0:
        Chemins[i-1] = Chemins[Ks[j-1]-1]+Chemins[i-1]
for e in Rs:
    print(" ".join(str(e) for e in Chemins[e-1]))