import sys
input = sys.stdin.readline

def main():
    compteur = [0]*26
    cp_tot = 0
    for lettre in input().lower():
        if lettre.isalpha(): 
            compteur[ord(lettre)-ord("a")] += 1
            cp_tot += 1
    print("\n".join([str(e/cp_tot) for e in compteur]))

main()