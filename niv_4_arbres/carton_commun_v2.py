N = int(input())
Ks = list(map(int,input().split()))
R = int(input())
Rs = [list(map(int,input().split())) for _ in range(R)]

for o1,o2 in Rs:
    L1 = [False for _ in range(N+1)]
    L2 = [False for _ in range(N+1)]
    last1 = o1
    last2 = o2
    while True:
        L1[last1]=True
        L2[last2]=True
        if L1[last2]:
            print(last2)
            break
        elif L2[last1]:
            print(last1)
            break
        if last1!=0:last1 = Ks[last1-1]
        if last2!=0:last2 = Ks[last2-1]