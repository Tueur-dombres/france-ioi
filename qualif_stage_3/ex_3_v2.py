nbPics, nbTypes = map(int,input().split())
L_pics = list(map(int,input().split()))
types = list(map(int,input().split()))

types_tries = sorted(types)
valeurs_types = {}

def comptage(n):
    return n*(n+1)//2

def dicho(L, elt):
    a = 0
    b = len(L)
    while b > a + 1:
        m = (a + b) // 2
        if L[m] > elt:
            b = m
        else:
            a = m
    return a-1 if L[a] == elt else a

splits = [[] for _ in range(nbTypes)]
for i_pic,pic in enumerate(L_pics):
    if pic <= types_tries[0]:
        pass
    else:
        i = dicho(types_tries, pic)
        while i < nbTypes and pic > types_tries[i]:
            i+=1
        splits[i].append(i_pic)
print(splits)
intervalles = [[0,nbPics-1]]
valeur_type_actu = nbPics*(nbPics+1)//2
for i_type in range(nbTypes-1,-1,-1):
    new_intervalles = []
    i_split = 0
    for inter in intervalles:
        splits_sur_cet_intervalle = [inter[0]-1]
        while i_split < len(splits[i_type]) and inter[0] <= splits[i_type][i_split] <= inter[1]:
            splits_sur_cet_intervalle.append(splits[i_type][i_split])
            i_split += 1

        splits_sur_cet_intervalle.append(inter[1]+1)
                
        intervalles_a_ajouter = []
        for k in range(len(splits_sur_cet_intervalle)-1):
            intervalles_a_ajouter += [[splits_sur_cet_intervalle[k] + 1, splits_sur_cet_intervalle[k+1] -1]]
            
        
        valeur_type_actu = valeur_type_actu - comptage(inter[1]-inter[0]+1) + sum(comptage(e[1] - e[0] + 1) for e in intervalles_a_ajouter)
        new_intervalles += intervalles_a_ajouter

    valeurs_types[types_tries[i_type]] = valeur_type_actu
    intervalles = new_intervalles

for type_affiche in types:
    print(valeurs_types[type_affiche])
