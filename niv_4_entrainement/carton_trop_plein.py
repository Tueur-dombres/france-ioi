N = int(input())
objets_pos = list(map(int,input().split()))
nb_objets_dans_objet = [0]*(N+1)
for obj in objets_pos:
    nb_objets_dans_objet[obj]+=1
print(max(nb_objets_dans_objet))