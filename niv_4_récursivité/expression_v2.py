from sys import setrecursionlimit
L = input()
setrecursionlimit(len(L)+50)
def recherche(pos):
    global L
    if pos>len(L):
        return "yes"
    if not L[pos] in "()[]{}<>":
        return recherche(pos+1)
    elif L[pos] in "([{<":
        tempo = recherche(pos+1)
        if tempo in ("no","yes"):
            return "no"
        else:
            return "yes" if "([{<".index(L[pos]) == ")]}>".index(L[tempo]) and recherche(tempo+1) != "no" else "no"
    else:
        return pos

print("yes" if recherche(0)=="yes" else "no")