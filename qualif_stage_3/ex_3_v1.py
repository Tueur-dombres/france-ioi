nbPics, nbTypes = map(int,input().split())
pics = list(map(int,input().split()))
types = list(map(int,input().split()))

st67 = True
for i in range(nbPics-1):
    if pics[i] >= pics[i+1]:
        st67 = False
        break
if st67:
    for type_actu in types:
        serie = min(nbPics, type_actu)
        comptage_possibilite = serie*(serie+1)//2
        print(comptage_possibilite)
else:
    for type_actu in types:
        comptage_possibilite = 0
        serie = 0
        for pic_actu in pics:
            if pic_actu <= type_actu:
                serie+=1
            else:
                comptage_possibilite += serie*(serie+1)//2
                serie = 0
        comptage_possibilite += serie*(serie+1)//2
        print(comptage_possibilite)