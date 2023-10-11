nbCartons = int(input())
arbre = [input().split()[1:] for _ in range(nbCartons+1)]

def parcours(noeud):
    print("A",noeud)
    for no in arbre[int(noeud)]:
        parcours(int(no))
    print("R",noeud)

for no in arbre[0]:parcours(no)