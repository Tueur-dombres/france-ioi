N,K = map(int,input().split())
def choisir(nbLettres,choix,pos):
    if nbLettres == 0:
        print(" ".join(str(e) for e in choix))
    else:
        for i in range(pos,N+2-nbLettres):
                choisir(nbLettres-1,choix+[i],i+1)

choisir(K,[],1)