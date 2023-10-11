N,K = map(int,input().split())
A = list(map(int,input().split()))
i=0
vus = []
while i < N+K:
    if i not in vus:
        j = N+K-1
        while j > i:
            if j not in vus:
                s = A[i]+A[j]
                paires = [A[i],A[j]]
                vus+=[i,j]
                inf,sup = i+1,j-1
                while inf < sup:
                    tempo_sup = sup
                    while inf<tempo_sup and A[inf]+A[tempo_sup]>s:
                        tempo_sup-=1
                    if A[inf]+A[tempo_sup]==s:
                        paires = paires[:len(paires)//2]+[A[inf],A[tempo_sup]]+paires[len(paires)//2:]
                        sup-=1
                        vus+=[inf,tempo_sup]
                    inf+=1
                if len(paires)==N:
                    print(" ".join(str(e) for e in paires))
                    j = i = N+K
            j-=1
    i+=1