nbParticipants = int(input())
L = sorted(map(int,input().split()))
nbParticipants = len(L)
Li = sorted(int(str(e)[::-1]) for e in L)
cp = 0
j = 0
for i in range(nbParticipants):
    while j<nbParticipants and L[i]>Li[j]:
        j+=1
    if j>=nbParticipants:break
    if L[i]==Li[j]:
        cp+=1
        j+=1

print(nbParticipants-cp)