nbGrenouilles  = int(input())
nbTours = int(input())
grenouille_pos = [0]*(nbGrenouilles+1)
grenouille_score = [0]*(nbGrenouilles+1)
grenouille_premiere = -1
grenouille_pos_premiere = 0
for _ in range(nbTours):
    if grenouille_premiere != -1:
        grenouille_score[grenouille_premiere] += 1
    grenouille, saut = map(int,input().split())
    grenouille_pos[grenouille] += saut
    if grenouille_pos[grenouille] == grenouille_pos_premiere:
        grenouille_premiere = -1
    elif grenouille_pos[grenouille] > grenouille_pos_premiere:
        grenouille_premiere = grenouille
        grenouille_pos_premiere = grenouille_pos[grenouille]

gagnant = 1
for grenouille in range(2,nbGrenouilles+1):
    if grenouille_score[grenouille] > grenouille_score[gagnant]:
        gagnant = grenouille
print(gagnant)