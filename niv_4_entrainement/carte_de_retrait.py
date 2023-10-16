H, P, N = map(int,input().split())

depense = [0]*H
depense_courante = 0
for i in range(N):
    R = int(input())
    depense_courante -= depense[i%H]
    if depense_courante + R > P:
        depense[i%H] = 0
        print(0)
    else:
        depense[i%H] = R
        depense_courante += R
        print(1)