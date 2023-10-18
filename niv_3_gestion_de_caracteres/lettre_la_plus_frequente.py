import sys
input = sys.stdin.readline

def main():
    compteur = [0]*26
    for lettre in input().lower():
        if lettre.isalpha(): compteur[ord(lettre)-ord("a")] += 1
    print(chr(compteur.index(max(compteur))+ord("A")))

main()