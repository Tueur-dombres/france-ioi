def lissage(L):
    retour = [L[0]]
    diff = 0
    for i in range(1,len(L)):
        new_val = (L[i-1]+L[i+1])/2 if i != len(L)-1 else L[i]
        retour += [new_val]
        if abs(retour[-1]-retour[-2]) > diff: diff = abs(retour[-1]-retour[-2])
        
    return retour, diff

taille = int(input())
diffmax = float(input())
signal_base = [float(input()) for _ in range(taille)]
signal = signal_base.copy()
diff = max(abs(signal[i]-signal[i-1]) for i in range(1,taille)) if taille >= 2 else 0
cp = 0
while diff >= diffmax:
    signal, diff = lissage(signal)
    cp+=1
print(cp)