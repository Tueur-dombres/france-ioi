N = int(input())
Ks = list(map(int,input().split()))
R = int(input())
Rs = [list(map(int,input().split())) for _ in range(R)]

for o1,o2 in Rs:
    L1 = [False for _ in range(N+1)]
    L1[0] = True
    last = o1
    while last!=0:
        L1[last]=True
        last = Ks[last-1]
    last = o2
    while not L1[last]:
        last = Ks[last-1]
    print(last)