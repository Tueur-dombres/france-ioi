nblivres, nbjours = map(int,input().split())
livres_dispos = [1]*(nblivres)
livres_retour = {}
for i in range(nbjours):
    for livre in livres_retour.get(i,[]):
        livres_dispos[livre] = 1
    for _ in range(int(input())):
        livre, duree = map(int,input().split())
        if livres_dispos[livre]:
            livres_dispos[livre] = 0
            livres_retour[i+duree] = livres_retour.get(i+duree, [])+[livre]
            print(1)
        else:
            print(0)