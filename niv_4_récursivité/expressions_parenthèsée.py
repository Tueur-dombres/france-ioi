from sys import setrecursionlimit
L = input()
setrecursionlimit(len(L)+50)
print(len(L),L)
def recherche(pos):
    global L
    if pos==len(L):
        print("THE END")
        return "yes"
    if not L[pos] in "()[]{}<>":
        return recherche(pos+1)
    elif L[pos] in "([{<":
        print("open", pos, L[pos])
        tempo = recherche(pos+1)
        print(pos,tempo)
        if tempo in ("no","yes"):
            print("faux")
            return "no"
        else:
            print(tempo,"verif_fermeture",L[pos],L[tempo],L[pos:])
            if "([{<".index(L[pos]) == ")]}>".index(L[tempo]):
                suivant  = recherche(tempo+1)
                return suivant
            else:
                return "no"
    else:
        print("close", pos, L[pos])
        return pos

print("yes" if recherche(0)=="yes" else "no")