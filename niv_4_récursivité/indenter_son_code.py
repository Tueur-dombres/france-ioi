from sys import setrecursionlimit
a = input()
setrecursionlimit(len(a)+50)
def affichage(taille,pos):
    if pos == len(a):return
    if a[pos] == "{":
        print(taille*3*" "+"{")
        taille+=1
    else:
        taille-=1
        print(taille*3*" "+"}")
    affichage(taille,pos+1)

affichage(0,0)