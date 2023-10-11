N = int(input())
Ks = list(map(int,input().split()))
R = int(input())
Rs = list(map(int,input().split()))
Chemins = [[i] for i in range(1,N+1)]
bool_Rs_vus = [False for _ in range(N)]

for i in Rs:
    j = i
    while Ks[j-1] != 0 and not bool_Rs_vus[j-1]:
        j = Ks[j-1]
        Chemins[i-1] = [j] + Chemins[i-1]
    if Ks[j-1] != 0:
        Chemins[i-1] = Chemins[Ks[j-1]-1]+Chemins[i-1]
        bool_Rs_vus[i-1] = True

    print(" ".join(str(e) for e in Chemins[i-1]))