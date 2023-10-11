N = int(input())
Ks = list(map(int,input().split()))
R = int(input())
Rs = list(map(int,input().split()))

for e in Rs:
    L=[e]
    while L[-1]!=0:
        L+=[Ks[L[-1]-1]]
    print(" ".join(str(e) for e in L[-2::-1]))
    