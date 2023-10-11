N = int(input())
L = [int(e) for e in input().split()]

mask = input()
i_connus = [i for i in range(len(mask)) if mask[i]!="?"]
size = len(mask)
size_min = 10**(size-1)
size_max = min(10**size,N+1)

valides_a_trier = [False for _ in range(N+1)]
for code in range(size_min,size_max):
    valide = True
    for i in i_connus:
        if mask[i]!=str(code)[i]:
            valide = False
            break
    if valide:
        valides_a_trier[code]=True

arbre = [[] for _ in range(N+1)]
for fils in range(1,N+1):
    père = L[fils-1]
    arbre[père] += [fils]

a_afficher = []
current_row = [0]
while current_row:
    row_suivante = []
    for noeud in current_row:
        row_suivante+=arbre[noeud]
        if valides_a_trier[noeud]:
            a_afficher += [noeud]
    current_row = row_suivante.copy()
print(" ".join(str(e) for e in a_afficher))