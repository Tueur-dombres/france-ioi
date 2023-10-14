G,N = map(int,input().split())
t1s = []
t2s = []
for _ in range(N):
    t1,t2 = map(int,input().split())
    t1s.append(t1)
    t2s.append(t2)
t1s.sort()
t2s.sort()

current_touristes = 0
retour = True
i,j = 0,0
while i<N:
    if t1s[i]<t2s[j]:
        current_touristes+=1
        i+=1
    else:
        current_touristes-=1
        j+=1
    if current_touristes > G:
        retour = False
        break
print(1 if retour else 0)
