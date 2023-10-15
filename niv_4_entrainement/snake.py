H, L = map(int,input().split())
grille = [list(map(int,input().split())) for _ in range(H)]
grille[0][0] = -1

A = int(input())
mouvements = [list(map(int,input().split())) for _ in range(A)]
EST,NORD,OUEST,SUD = (1,0),(0,-1),(-1,0),(0,1) #x,y
directions = [SUD,OUEST,NORD,EST]

tete = [0,0] # x,y
queue = [0,0]

dir_tete = 3 #EST
dir_queue = 3 #EST

i_tete = 0
i_queue = 0

tour = 1
tour_queue = 1
vivant = True
stock_nourriture = 0
while vivant:
    if stock_nourriture > 0:
        stock_nourriture -= 1
    else:
        if i_queue < A and mouvements[i_queue][0] == tour_queue:
            dir_queue = (dir_queue+mouvements[i_queue][1])%4
            i_queue+=1
        grille[queue[1]][queue[0]] = 0
        queue = [queue[0]+directions[dir_queue][0],queue[1]+directions[dir_queue][1]]
        tour_queue += 1

    
    if i_tete < A and mouvements[i_tete][0] == tour:
        dir_tete = (dir_tete+mouvements[i_tete][1])%4
        i_tete+=1
    tete = [tete[0]+directions[dir_tete][0],tete[1]+directions[dir_tete][1]]

    if not 0 <= tete[0] < L or not 0 <= tete[1] < H or grille[tete[1]][tete[0]] == -1:
        vivant = False
    else:
        stock_nourriture += grille[tete[1]][tete[0]]
        grille[tete[1]][tete[0]] = -1
    
    tour+=1
    for e in grille:print(e)
    print(tour,queue,tete,stock_nourriture,vivant)
print(tour)