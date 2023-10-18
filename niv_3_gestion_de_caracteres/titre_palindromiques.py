import sys
input = sys.stdin.readline

def is_palindrome(chaine):
    a = chaine[:len(chaine)//2]
    b = chaine[:-len(chaine)//2-(len(chaine)+1)%2:-1]
    #print(a == b, a, b, sep="\n", end = "\n\n")
    return a == b

def main():
    nblivres = int(input())
    retour = []
    for _ in range(nblivres):
        livre = input()[:-1]
        if is_palindrome("".join([e.lower() for e in livre if e!=" "])):
            retour.append(livre)
    print("\n".join(retour))

main()