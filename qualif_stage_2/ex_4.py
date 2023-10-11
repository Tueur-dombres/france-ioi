T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    D = int(input())
    graphe_autoroutes = [[] for _ in range(N+1)]
    graphe_nationales = [[] for _ in range(N+1)]
    for _ in range(M):
        u,v,t = map(int,input().split())
        if t == 1:
            graphe_autoroutes[u]+=[v]
        else:
            graphe_nationales[u]+=[v]

    d_possible = [D]
    vus = {D}
    i = 0
    while i < len(d_possible):
        for ville in graphe_autoroutes[d_possible[i]]+graphe_nationales[d_possible[i]]:
            if ville not in vus:
                vus.add(ville)
                d_possible.append(ville)
        i+=1
    perdre_des_cles = False
    for I in d_possible:
        vus_in_I = {I}
        I_possible = [I]
        i = 0
        while i < len(I_possible):
            for ville in graphe_autoroutes[I_possible[i]]+graphe_nationales[I_possible[i]]:
                if ville not in vus_in_I:
                    vus_in_I.add(ville)
                    I_possible.append(ville)
            i+=1
        perdre_ses_cles_en_I = False
        for F in I_possible[1:]:
            vus_in_F = {F}
            F_possible = [F]
            i = 0
            perdre_ses_cles_en_F = True
            while i < len(F_possible):
                if F_possible[i] == I:
                    perdre_ses_cles_en_F = False
                    break
                for ville in graphe_nationales[F_possible[i]]:
                    if ville not in vus_in_F:
                        vus_in_F.add(ville)
                        F_possible.append(ville)
                i+=1
            if perdre_ses_cles_en_F == True:
                perdre_ses_cles_en_I = True
                break
        
        if perdre_ses_cles_en_I == True:
            perdre_des_cles = True
            break
    print("Oui" if perdre_des_cles else "Non")


